import pandas as pd
import string
import modules.ask_y_n_statement as ask
from modules.pccm_names import names_surgery as names

class BlockDescription():

    def __init__(self, file_number, block_id, block_no):
        self.file_number = file_number
        self.block_id= block_id
        self.block_no = block_no
        self.block_desc_df_cols = names('block_data')


    def block_description (self):
        block_type_list = names('block_type_list')
        block_desc_df = pd.DataFrame(columns=self.block_desc_df_cols)
        if int(self.block_no) == 0:
            block_desc_df.loc[self.block_no] = ['No blocks available', 'NA', 'NA']
        else:
            block_id_list =BlockDescription.create_block_id(self)
            for id in range(0,len(block_id_list)):
                print ("For Block ID "+self.block_id+', Block reference: '+block_id_list[id])
                block_type = ask.ask_option("Block type", block_type_list)
                block_desc = input("Block Description for block "+block_id_list[id]+": ")
                block_desc_df.loc[id] = [self.file_number, self.block_id, block_id_list[id], block_type, block_desc]
            print(block_desc_df)
            check = ask.ask_y_n("Are block descriptions correct?")
            if not check:
                to_correct = ask.ask_y_n("Correct all entries?")
                if not to_correct:
                    to_do =True
                    while to_do:
                        id = input("Enter block id to change: ")
                        print (block_desc_df.loc[id, :])
                        col_change = ask.ask_option("Name of column to change", self.block_desc_df_cols)
                        new_val = input("Enter correct value for "+col_change +' for '+id)
                        block_desc_df.loc[id, col_change] = new_val
                        print(block_desc_df)
                        to_do = ask.ask_y_n("Make more changes?")
        block_data_all =BlockDescription.block_description_for_db(self,block_desc_df)
        return block_desc_df, block_data_all

    def block_description_for_db(self, block_desc_df):
        block_type_list = names('block_type_list')
        block_data_all = []
        for type in block_type_list:
            query_type = 'block_type == ' + '"' + type + '"'
            id_desc = block_desc_df.query(query_type)
            if list(id_desc.shape)[0] == 0:
                block_data_type = ['Not Removed']
                block_data_all.append(block_data_type)
            else:
                block_data_type = []
                id = list(id_desc['block_reference'])
                desc = list(id_desc['block_description'])
                for index in range(list(id_desc.shape)[0]):
                    data = id[index] + ": " + desc[index]
                    block_data_type.append(data)
                block_data_type = ["; ".join(block_data_type)]
                block_data_all.append(block_data_type)
        return block_data_all

    def create_block_id(self):
        block_id_list = []
        block_no = int(self.block_no)
        block_id_chunks = list(divmod(block_no, 26))
        chunk = block_id_chunks[0]
        suffix = [i for i in range(chunk)]
        if chunk == 0:
            for j in range(block_id_chunks[1]):
                alph_list = string.ascii_uppercase[j]
                block_id_list.append(alph_list)
        else:
            for i in range(chunk):
                if i == chunk - 1:
                    for j in range(block_id_chunks[1]):
                        alph_list = string.ascii_uppercase[j] + str(i)
                        block_id_list.append(alph_list)
                else:
                    for j in range(26):
                        alph_list = string.ascii_uppercase[j] + suffix[i]
                        block_id_list.append(alph_list)
        print((", ").join(block_id_list))
        check_list = ask.ask_y_n("Is block list correct?")
        while not check_list:
            block_id_list = []
            for i in range(block_no):
                id = input('Block id of block number ' + str(i + 1) + ': ')
                block_id_list.append(id)
            print((", ").join(block_id_list))
            check_list = ask.ask_y_n("Is block list correct?")
        return block_id_list

    @staticmethod
    def rb_lb_data (df, cols):
        data_all = []
        for col in cols:
            data = list(df[col])
            data_all.append(data)
        if list(df.shape)[0] == 2:
            for data in data_all:
                data[0] = 'RB: ' + data[0]
                data[1] = 'LB: ' + data[1]
        data_list = ask.join_lists(data_all, "| ")
        return data_list

    @staticmethod
    def breast_list(breast_biopsy):
        if breast_biopsy == "Bilateral":
            breasts = ('RB', 'LB')
        else:
            breasts = [breast_biopsy]
        return breasts

    @staticmethod
    def block_details():
        block_sr = input("Biopsy Block Serial Number: ")
        block_location = BlockDescription.block_location()
        block_id = input("Biopsy Block ID: ")
        block_number = input("Number of blocks: ")
        data = block_sr, block_location, block_id, block_number
        return data


    @staticmethod
    def block_location():
        location = False
        while location == False:
            print("Biopsy Block Location: ")
            block_cab = input("Cabinet No: ")
            block_drawer = input("Drawer Number: ")
            block_col = input("Column Number: ")
            block_pos = ask.ask_option("Is Block in", ["Front", "Back"])
            block_location = block_cab + "-" + block_drawer + "-" + block_col + block_pos[0]
            print("Block location is " + block_location)
            location = ask.ask_y_n("Is this correct?")
        return block_location

    @staticmethod
    def ihc_report():
        tumour_er = ask.ask_option("ER Status", ["ER_positive", "ER_negative"])
        if tumour_er == "ER_positive":
            tumour_er_percent = input("ER Percent (number only), Enter 'Data not in Report' if %age not available: ")
        else:
            tumour_er_percent = tumour_er
        tumour_pr = ask.ask_option("PR Status", ["PR_positive", "PR_negative"])
        if tumour_pr == "PR_positive":
            tumour_pr_percent = input("PR Percent (number only), Enter 'Data not in Report' if %age not available: ")
        else:
            tumour_pr_percent = tumour_pr
        tumour_her2 = ask.ask_option("HER2 Status", ["HER2_positive", "HER2_negative",
                                                     "HER2_equivocal"])
        tumour_her2_grade = input("HER2 Grade: ")
        tumour_fish = ask.ask_option("FISH", ["FISH_positive", "FISH_negative", "FISH Not Done"])
        tumour_ki67 = input("Ki67 Percent, Number only, Enter 'Not Done' if test not done: ")
        data = tumour_er, tumour_er_percent, tumour_pr, tumour_pr_percent, tumour_her2, tumour_her2_grade, tumour_fish,\
               tumour_ki67
        return data