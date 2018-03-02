import sqlite3
import os.path
import ask_y_n_statement
import add_update_sql as add
folder = input ("Folder name: ")
db_name = input("DB name: ")
path = os.path.join(folder, db_name)
conn = sqlite3.connect(path)
cursor = conn.cursor()
next = True
while next:
    check = False
    while not check:
        file_number = input("File Number: ")
        print("File Number: " + file_number)
        check = ask_y_n_statement.ask_y_n("Is this file number correct")
    table = ask_y_n_statement.ask_option("Table", ["Patient_Information_History", "Clinical_Exam", "Block_Report_Data", "All"])
    if table != "All":
        add.check_file(conn, cursor, table, file_number)
    else:
        tables = ["Patient_Information_History", "Clinical_Exam", "Block_Report_Data"]
        for index in tables:
            add.check_file(conn, cursor, index, file_number)
    next = ask_y_n_statement.ask_y_n("Add/update another record?")


