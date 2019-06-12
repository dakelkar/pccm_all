import pandas as pd
import os
import sqlite3
from datetime import date
from modules.pccm_names import ffpe_db_tables
from sql.add_update_sql import table_check
import modules.table_dicts as table_dicts


class PrintFFPEDb:

    def __init__(self, folder, file, user_name):
        self.folder = folder
        self.file = file
        self.user_name = user_name

    def print_file(self, research):
        extract_data = ExtractData(self.folder, self.file, self.user_name, research)
        output_file, output_folder = extract_data.output_names()
        extract_data.output_data(output_file, output_folder)


class ExtractData:
    def __init__(self, folder, file, user_name, research):
        self.path = os.path.join(folder, file)
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        self.folder = folder
        self.file = file
        self.user_name = user_name
        self.research = research

    def output_names(self):
        output_folder = os.path.join(self.folder, 'data_output')
        output_file, extension = self.file.split('.d')
        if self.research:
            output_file = str(date.today()).replace('-', '_') + "_Research_" + output_file + '.xlsx'
            print(output_file)
        else:
            output_file = str(date.today()).replace('-', '_') + '_' + output_file + '.xlsx'
            print(output_file)
        return output_file, output_folder

    def print_table(self, writer, table):
        modules = table_dicts.table_module_dict(table)
        if self.research:
            modules = table_dicts.table_module_research(table)
        if modules:
            columns = []
            for module in modules:
                cols = table_dicts.db_dict(table, module)
                columns = columns + cols
        else:
            modules = 'no_modules'
            columns = table_dicts.db_dict(table, modules)
        if 'file_number' not in columns:
            col_list = ['file_number'] + columns
        else:
            col_list = columns
        if self.user_name != 'dk':
            sql_statement = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
        else:
            sql_statement = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "' WHERE file_number NOT LIKE "
                                                                                   "'%delete'")
        df = pd.read_sql(sql_statement, self.conn)
        number = df.shape[0]
        df.to_excel(writer, sheet_name=table, startrow=0, index=False, header=True)
        return number

    def output_data(self, output_file, output_folder):
        tables_to_print = []
        summary_df = pd.DataFrame(columns=["table_name", "number_entries"])
        output_path = os.path.join(output_folder, output_file)
        for table in ffpe_db_tables():
            check = table_check(self.cursor, table)
            if check:
                tables_to_print.append(table)
        writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        index = 0
        for table in tables_to_print:
            number = self.print_table(writer, table)
            summary_df.loc[index] = [table, number]
            index = index + 1
        self.print_summary(summary_df, output_file, output_folder)
        writer.save()

    @staticmethod
    def print_summary(summary_df, output_file, output_folder):
        output_name = 'Summary_' + output_file
        ex_path = os.path.join(output_folder, output_name)
        writer = pd.ExcelWriter(ex_path, engine='xlsxwriter')
        summary_df.reset_index(drop=True, inplace=True)
        summary_df.to_excel(writer, sheet_name="Summary", index=False)
        writer.save()
        return
