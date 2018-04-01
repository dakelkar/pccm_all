def add_insert():
    import sqlite3
    import modules.ask_y_n_statement as ask_y_n_statement
    import sql.add_update_sql as add_update_sql
    from datetime import datetime
    import os.path
    import textwrap
    folder = 'd:/repos/pccm_all/main/DB\PCCM_BreastCancerDB3_2018-03-22.db'
    file = "PCCM_BreastCancerDB1_2018-03-15.db"
    path = os.path.join(folder, file)
    if os.path.isfile(folder):
        conn = sqlite3.connect(folder)
        cursor = conn.cursor()
        folder_next = True
        files_added = []
        user_name = input("Please input username/user_id: ")
        while folder_next:
            check = False
            while not check:
                file_number = input("File Number: ")
                print("File Number: " + file_number)
                check = ask_y_n_statement.ask_y_n("Is this file number correct")
            table = ask_y_n_statement.ask_option("Table", ["Patient_Information_History", "Biopsy_Report_Data","Clinical_Exam", "Surgery_Block_Report_Data", "All"])
            if table != "All":
                add_update_sql.check_file(conn, cursor, table, file_number)
            else:
                tables = ["Patient_Information_History", "Biopsy_Report_Data","Clinical_Exam", "Surgery_Block_Report_Data", "All"]
                for index in tables:
                    add_update_sql.check_file(conn, cursor, index, file_number)
            files_added.append(file_number)
            folder_next = ask_y_n_statement.ask_y_n("Add/update another record?")
        data = "Folders added/edited by " +user_name+" in this session are: " + ", ".join(files_added)
        file_name = user_name+ datetime.now().strftime('%Y_%m_%d_at_%H_%M')+".txt"
        path = os.path.join(folder, file_name)
        f = open(path, 'w')
        f.write(data)
        f.close()
    else:
        note = "current path: '" + path + "' to database is not valid. Check path and database name and run " \
                                          "start_pccm_db() again."
        wrapper = textwrap.TextWrapper(width=75)
        string = wrapper.fill(text=note)
        print(string)

