import sqlite3
import ask_y_n_statement
import add_update_sql as add
path = "DB\\PCCM_BreastCancerDB_2018-03-09.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()
next = True
files_added = []
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
    files_added.append(file_number)
    next = ask_y_n_statement.ask_y_n("Add/update another record?")
print("Folders added in this session are: " + ", ".join(files_added))
quest = ask_y_n_statement.ask_y_n("Do you want to quit?", quit())


