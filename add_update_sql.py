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
    sql_insert = "INSERT INTO Patient_Information_History(File_number) VALUES (?)", file_number
    cursor.execute(sql_insert, data)
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
    from ask_y_n_statement import ask_y_n
    col_number = len (data)
    print ("Entries for database are as follows : ")
    for index in range (0, col_number):
        print (columns[index] +": " + data[index])
    ans = ask_y_n("Are entries for file "+ file_number+ " correct ?", True, False)
    return ans