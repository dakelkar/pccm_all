import sqlite3
import os.path
from pccm_bcdb_add import add_new, update_record
from ask_y_n_statement import ask_y_n
folder = input ("Folder name: ")
db_name = input("DB name: ")
path = os.path.join(folder, db_name)
conn = sqlite3.connect(path)
cursor = conn.cursor()
table = "Patient_Information_History"
next = True
while next:
    check = False
    while not check:
        file_number = input("File Number: ")
        print("File Number: " + file_number)
        check = ask_y_n("Is this file number correct")
    sql = "SELECT rowid FROM Patient_Information_History WHERE File_number = ?"
    cursor.execute(sql, (file_number,))
    data=cursor.fetchall()
    if len(data)==0:
        cursor.execute("INSERT INTO Patient_Information_History(File_number) VALUES ('"+file_number+"')")
        print (file_number + " does not exist in table Patient_Information_History. Enter new record")
        add_new(conn, cursor, file_number, table)
    else:
        print(file_number + " already exists. Update record")
        update_record(conn, cursor, file_number, table)
    next = ask_y_n("Add/update another record?")
