import modules.ask_y_n_statement as ask
import sql.add_update_sql as sql
import sqlite3
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

    def surgery_block_information_1(self, block_data_type= 'primary_surgery'):
        module_name = "surgery_block_information_1"
        check = False
        while not check:
            block_sr = input("Surgery Block Serial Number: ")
            surg_block_id = input("Surgical Block ID: ")
            surg_no_block = input("Number of Blocks (please input only number): ")
            surg_block_source = input("Pathology Lab (source of block): ")
            breast_cancer_yes_no = ask.ask_y_n('Is this a case of breast cancer', yes_ans="yes", no_ans="no")
            pathology_report_available_yes_no = ask.ask_y_n('Is the pathology report available', yes_ans="yes", no_ans="no")
            surg_date = ask.check_date("Date of Surgery: ")
            surg_name = ask.ask_option("Name of the Surgeon/s", ["Dr. C. B. Koppiker"])
            surg_hosp_id = input("Hospital ID: ")
            lesion_side = ask.ask_option("Lesion on", ["Right Breast", "Left Breast", 'Unilateral',"Bilateral"])
            try:
                nact = sql.get_value(col_name='NACT_status', table='Neo_Adjuvant_Therapy', file_number=self.file_number,
                                     cursor=self.cursor)
            except sqlite3.Error:
                nact = "Data to be filled"
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

            data_list_1 = [block_data_type, block_sr,surg_block_id, surg_no_block, breast_cancer_yes_no,
                           pathology_report_available_yes_no, surg_block_source, surg_date, surg_name, surg_hosp_id, lesion_side, nact, surg_type]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list_1)
        return data_list_1

    def surgery_block_information_2(self):
        module_name = "surgery_block_information_2"
        check = False
        while not check:
            try:
                no_blocks = sql.get_value(col_name='Number_Blocks_Surgery_Block', table=self.table, file_number=self.file_number,
                                     cursor=self.cursor)
            except sqlite3.Error:
                no_blocks = input("Please input number of blocks (if block information is not available please enter 0: ")
            try:
                block_id = sql.get_value(col_name='Block_ID_Surgery_Block', table=self.table,
                                          file_number=self.file_number, cursor=self.cursor)
            except sqlite3.Error:
                block_id = input("Please input block id: ")
            block_desc_df, block_data_all = BlockDescription.block_description(self.file_number, block_id, no_blocks)
            tumour_size = input("Tumour size (please input digits only): ")
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
            necrosis = ask.ask_y_n_na("Necrosis", yes_ans='necrosis_yes', no_ans='necrosis_no', na_ans='Data not in Report')
            percent_vasc_invasion = input("Percent Vascular Invasion "
                                          "Enter number only; Enter 'Data not in report' if not available: ")
            percent_lymph_invasion = input("Percent Lymphocyte Invasion "
                                          "Enter number only; Enter 'Data not in report' if not available: ")
            percent_stroma = input("Percent Stroma "
                                          "Enter number only; Enter 'Data not in report' if not available: ")
            margin = ask.ask_option("Margins", ["Involved", "Free"])
            margin_id, margin_type = ('NA', )*2
            if margin == 'Involved':
                margin_id = input('Margin that is involved: ')
                margin_type = input('Margin type: ')
            tumour_block_ref, node_block_ref, ad_normal_block_ref, red_tissue_block_ref \
                = ask.join_lists(block_data_all, sep="; ")
            data_list = [tumour_block_ref, node_block_ref, ad_normal_block_ref, red_tissue_block_ref,tumour_size, tumour_unit,
                         tumour_grade, surg_diag, dcis_percent, tumour_invasion, per_inv, necrosis, percent_vasc_invasion,
                         percent_lymph_invasion, percent_stroma, margin, margin_id, margin_type]
            columns_list = names(module_name)
            check = sql.review_input(self.file_number, columns_list, data_list)
        return (tuple(data_list), block_desc_df)

    def surgery_block_information_3 (file_number):
        module_name = "surgery_block_information_3"
        check = False
        while not check:
            surgery_er = ask.ask_option("ER Status", ["Positive", "Negative", "Data not available", "Other"])
            if (surgery_er == "Positive"):
                surgery_er_percent = input("ER Percent: ")
            else:
                surgery_er_percent = "ER status " + surgery_er
            surgery_pr = ask.ask_option("PR Status", ["Positive", "Negative", "Data not available", "Other"])
            if (surgery_pr == "Positive"):
                surgery_pr_percent = input("PR Percent: ")
            else:
                surgery_pr_percent = "PR status " + surgery_pr
            surgery_her2 = ask.ask_option("HER2 Status", ["Positive", "Equivocal", "Negative", "Test Not Done", "Other"])
            surgery_her2_grade = input("HER2 Grade: ")
            surgery_fish = ask.ask_option("FISH", ["Positive", "Negative"])
            surgery_ki67 = input("Ki67 Percent: ")
            sent_data = node_details("Sentinel")
            sentinel, sent_number_rem, sent_number_pos, sent_number = sent_data
            ax_data = node_details("Axillary")
            ax, ax_number_rem, ax_number_pos, ax_number = ax_data
            print("Axillary Node Number: " + ax_number)
            ap_data = node_details("Apical")
            ap, ap_number_rem, ap_number_pos, ap_number = ap_data
            per_spread = ask.ask_y_n_na("Perinodal Spread", yes_ans='Yes', no_ans='No', na_ans='Data not in Report')
            supra_inv = ask.ask_y_n_na("Supraclavicular Node Involvment", yes_ans='Yes', no_ans='No', na_ans='Data not in Report')
            data_list = [surgery_er ,surgery_er_percent, surgery_pr, surgery_pr_percent, surgery_her2, surgery_her2_grade,
                         surgery_fish, surgery_ki67,sentinel, sent_number_rem, sent_number_pos, ax, ax_number_rem,
                         ax_number_pos, ax_number, ap, ap_number_rem, ap_number_pos, per_spread, supra_inv]
            columns_list = names(module_name)
            check = add_update_sql.review_input(file_number, columns_list, data_list)
        return (tuple(data_list))


    def node_details (node_name):
        node_name + " Node"
        number_removed = input("Number of "+node_name+" Nodes removed: ")
        if number_removed==0:
            node, number_removed, number_positive, number = ("No node removed", )*4
        else:
            number_positive = input("Number of "+node_name+" Nodes positive: ")
            if int(number_positive)>0:
                node = "Positive"
                if int(number_positive) < 4:
                    number = '1'
                elif int(number_positive) < 10:
                    number = '2'
                else:
                    number = '3'
            else:
                node = "Negative"
                number = 0

        data = [node, number_removed, number_positive, number]
        return data

    def path_stage(file_number, user_name):
        module_name = "path_stage"
        check = False
        while not check:
            category = "pT"
            options = ["is", "0", "1", "2", "3", "4", "Other"]
            pT = ask.ask_option(category, options)
            category = "pN"
            options = ["0", "1", "2", "3", "4", "Other"]
            pN = ask.ask_option(category, options)
            category = ("M")
            options = ["0", "1", "Other"]
            M = ask.ask_option(category, options)
            path_stage = "pT" + pT + "N" + pN + "M" + M
            clinical_stage = 'NA'
            print ("Pathological Stage: "+ path_stage)
            check = ask.ask_y_n("Is pathological stage correct")
            if not check:
                path_stage = input("Please enter correct pathological stage: ")
            if M in {"1", "2", "3"} :
                clinical_stage = "IV"
            elif M == "0":
                if pN == "3":
                    clinical_stage = "IIIC"
                elif pN == "2":
                    if pT == "4":
                        clinical_stage = "IIIB"
                    else:
                        clinical_stage = "IIIA"
                elif pN == "1mi":
                    clinical_stage = "IB"
                elif pN == "1":
                    if (pT=="0" or pT == "1"):
                        clinical_stage = "IIA"
                    elif pT=="2":
                        clinical_stage = "IIB"
                    elif pT == "3":
                        clinical_stage = "IIIA"
                    elif pT =="4":
                        clinical_stage = "IIIB"
                    else:
                        clinical_stage = input("Clinical Staging: ")
                elif pN =="0":
                    if pT =="is":
                        clinical_stage = "0"
                    elif pT == "1":
                        clinical_stage = "IA"
                    elif pT =="2":
                        clinical_stage = "IIA"
                    elif pT == "3":
                        clinical_stage = "IIB"
                    elif pT == "4":
                        clinical_stage = "IIIB"
                    else:
                        clinical_stage = input("Clinical Staging: ")
            else:
                clinical_stage = input("Clinical Staging: ")
            print ("Clinical stage "+ clinical_stage)
            print ("Based on TNM status", path_stage, "and TABLE 2 of Giuliano et al., 2017, CA CANCER J "
                                                      "CLIN 2017;67:290–303")
            check = ask.ask_y_n("Is clinical stage correct")
            if not check:
                clinical_stage = input("Please enter correct clinical stage: ")
            last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
            data_list = [pT, pN, M, path_stage, clinical_stage, user_name, last_update]
            columns_list = names(module_name)
            check = add_update_sql.review_input(file_number, columns_list, data_list)
        return (tuple(data_list))


    def add_data(conn, cursor, file_number, user_name):
        table = "Surgery_Block_Report_Data"
        enter = ask.ask_y_n("Enter Surgery Block information?")
        if enter:
            data = surgery_block_information_1(file_number,cursor)
            add_update_sql.update_multiple(conn, cursor, table, names("surgery_block_information_1"), file_number, data)
        enter = ask.ask_y_n("Enter Surgery Block information (Tumour Details) ?")
        if enter:
            data, block_data_df = surgery_block_information_2(file_number, cursor)
            add_update_sql.update_multiple(conn, cursor, table, names("surgery_block_information_2"), file_number, data)
            block_data_df.to_sql("", conn, index=False, if_exists="append")
        enter = ask.ask_y_n("Enter Surgery Block information (Node Details)?")
        if enter:
            data = surgery_block_information_3(file_number)
            add_update_sql.update_multiple(conn, cursor, table, names("surgery_block_information_3"), file_number, data)
        enter = ask.ask_y_n("Enter Pathological Stage?")
        if enter:
            data = path_stage(file_number, user_name)
            add_update_sql.update_multiple(conn, cursor, table, names("path_stage"), file_number, data)


    def edit_data(conn, cursor, file_number, user_name):
        table = "Surgery_Block_Report_Data"
        print("Surgery Block information")
        col_list = names("surgery_block_information_1")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = surgery_block_information_1(file_number, cursor)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print ("Surgery Block information (Tumour Details)")
        col_list = names("surgery_block_information_2")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            add_update_sql.delete_rows(cursor, 'block_data', "file_number", file_number)
            data, block_data_df = surgery_block_information_2(file_number, cursor)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
            block_data_df.to_sql("", conn, index=False, if_exists="append")
        print("Surgery Block information (Node Details)")
        col_list = names("surgery_block_information_3")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = surgery_block_information_3(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Pathological Stage")
        col_list = names("path_stage")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = path_stage(file_number, user_name)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)