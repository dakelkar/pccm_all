import modules.ask_y_n_statement as ask
import sql.add_update_sql as sql
import modules.pccm_names as names
from datetime import datetime
from additional_tables.block_description import BlockDescription

class BiopsyData:
    def __init__(self, conn, cursor, file_number, user_name):
        self.table = 'Biopsy_Report_Data'
        self.file_number = file_number
        self.cursor = cursor
        self.user_name = user_name
        self.conn = conn
        self.block_type = 'biopsy'

    # check column names


    def migrate_block_data(self):
        columns = 'block_id'
        block_information = sql.get_block_id_multiple(col_name=tuple(columns), table = 'Block_list',
                                          file_number=self.file_number, cursor=self.cursor,
                                          block_type=self.block_type)
        if len(set(block_information))>1:
            block_id = ask.ask_list('Which block is information to be entered for: ', set(block_information))
        else:
            block_id = block_information
        return block_id


    def biopsy_report_info(self, file_number='test'):
        check = False
        while not check:
            block_id = BiopsyData.migrate_block_data(self)
            reason_biopsy = ask.ask_option('Reason_for_Biopsy', ['Diagnostic', 'Follow-up', 'NACT follow-up',
                                                                 'Recurrence'])
            biopsy_site = ask.ask_option('Biopsy_site', ['Left Breast', 'Right Breast', ' Left Axilla', 'Right Axilla'])
            biopsy_report_pccm = ask.ask_y_n_na("Is the biopsy report available?", yes_ans="Biopsy_report_PCCM_yes",
                                                no_ans="Biopsy_report_PCCM_no", na_ans="Biopsy Not Done")
            ihc_report_pccm = ask.ask_y_n_na("Is the IHC report available?", yes_ans="IHC_report_PCCM_yes",
                                             no_ans="IHC_report_PCCM_no", na_ans="IHC Not Done")
            if block_id == 'NA':
                block_id = input('Block id: ')
                block_series = input('Block series: ')
                no_of_blocks = 'NA'
            else:
                block_series = set(sql.get_block_id_multiple(col_name='block_series', table='Block_list',
                                          file_number=self.file_number, cursor=self.cursor, block_type=block_id))
                no_of_blocks = set(sql.get_block_id_multiple(col_name='no_of_blocks', table='Block_list',
                                          file_number=self.file_number, cursor=self.cursor, block_type=block_id))
            block_details = [block_id, block_series, no_of_blocks,reason_biopsy, biopsy_site, biopsy_report_pccm,
                             ihc_report_pccm]
            biopsy_details = [biopsy_report_pccm] * 9
            if biopsy_report_pccm == 'Biopsy_report_PCCM_yes':
                biopsy_details = BiopsyData.biopsy_details(self, block_id)
            elif biopsy_report_pccm == 'Biopsy_report_PCCM_no':
                biopsy_details = ['Requires Follow-up'] * 9
            ihc_details = [ihc_report_pccm] * 11
            if ihc_report_pccm == 'IHC_report_PCCM_yes':
                ihc_details = BiopsyData.ihc_data(self, block_id)
            elif biopsy_report_pccm == 'IHC_report_PCCM_no':
                ihc_details = ['Requires Follow-up'] * 9
            last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
            col_list = names.names_biopsy_x('block_details')
            check = sql.review_input(file_number, col_list, block_details)
            data_list = block_details, biopsy_details, ihc_details + [last_update] + [self.user_name]
        return data_list

    def ihc_data(self, block_id):
        module_name = "ihc_data"
        columns_list = names.names_biopsy_x(module_name)
        check = False
        while not check:
            print('Please input all data for ' + block_id + ' block only')
            tumour_er, tumour_er_percent, tumour_pr, tumour_pr_percent, tumour_her2, tumour_her2_grade, \
            tumour_fish, tumour_ki67 = BlockDescription.ihc_report('Tumour_biopsy')
            fnac = ask.ask_y_n_na(question="Lymph Node biopsy FNAC",
                                  yes_ans="Lymph_Node_biopsy_FNAC_yes",
                                  no_ans="Lymph_Node_biopsy_FNAC_no", na_ans="Data not in report")
            fnac_location, fnac_diagnosis = (fnac,) * 2
            if fnac == "Lymph_Node_biopsy_FNAC_yes":
                fnac_location = input("Please enter lymph node biopsy location: ")
                fnac_diagnosis = ask.ask_option("Lymph Node biopsy diagnosis",
                                                ["Lymph_Node_biopsy_malignant",
                                                 "Lymph_Node_biopsy_non_malignant",
                                                 "Data not in report"])
            data_list = [tumour_er, tumour_er_percent, tumour_pr, tumour_pr_percent, tumour_her2,
                               tumour_her2_grade, tumour_fish, tumour_ki67, fnac, fnac_location, fnac_diagnosis]
            check = sql.review_input(self.file_number, columns_list, data_list)
        return data_list

    def biopsy_details(self, block_id):
        check = False
        while not check:
            print('Please input all data for ' + block_id + ' report only')
            biopsy_date = ask.check_date("Date of Biopsy: ")
            biopsy_source = ask.ask_option('Source of Biopsy Block', ['Golwilkar Lab', 'AG Diagnostics',
                                                                      'Ruby Hall Clinic'])
            biopsy_lab_id = input("Biopsy Lab ID/SID: ")
            biopsy_type = ask.ask_option("Biopsy Type", ["Trucut", "VAB", 'Excision', 'FNAC'])
            biopsy_diagnosis = input('Enter the diagnosis in its full form (eg., Infiltrating Duct Carcinoma): ')
            biopsy_comments = input('Enter any additional comments on the diagnosis: ')
            tumour_grade = ask.ask_option("Tumour Biopsy Diagnosis", ["I", "II", "III"])
            lymph_emboli = ask.ask_y_n_na(question="Are Lymphovascular emboli seen?",
                                          yes_ans='Lymphovascular_emboli_biopsy_seen',
                                          no_ans='Lymphovascular_emboli_biopsy_not_seen', na_ans='Data not in report')
            dcis_biopsy = ask.ask_y_n_na(question="Does the biopsy show DCIS", yes_ans="DCIS_biopsy_yes",
                                         no_ans="DCIS_biopsy_no", na_ans="Data not in report")
            data_list = [biopsy_date, biopsy_source, biopsy_lab_id, biopsy_type, biopsy_diagnosis, biopsy_comments,
                         tumour_grade, lymph_emboli, dcis_biopsy]
            col_list = names.names_biopsy_x('biopsy_details')
            check = sql.review_input(self.file_number, col_list, data_list)
        return data_list

    def add_data(self):
        enter = ask.ask_y_n("Enter Biopsy Block Report information?")
        if enter:
            data = BiopsyData.biopsy_report_info(self)
            sql.update_multiple(self.conn, self.cursor, self.table, names.names_biopsy_new("biopsy_report_info"), self.file_number, data)
        enter = ask.ask_y_n("Enter Tumour Biopsy data?")
        if enter:
            data = BiopsyData.biopsy_report_info(self)
            sql.update_multiple(self.conn, self.cursor, self.table, names.names_biopsy_new("tumour_biopsy_data"), self.file_number, data)

    def edit_data(self):
        print("Block Report information")
        col_list = names.names_biopsy_new("biopsy_report_info")
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = BiopsyData.biopsy_report_info(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
        print("Tumour Biopsy data")
        col_list = names.names_biopsy_new("tumour_biopsy_data")
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = BiopsyData.biopsy_report_info(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)