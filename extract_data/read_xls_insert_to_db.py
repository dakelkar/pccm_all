import pandas as pd
import sqlite3
import os
import uuid
import sql.add_update_sql as sql
import modules.pccm_names as names

# add new columns to table.
file_xls = '2019_07_10_PCCM_BreastCancerDB_devyani_2019_06_13.xlsx'
folder_xls = 'D:/OneDrive/iiser_data/Prashanti_docs/Database_files/Block_data_biopsy_surgery'
table_name = 'block_list'

xls_path = os.path.join(folder_xls, file_xls)
df = pd.read_excel(xls_path, sheet_name = table_name)
df.head()
file_db = 'PCCM_BreastCancerDB_2019_07_10_Devyani.db'
folder_db = 'd:/repos/pccm_db/main/DB'
db_path = os.path.join(folder_db, file_db)
df = df.astype(str)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
columns = names.block_list('all')
for index in range(df.shape[0]):
    data = list(df.loc[index])
    pk = uuid.uuid4().hex
    sql.add_pk_fk_to_table(conn, cursor, table_name, col_filter='pk', pk=pk)
    print(data[0])
    sql.update_multiple_key(conn, cursor, table_name, columns=columns, key_name='pk',
                            key_value=pk, data=data)


