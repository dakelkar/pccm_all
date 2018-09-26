import pandas as pd
import sqlite3
import os
import modules.pccm_names as pccm_names
import sql.add_update_sql as sql
from datetime import datetime

#create new table
path_all = 'D:/repos/pccm_db/main/DB/DB_with_real_data/PCCM_BreastCancerDB_all_data.db'
os.path.isfile(path_all)
conn_all = sqlite3.connect(path_all)
cursor_all = conn_all.cursor()
table = "Biopsy_Report_Data"
file_number = "File_number"
if sql.table_check(cursor_all, table) == 0:
    cursor_all.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    module_names = ["biopsy_report_info", "tumour_biopsy_data", "lymphnode_biopsy"]
    for index in module_names:
        col_name = pccm_names.names_biopsy(index)
        sql.add_columns(cursor_all, table, col_name)

#read from excel with same col names and distribution as in table

file_to_read = "D:/Documents/IISER/Prashanti_docs/Breast_Cancer_FFPE_blocks_database_Biopsy_dk08062018.xlsx"
data = pd.read_excel(file_to_read,header=1, dtype = 'object' ,usecols= 'A:AB')
update_by = "dk from ruhi/shaheen data"
last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
module_names = ["biopsy_report_info", "tumour_biopsy_data", "lymphnode_biopsy"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + pccm_names.names_biopsy(index)
columns = ", ".join(col_list)
for index in range (0, len(data)):
    data_list = list(data.loc[index])
    data_list.append(update_by)
    data_list.append(last_update)
    sql.insert(conn_all, cursor_all, table, columns, data_list)

#for surgery_report
table = "Surgery_Block_Report_Data"
if sql.table_check(cursor_all, table) == 0:
    cursor_all.execute('CREATE TABLE {tn}({nf})' .format(tn=table, nf=file_number))
    module_names = ["surgery_block_information_1","surgery_block_information_2", "surgery_block_information_3",
                    "path_stage"]
    for index in module_names:
        col_name = pccm_names.names_surgery(index)
        sql.add_columns(cursor_all, table, col_name)

#add data

file_to_read = "D:/Documents/IISER/Prashanti_docs/Breast_Cancer_FFPE_blocks_database_Surgery_dk08062018.xlsx"
data = pd.read_excel(file_to_read,header=1, dtype = 'object' ,usecols= 'A:BB')
update_by = "dk from ruhi/shaheen data"
last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
module_names = ["surgery_block_information_1","surgery_block_information_2", "surgery_block_information_3",
                    "path_stage"]
col_list = ["File_number"]
for index in module_names:
    col_list = col_list + pccm_names.names_surgery(index)
columns = ", ".join(col_list)
for index in range (0, len(data)):
    data_list = list(data.loc[index])
    data_list.append(update_by)
    data_list.append(last_update)
    sql.insert(conn_all, cursor_all, table, columns, data_list)