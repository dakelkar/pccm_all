import modules.ask_y_n_statement as ask
import sql.add_update_sql as sql
from modules.pccm_names import names_surgery as names
from additional_tables.block_description import BlockDescription
from datetime import datetime

class SurgeryBlockData:
    def __init__(self, conn, cursor, file_number, user_name):
        self.table = 'Surgery_Block_Report_Data'
        self.file_number = file_number
        self.cursor = cursor
        self.user_name = user_name
        self.conn = conn
        self.module_list = ['surgery_block_information_1', 'surgery_block_information_2', 'surgery_block_information_3',
                            'path_stage']

    def surgery_block_information_1(self, block_data_type= 'primary_surgery'):
        module_name = self.module_list[0]
        check = False
        while not check:
            data_type = ask.ask_y_n("Is surgery type '" + block_data_type + "'")
            if not data_type:
                block_data_type = input ("Please input type of surgery: ")
            block_sr_no = input("Surgery Block Serial Number: ")
            surg_block_id = input("Surgical Block ID: ")
            surg_no_block = input("Number of Blocks (please input only number): ")
            surg_block_source = input("Pathology Lab (source of block): ")
            breast_cancer_yes_no = ask.ask_y_n('Is this a case of breast cancer',
                                               yes_ans="breast cancer_yes", no_ans="breast cancer_no")
            pathology_report_available_yes_no = ask.ask_y_n('Is the pathology report available', yes_ans="yes",
                                                            no_ans="no")
            surg_date = ask.check_date("Date of Surgery: ")
            surg_name = ask.ask_option("Name of the Surgeon/s", ["Dr. C. B. Koppiker"])
            surg_hosp_id = input("Hospital ID: ")
            lesion_side = ask.ask_option("Lesion on", ["Right Breast", "Left Breast", 'Unilateral',"Bilateral"])
            nact = sql.get_value(col_name='NACT_status', table='Neo_Adjuvant_Therapy', file_number=self.file_number,
                                     cursor=self.cursor, error_statement= "Please enter (Data to be filled) for NACT "
                                                                          "details here")
            surg_list = ['Mastectomy','Modified Radical Mastectomy','Breast Conservation Surgery',
                         'Therapeutic Mammoplasty', 'Reduction Mammoplasty', 'Lumpectomy (Wide Local Excision)',
                         "Reconstruction"]
            if lesion_side != "Bilateral":
                surg_type = ask.ask_option("Type Surgery", surg_list)
            else:
                print ("Right Breast Surgery")
                surg_type = ask.ask_option("Type Surgery", surg_list)
                surg_type_rb = "RB: "+surg_type
                print("Left Breast Surgery")
                surg_type = ask.ask_option("Type Surgery", surg_list)
                surg_type_lb = "LB: " + surg_type
                surg_type = surg_type_rb+"; "+surg_type_lb
            data_list_1 = [block_data_type, block_sr_no, surg_block_id, surg_no_block, breast_cancer_yes_no,
                           pathology_report_available_yes_no, surg_block_source, surg_date, surg_name, surg_hosp_id,
                           lesion_side, nact, surg_type]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list_1)
        return data_list_1

    def surgery_block_information_2(self):
        module_name = self.module_list[1]
        check = False
        while not check:
            no_blocks = sql.get_value(col_name='Number_Blocks_Surgery_Block', table=self.table,
                                      file_number=self.file_number, cursor=self.cursor, error_statement=
                                      "Please input number of blocks (if block information is not available "
                                      "please enter 0: ")
            block_id = sql.get_value(col_name='Block_ID_Surgery_Block', table=self.table, file_number=self.file_number,
                                     cursor=self.cursor, error_statement="Please input block id: ")
            blocks = BlockDescription(self.file_number, block_id, no_blocks)
            block_desc_df, block_data_all = blocks.block_description()
            breast_cancer_yes_no = sql.get_value(col_name='Breast_Cancer_Yes_No_Surgery_Block', table = self.table,
                                                 file_number=self.file_number, cursor=self.cursor,
                                                 error_statement='Is this a case of breast cancer if yes answer if yes '
                                                                 'answer breast cancer_yes and if no answer '
                                                                 'breast cancer_no')
            tumour_size, tumour_unit, tumour_grade, surg_diag, dcis_yes_no, dcis_type, dcis_percent, tumour_invasion, \
            per_inv, necrosis, percent_vasc_invasion, percent_lymph_invasion, percent_stroma, margin, margin_id, \
            margin_type = (breast_cancer_yes_no, )*16
            if breast_cancer_yes_no == 'breast cancer_yes':
                tumour_size = input("Tumour size (please input dimension only, e.g, 1 x 3 x 4): ")
                tumour_unit = ask.ask_option("Tumour size unit", ['mm', 'cm'])
                tumour_grade = ask.ask_option("Tumour Grade", ["I", "II", "III"])
                surg_diag = ask.ask_option("Surgery Diagnosis", names('diagnosis'))
                dcis_yes_no = ask.ask_y_n_na('Is DCIS present', yes_ans='dcis_yes', no_ans='dcis_no',
                                             na_ans='Data not in Report')
                dcis_type, dcis_percent = (dcis_yes_no,) * 2
                if dcis_yes_no == 'dcis_yes':
                    dcis_type = input('Enter type of DCIS if textual description given (else enter NA): ')
                    dcis_percent = input("Percent DCIS (number only): ")
                tumour_invasion = ask.ask_option("Type of Tumour Invasion", ['Microinvasion', 'Macroinvasion'])
                per_inv = ask.ask_y_n_na(question="Perineural Invasion", yes_ans='perineural_invasion_yes',
                                         no_ans='perineural_invasion_no',na_ans='Data not in Report')
                necrosis = ask.ask_y_n_na("Necrosis", yes_ans='necrosis_yes', no_ans='necrosis_no',
                                          na_ans='Data not in Report')
                percent_vasc_invasion = input("Percent Vascular Invasion "
                                              "Enter number only; Enter 'Data not in report' if not available: ")
                percent_lymph_invasion = input("Percent Lymphocyte Invasion "
                                              "Enter number only; Enter 'Data not in report' if not available: ")
                percent_stroma = input("Percent Stroma "
                                              "Enter number only; Enter 'Data not in report' if not available: ")
                margin = ask.ask_option("Margins", ["Surgery_Block_Margins_involved", "Surgery_Block_Margins_free"])
                margin_id, margin_type = ('NA', )*2
                if margin == 'Surgery_Block_Margins_involved':
                    margin_id = input('Margin that is involved: ')
                    margin_type = input('Margin type: ')
            tumour_block_ref, node_block_ref, ad_normal_block_ref, red_tissue_block_ref \
                = ask.join_lists(block_data_all, sep="; ")
            data_list = [tumour_block_ref, node_block_ref, ad_normal_block_ref, red_tissue_block_ref,tumour_size,
                         tumour_unit, tumour_grade, surg_diag, dcis_yes_no, dcis_type, dcis_percent, tumour_invasion,
                         per_inv, necrosis, percent_vasc_invasion, percent_lymph_invasion, percent_stroma, margin,
                         margin_id, margin_type]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list)
        return (tuple(data_list), block_desc_df)

    def surgery_block_information_3 (self):
        module_name = self.module_list[2]
        check = False
        while not check:
            surgery_er, surgery_er_percent, surgery_pr, surgery_pr_percent, surgery_her2, surgery_her2_grade, \
            surgery_fish, surgery_ki67, = BlockDescription.ihc_report()
            sentinel, sent_number_rem, sent_number_pos = SurgeryBlockData.node_details("Sentinel")
            ax, ax_number_rem, ax_number_pos = SurgeryBlockData.node_details("Axillary")
            ap, ap_number_rem, ap_number_pos = SurgeryBlockData.node_details("Apical")
            per_spread = ask.ask_y_n_na("Perinodal Spread", yes_ans='Yes', no_ans='No', na_ans='Data not in Report')
            supra_inv = ask.ask_y_n_na("Supraclavicular Node Involvment", yes_ans='Yes', no_ans='No',
                                       na_ans='Data not in Report')
            data_list = [surgery_er ,surgery_er_percent, surgery_pr, surgery_pr_percent, surgery_her2,
                         surgery_her2_grade, surgery_fish, surgery_ki67, sentinel, sent_number_rem, sent_number_pos, ax,
                         ax_number_rem, ax_number_pos, ap, ap_number_rem, ap_number_pos, per_spread, supra_inv]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list)
        return (tuple(data_list))

    def path_stage(self):
        module_name = self.module_list[3]
        check = False
        while not check:
            category = "pT"
            options = ["is", "0", "1", "2", "3", "4", "Other"]
            pt = ask.ask_option(category, options)
            category = "pN"
            options = ["0", "1", "2", "3", "4", "Other"]
            pn = ask.ask_option(category, options)
            category = ("M")
            options = ["0", "1", "Other"]
            m = ask.ask_option(category, options)
            path_stage, clinical_stage = BlockDescription.stage(pt, pn, m)
            last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
            data_list = [pt, pn, m, path_stage, clinical_stage, self.user_name, last_update]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list)
        return (tuple(data_list))

    def add_data(self):
        enter = ask.ask_y_n("Enter Surgery Block information?")
        if enter:
            data = SurgeryBlockData.surgery_block_information_1(self)
            col_list = names(self.module_list[0])
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
        enter = ask.ask_y_n("Enter Surgery Block information (Tumour Details) ?")
        if enter:
            col_list = names(self.module_list[1])
            data, block_data_df = SurgeryBlockData.surgery_block_information_2(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
            block_data_df.to_sql("block_data", self.conn, index=False, if_exists="append")
        enter = ask.ask_y_n("Enter Surgery Block information (Node Details)?")
        if enter:
            col_list = names(self.module_list[2])
            data = SurgeryBlockData.surgery_block_information_3(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
        enter = ask.ask_y_n("Enter Pathological Stage?")
        if enter:
            col_list = names(self.module_list[3])
            data = SurgeryBlockData.path_stage(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)

    def edit_data(self):
        print("Surgery Block information")
        col_list = names(self.module_list[0])
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = SurgeryBlockData.surgery_block_information_1(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
        print("Surgery Block information (Tumour Details)")
        col_list = names(self.module_list[1])
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            sql.delete_rows(self.cursor, 'block_data', "file_number", self.file_number)
            data, block_data_df = SurgeryBlockData.surgery_block_information_2(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
            block_data_df.to_sql("block_data", self.conn, index=False, if_exists="append")
        print("Surgery Block information (Node Details)")
        col_list = names(self.module_list[2])
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = SurgeryBlockData.surgery_block_information_3(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)
        print("Pathological Stage")
        col_list = names(self.module_list[3])
        enter = sql.review_data(self.conn, self.cursor, self.table, self.file_number, col_list)
        if enter:
            data = SurgeryBlockData.path_stage(self)
            sql.update_multiple(self.conn, self.cursor, self.table, col_list, self.file_number, data)

    @staticmethod
    def node_details(node_name):
        print(node_name + " Node")
        number_removed = input("Number of " + node_name + " Nodes removed: ")
        if number_removed == 0:
            node, number_removed, number_positive = ("No node removed",) * 3
        else:
            number_positive = input("Number of " + node_name + " Nodes positive: ")
            if int(number_positive) > 0:
                node = "Positive"
            else:
                node = "Negative"
        data = [node, number_removed, number_positive]
        return data
