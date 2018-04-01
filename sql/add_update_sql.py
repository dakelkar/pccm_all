def update_single(conn, cursor, table, column, file_number, var):
    # update a single column in a sql db. Key is file_number.
    sql_update = "UPDATE " + table + " SET " + column + "= ? WHERE File_number = '" + file_number + "'"
    cursor.execute(sql_update, [var])
    conn.commit()


def insert(conn, cursor, table, columns, data):
    # insert data in multiple cols in a sql db. adds a new row
    col_number = len(data)
    place_holder = ["?"] * col_number
    place_str = ",".join(place_holder)
    sql_insert = "INSERT INTO " + table + "(" + columns + ") VALUES (" + place_str + ")"
    cursor.execute(sql_insert, data)
    conn.commit()

def insert_file_number (conn, cursor, file_number):
    # insert data in multiple cols in a sql db. adds a new row
    sql_insert = "INSERT INTO Patient_Information_History(File_number) VALUES (?)"
    cursor.execute(sql_insert, file_number)
    conn.commit()

def update_multiple(conn, cursor, table, columns, file_number, data):
    # update multiple columns in a sql db. Key is file_number.
    col_number = len(data)
    for index in range(0, col_number):
        sql_update = "UPDATE " + table + " SET " + columns[index] + "= ? WHERE File_number = '" + file_number + "'"
        var = data[index]
        cursor.execute(sql_update, [var])
    conn.commit()


def add_columns(cursor, table, columns):
    col_number = len(columns)
    for index in range(0, col_number):
        sql_add = "ALTER TABLE " + table + " ADD " + columns[index]
        cursor.execute(sql_add)

def review_input (file_number, columns, data):
    import modules.ask_y_n_statement as ask_y_n_statement
    col_number = len (data)
    print ("Entries for database are as follows : ")
    for index in range (0, col_number):
        print (columns[index] +": " + data[index])
    ans = ask_y_n_statement.ask_y_n("Are entries for file "+ file_number+ " correct ?", True, False)
    return ans

def review_data (conn, cursor, table, file_number, col_list):
    import modules.ask_y_n_statement as ask
    sql = ('SELECT '+ ", ".join(col_list) +' FROM '+ table + " WHERE File_number = '" +file_number+"'")
    data = cursor.execute(sql)
    data_list = data.fetchall()
    data_list = list(data_list[0])
    col_number = len(col_list)
    if data_list== [None]*len(data_list):
        print("This section of the database has not been entered")
        enter = ask.ask_y_n("Do you want to enter now")
        return enter
    if None in set(data_list):
        print("Some entries are missing from the database: ")
        for index in range (0, col_number):
            print (col_list[index]+ " : " + str(data_list[index]))
        enter = ask.ask_option("Do you want to proceed?", ["Edit all", "Add new data only"])
        if enter == "Edit all":
            return True
        else:
            edit_few(conn, cursor, table, col_list, file_number, data_list)
    else:
        print("Entries present in database are as follows : ")
        for index in range (0, col_number):
            print (col_list[index]+ " : " + str(data_list[index]))
        enter = ask.ask_option("Do you want to", ["Edit all", "Edit some entries", "Edit None"])
        if enter == "Edit some entries":
            for index in range(0, col_number):
                print(col_list[index] + " : " + str(data_list[index]))
                edit = ask.ask_y_n("Edit")
                if edit:
                    data = input("Data for " + col_list[index] + ": ")
                    update_single(conn, cursor, table, col_list[index], file_number, data)
            return False
        elif enter == "Edit all":
            return True
        else:
            return False

def edit_few(conn, cursor, table, col_list, file_number, data_list):
    col_number = len (col_list)
    for index in range (0, col_number):
        if data_list[index] == None:
            data = input ("Data for "+col_list[index]+": ")
            update_single(conn, cursor, table, col_list[index], file_number, data)
    return False

def check_file(conn, cursor, table, file_number):
    import modules.ask_y_n_statement as ask_y_n_statement
    import add_edit.add_new as add_new
    import add_edit.edit_record as edit_record
    sql = "SELECT rowid FROM " + table + " WHERE File_number = ?"
    cursor.execute(sql, (file_number, ))
    data = cursor.fetchall()
    if len(data) == 0:
        cursor.execute("INSERT INTO " + table + "(File_number) VALUES ('" + file_number + "')")
        print(file_number + " does not exist in table " + table + ". Enter new record")
        add_new.add_new(conn, cursor, file_number, table)
    else:
        todo = ask_y_n_statement.ask_option(file_number + " already exists in table " + table + ".",
                                            ["Edit record", "Add new record for same file number", "Edit None"])
        if todo == "Edit record":
            edit_record.edit_record(conn, cursor, file_number, table)
        elif todo =="Add new record for same file number":
            print("Add additional record module TBD")
        else:
            print ("Proceeding to next table")

def review_df(df):
   import modules.ask_y_n_statement as ask
   print (df)
   check = ask.ask_y_n("Is data entered correct?")
   return check