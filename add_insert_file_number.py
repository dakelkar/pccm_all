import sqlite3
import ask_y_n_statement
import add_update_sql as add
from datetime import datetime
import os.path
path = "DB\\PCCM_BreastCancerDB1_2018-03-15.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()
next = True
quest = False
files_added = []
user_name = input("Please input username/user_id: ")
while next:
    check = False
    while not check:
        file_number = input("File Number: ")
        print("File Number: " + file_number)
        check = ask_y_n_statement.ask_y_n("Is this file number correct")
    table = ask_y_n_statement.ask_option("Table", ["Patient_Information_History", "Biopsy_Report_Data","Clinical_Exam", "Surgery_Block_Report_Data", "All"])
    if table != "All":
        add.check_file(conn, cursor, table, file_number)
    else:
        tables = ["Patient_Information_History", "Biopsy_Report_Data","Clinical_Exam", "Surgery_Block_Report_Data", "All"]
        for index in tables:
            add.check_file(conn, cursor, index, file_number)
    files_added.append(file_number)
    next = ask_y_n_statement.ask_y_n("Add/update another record?")
data = "Folders added/edited by " +user_name+" in this session are: " + ", ".join(files_added)
folder = "DB"
file_name = user_name+ datetime.now().strftime('%Y_%m_%d_at_%H_%M')+".txt"
path = os.path.join(folder, file_name)
f = open(path, 'w')
f.write(data)
f.close()

