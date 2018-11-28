import sqlite3
import os
import pandas as pd

path_all = 'D:/repos/pccm_db/main/DB/DB_pilot_10/PCCM_BreastCancerDB_added_name_and_update1_2018-04-18.db'
os.path.isfile(path_all)
conn_all = sqlite3.connect(path_all)
cursor_all = conn_all.cursor()
table = "Patient_Information_History"
sql = "SELECT File_number FROM table = '"+table+"'"
df = pd.read_sql(sql, conn_all)
sql = "ATTACH DATABASE 'PCCM_BreastCancerDB_added_name_and_update1_2018-04-18' As 'Nutan_data'"
table = cursor_all.execute(sql)
names = table.fetchall()
