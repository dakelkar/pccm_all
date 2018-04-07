import modules.ask_y_n_statement as ask_y_n_statement
from sql.add_update_sql import review_input, update_multiple, review_data
import modules.pccm_names as names

def radiation (file_number):
    check = False
    while not check:
        radio = ask_y_n_statement.ask_y_n("Radiotherapy Recieved?")
        if not radio:
            radio = ask_y_n_statement.ask_option("Reason for not recieving radiotherapy", ["Not indicated", "Unable to afford",
                                                                                           "Patients reluctance",
                                                                                           "Logistic concerns"])
            radio_date,  radio_type, imrt, radio_tox, radio_delayed_tox, radio_finish, radio_location, radio_onco = ("NA", )*8
        else:
            radio = "Radiation therapy recieved"
            radio_date = input("Date of starting radiotherapy")
            radio_type = ask_y_n_statement.ask_option("Type of radiotherapy", ["Cobalt", "Linear Accelerator based treatment"])
            imrt = ask_y_n_statement.ask_y_n("Did the patient opt for Intensity Modulated/3Dimensional conformal radiotherapy ("
                                             "IMRT/3DCRT)")
            if imrt:
                imrt = "patient opted for Intensity Modulated/3Dimensional conformal radiotherapy (IMRT/3DCRT)"
            else:
                imrt = ask_y_n_statement.ask_option("Reasons for not opting for IMRT/3DCRT", ["Financial", "Not advised",
                                                                                              "Not known"])
            radio_tox = ask_y_n_statement.ask_option("Did radiotherapy related acute toxicity occur?", ["Yes", "No",
                                                                                                        "Not known"])
            radio_delayed_tox = ask_y_n_statement.ask_option("Did radiotherapy related delayed toxicity occur?", ["Yes", "No",
                                                                                                        "Not known"])
            radio_finish = input ("Date of finishing radiotherapy: ")
            radio_location = input("Location of radiotherapy: ")
            radio_onco = input("Name of Radiation Oncologist: ")
        data_list = [radio, radio_date,  radio_type, imrt, radio_tox, radio_delayed_tox, radio_finish, radio_location,
                     radio_onco]
        col_list =names.names_radiation()
        check = review_input(file_number, col_list, data_list)
    return data_list

def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Radiotherapy(File_number) VALUES ('" + file_number + "')")

def add_data(conn, cursor, file_number):
    file_row(cursor, file_number)
    table = "Radiotherapy"
    col_list = names.names_radiation()
    cursor.execute("INSERT INTO Radiotherapy(File_number) VALUES ('" + file_number + "')")
    data = radiation(file_number)
    update_multiple(conn, cursor, table, col_list, file_number, data)

def edit_data(conn, cursor, file_number):
    table = "Radiotherapy"
    col_list = names.names_radiation()
    enter = review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = radiation(file_number)
        update_multiple(conn, cursor, table, col_list, file_number, data)
