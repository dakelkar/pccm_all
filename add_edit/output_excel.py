import pandas as pd
import os
import sqlite3
from modules.ask_y_n_statement import ask_option, ask_y_n
from datetime import date
from modules.pccm_names import db_tables
from sql.add_update_sql import table_check
import modules.table_dicts as table_dicts


def output_data():
    path, ex_path, data_location_name = define_path()
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    tables_to_print = []
    summary_df = pd.DataFrame(columns=["table_name", "number_entries"])
    for table in db_tables():
        check = table_check(cursor, table)
        if check:
            tables_to_print.append(table)
    if not tables_to_print:
        print("Selected Database has no tables. Please re-start and edit database file")
        return
    else:
        writer = pd.ExcelWriter(ex_path, engine='xlsxwriter')
        print('This database contains the following tables:')
        i = 1
        for table in tables_to_print:
            print(str(i) + ". " + table)
            i = i+1
        to_print = ask_option("Do you want to print all tables or only select tables?",
                              ["All tables", "Select tables"])
        if to_print == "All tables":
            index = 0
            for table in tables_to_print:
                print_table(conn, writer, table)
                number = print_table(conn, writer, table)
                summary_df.loc[index] = [table, number]
                index = index + 1
        elif to_print == "Select tables":
            for table in tables_to_print:
                to_print = ask_y_n("Do you want to print " + table)
                if to_print:
                    print_table(conn, writer, table)
        print("Data file " + data_location_name[3] + " has been created at " + data_location_name[2]+'\n')
        print_summary(summary_df, data_location_name)
    writer.save()
    print("Data file " + data_location_name[3] + " has been created at " + data_location_name[2])


def define_path():
    data_location_name = ['D:/repos/pccm_db/main/DB', "PCCM_BreastCancerDB_all_data.db",
                          'D:/repos/pccm_db/main/DB', 'Output_' + str(date.today()) + '.xlsx']
    check_folder = None
    while check_folder != 'All are correct':
        print('\nFolder location of database file is set as: \n' + data_location_name[0] + '\n')
        print('Database file name is set as: \n' + data_location_name[1] + '\n')
        print('Output file destination is set as \n' + data_location_name[2] + '\n')
        print('Output file name is set as \n' + data_location_name[3] + '\n')
        check_folder = ask_option("Do you want to change any options?",
                                  ['Database Folder', 'Database File', 'Output File Destination',
                                   'Output File Name', 'All are correct'])
        if check_folder == 'Database Folder':
            print('Folder location of database file is set as: \n' + data_location_name[0] + '\n')
            data_location_name[0] = input("Please enter destination folder: ")
        elif check_folder == 'Database File':
            print('Database file name is set as: \n' + data_location_name[1] + '\n')
            data_location_name[1] = input("Please input correct database file name: ")
        elif check_folder == 'Output File Destination':
            print('Output file destination is set as: \n' + data_location_name[2] + '\n')
            data_location_name[2] = input("Please input correct output file destination: ")
        elif check_folder == 'Output File Name':
            print('Output file name is set as: \n' + data_location_name[3] + '\n')
            file_name = input("Please input correct output file name (without date and .xlsx): ")
            data_location_name[3] = file_name + '_' + str(date.today()) + '.xlsx'
    path = os.path.join(data_location_name[0], data_location_name[1])
    ex_path = os.path.join(data_location_name[2], data_location_name[3])
    return path, ex_path, data_location_name


def print_table(conn, writer, table):
    modules = table_dicts.table_module_dict(table)
    if table == 'Patient_Information_History':
        output_type = ask_y_n('Do you want a research print out for '+table+'?')
        if output_type:
            modules = table_dicts.table_module_research(table)
    columns = []
    if not modules:
        modules = 'no_modules'
        columns = table_dicts.db_dict(table, modules)
    else:
        for module in modules:
            cols = table_dicts.db_dict(table, module)
            columns = columns + cols
    col_list = table_dicts.create_col_list(columns)
    sql = ('SELECT ' + ", ".join(col_list) + " FROM '" + table + "'")
    df = pd.read_sql(sql, conn)
    number = df.shape[0]
    df.to_excel(writer, sheet_name=table, startrow=0,index=False, header=True)
    return number


def print_summary (df,data_location_name):
    data_location_name[3] = 'Summary_'+ data_location_name[3]
    ex_path = os.path.join(data_location_name[2], data_location_name[3])
    writer = pd.ExcelWriter(ex_path, engine='xlsxwriter')
    df.reset_index(drop=True, inplace=True)
    df.to_excel(writer, sheet_name="Summary", index = False)
    writer.save()
    return