def add_insert():
    import sqlite3
    import modules.ask_y_n_statement as ask_y_n_statement
    import sql.add_update_sql as add_update_sql
    from datetime import datetime
    import os
    import textwrap
    from modules.pccm_names import db_tables
    folders = "d:/repos/pccm_db/main/DB"
    file = 'PCCM_BreastCancerDB_test_biopsy_2018-09-08.db'
    #file = 'PCCM_BreastCancerDB_all_data_rituja_surgery_data.db'
    path = os.path.join(folders, file)
    if os.path.isfile(path):
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        user_name = input("Please input username/user_id: ")
        folder_next = True
        files_table_added = []
        while folder_next:
            check = False
            while not check:
                file_number = input("File Number: ")
                print("File Number: " + file_number)
                check = ask_y_n_statement.ask_y_n("Is this file number correct")
            check_table = True
            while check_table:
                table = ask_y_n_statement.ask_option("Table", db_tables())
                file_table = file_number + "-" + table
                files_table_added.append(file_table)
                check_table = add_update_sql.check_file(conn, cursor, table, file_number, user_name)
            folder_next = ask_y_n_statement.ask_y_n("Add/update another record?")
        data = "Folders added/edited by " +user_name+" in this session are: " + "; ".join(files_table_added)
        file_name = user_name+ datetime.now().strftime('%Y_%m_%d_at_%H_%M')+".txt"
        path = os.path.join(folders, file_name)
        f = open(path, 'w')
        f.write(data)
        f.close()
    else:
        note = "current path: '" + path + "' to database is not valid. Check path and database name and run " \
                                          "start_pccm_db() again."
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=note)
        print(string)

