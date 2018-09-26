import modules.ask_y_n_statement as ask
import sql.add_update_sql as sql
from modules.pccm_names import names_biopsy_new as names
from datetime import datetime
import pandas as pd
import sqlite3
from additional_tables.block_description import BlockDescription


def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Biopsy_Report_Data(File_number) VALUES ('" + file_number + "')")


class BiopsyData:
    def __init__(self, conn, cursor, file_number, user_name):
        self.table = 'Biopsy_Report_Data'
        self.file_number = file_number
        self.cursor = cursor
        self.user_name = user_name
        self.conn = conn

    def biopsy_report_info(self, file_number='test'):
        module_name = "biopsy_report_info"
        df_cols = names('biopsy_report_info_df')
        data_list_df = pd.DataFrame(columns=df_cols)
        check = False
        while not check:
            biopsy_report_pccm = ask.ask_y_n_na("Is the biopsy report available?", yes_ans="Biopsy_report_PCCM_yes",
                                                no_ans="Biopsy_report_PCCM_no", na_ans="Biopsy Not Done")
            ihc_report_pccm = ask.ask_y_n_na("Is the IHC report available?", yes_ans="IHC_report_PCCM_yes",
                                             no_ans="IHC_report_PCCM_no", na_ans="IHC Not Done")
            breast_biopsy = biopsy_report_pccm
            data_list = [biopsy_report_pccm] * 11
            data_list_df.loc[biopsy_report_pccm] = data_list
            if biopsy_report_pccm == 'Biopsy_report_PCCM_yes':
                data_list_df, breast_biopsy = BiopsyData.biopsy_details(self, df_cols)
            data_all = BlockDescription.rb_lb_data(data_list_df, df_cols)
            data_list = [biopsy_report_pccm, ihc_report_pccm, breast_biopsy]+data_all
            columns_list = names(module_name)
            check = sql.review_input(file_number, columns_list, data_list)
        return data_list

    def tumour_biopsy_data(self):
        module_name = "tumour_biopsy_data"
        columns_list = names(module_name)
        df_cols = columns_list[:-2]
        data_list_df = pd.DataFrame(columns=df_cols)
        try:
            ihc_biopsy = sql.get_value(col_name='IHC_report_PCCM_yes_no', table=self.table,
                                       file_number=self.file_number, cursor=self.cursor)
        except sqlite3.Error:
            ihc_biopsy = ask.ask_y_n_na("Is the IHC report available?", yes_ans="IHC_report_PCCM_yes",
                                        no_ans="IHC_report_PCCM_no", na_ans="IHC Not Done")
        check = False
        while not check:
            try:
                breast_biopsy = sql.get_value(col_name='Breast_Biopsy', table=self.table,
                                              file_number=self.file_number, cursor=self.cursor)
            except sqlite3.Error:
                breast_biopsy = ask.ask_option('Breast that biopsy has been done for',
                                               ['Right Breast', 'Left Breast', 'Unilateral', "Bilateral"])
            breasts = BlockDescription.breast_list(breast_biopsy)
            for breast in breasts:
                check_breast = False
                while not check_breast:
                    print('Please input all data for ' + breast + ' block only')
                    tumour_er, tumour_er_percent, tumour_pr, tumour_pr_percent, tumour_her2, tumour_her2_grade, \
                    tumour_fish, tumour_ki67 = (ihc_biopsy, )* 8
                    if ihc_biopsy == 'IHC_report_PCCM_yes':
                        ihc_data = BlockDescription.ihc_report()
                        tumour_er, tumour_er_percent, tumour_pr, tumour_pr_percent, tumour_her2, tumour_her2_grade, \
                        tumour_fish, tumour_ki67 = ihc_data
                    fnac = ask.ask_y_n_na(question=("Lymph Node biopsy FNAC for " + breast),
                                          yes_ans="Lymph_Node_biopsy_FNAC_yes",
                                          no_ans="Lymph_Node_biopsy_FNAC_no", na_ans="Data not in report")
                    fnac_location, fnac_diagnosis = (fnac,) * 2
                    if fnac == "Lymph_Node_biopsy_FNAC_yes":
                        fnac_location = input("Please enter lymph node biopsy location: ")
                        fnac_diagnosis = ask.ask_option("Lymph Node biopsy diagnosis",
                                                        ["Lymph_Node_biopsy_malignant",
                                                         "Lymph_Node_biopsy_non_malignant",
                                                         "Data not in report"])
                    df_data = [tumour_er, tumour_er_percent, tumour_pr, tumour_pr_percent, tumour_her2,
                                       tumour_her2_grade, tumour_fish, tumour_ki67, fnac, fnac_location, fnac_diagnosis]
                    print('Data entered for ' + breast + 'is as follows:\n')
                    check_breast = sql.review_input(self.file_number, df_cols, df_data)
                    data_list_df.loc[breast] = df_data
                data_list = BlockDescription.rb_lb_data(data_list_df, df_cols)
            check = sql.review_input(self.file_number, columns_list, data_list)
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = data_list+[last_update]+[self.user_name]
        return data_list

    def biopsy_details(self, df_cols):
        data_list_df = pd.DataFrame(columns=df_cols)
        breast_biopsy = ask.ask_option('Breast that biopsy has been done for',
                                       ['Right Breast', 'Left Breast', 'Unilateral', "Bilateral"])
        breasts = BlockDescription.breast_list(breast_biopsy)
        for breast in breasts:
            check_breast = False
            while not check_breast:
                print('Please input all data for ' + breast + ' report only')
                block_sr, block_location, block_id, block_number = ('block_not_available',) * 4
                block_check = ask.ask_y_n('Are the biopsy blocks available?')
                if block_check:
                    block_sr = input("Biopsy Block Serial Number: ")
                    block_location = BlockDescription.block_location()
                    block_id = input("Biopsy Block ID (include series identifiers): ")
                    block_number = input("Number of blocks: ")
                biopsy_date = ask.check_date("Date of Biopsy: ")
                biopsy_lab_id = input("Biopsy Lab ID/SID: ")
                print('Please input all data for ' + breast + ' block only')
                biopsy_type = ask.ask_option("Biopsy Type",
                                             ["Direct", "USG Guided", "VAB", "Tru-cut", "Steriotactic", 'Core',
                                              'Excision', 'FNAC', "Other"])
                category = "Tumour biopsy diagnosis"
                options = ['Benign', "Ductal carcinoma in situ(DCIS) with microinvasion",
                           "Ductal carcinoma in situ(DCIS) without microinvasion", "Lobular Carcinoma in Situ (LCS)",
                           "Invasive Ductal Carcinoma (IDC)", "Invasive Lobular Carcinoma (ILC)",
                           "Granulamatous Mastitis", "Papillary Carcinoma", "Phylloid Carcinoma",
                           "Invasive Mammary Carcinoma", "Invasive Breast Carcinoma", "Other"]
                tumour_diagnosis = ask.ask_option(category, options)
                tumour_grade = ask.ask_option("Tumour Biopsy Diagnosis", ["I", "II", "III"])
                lymph_emboli = ask.ask_y_n_na(question="Are Lymphovascular emboli seen?",
                                              yes_ans='Lymphovascular_emboli_biopsy_yes',
                                              no_ans='Lymphovascular_emboli_biopsy_no', na_ans='Data not in report')
                dcis_biopsy = ask.ask_y_n_na(question="Does the biopsy show DCIS", yes_ans="DCIS_biopsy_yes",
                                             no_ans="DCIS_biopsy_no", na_ans="Data not in report")
                df_data = [block_sr, block_location, block_id, block_number, biopsy_date, biopsy_lab_id, biopsy_type,
                           tumour_diagnosis, tumour_grade, lymph_emboli, dcis_biopsy]
                print('Data entered for ' + breast + ' is as follows:\n')
                check_breast = sql.review_input(self.file_number, df_cols, df_data)
            data_list_df.loc[breast] = df_data
        return data_list_df, breast_biopsy

    def add_data(self):
        enter = ask.ask_y_n("Enter Biopsy Block Report information?")
        if enter:
            data = BiopsyData.biopsy_report_info(self)
            sql.update_multiple(self.conn, self.cursor, self.table, names("biopsy_report_info"), self.file_number, data)
        enter = ask.ask_y_n("Enter Tumour Biopsy data?")
        if enter:
            data = BiopsyData.tumour_biopsy_data(self)
            sql.update_multiple(self.conn, self.cursor, self.table, names("tumour_biopsy_data"), self.file_number, data)

    def edit_data(self):
        print("Block Report information")
        col_list = names("biopsy_report_info")
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = BiopsyData.biopsy_report_info(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
        print("Tumour Biopsy data")
        col_list = names("tumour_biopsy_data")
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = BiopsyData.tumour_biopsy_data(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)