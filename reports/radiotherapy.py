import modules.ask_y_n_statement as ask
from sql.add_update_sql import review_input, update_multiple, review_data, last_update
import modules.pccm_names as names


def radiation (file_number, user_name):
    check = False
    while not check:
        radio = ask.ask_y_n("Radiotherapy Recieved?")
        if not radio:
            radio = ask.ask_option("Reason for not recieving radiotherapy", ["Not indicated", "Unable to afford",
                                                                                           "Patients reluctance",
                                                                                           "Logistic concerns"])
            radio_date,  radio_type, imrt, radio_tox, radio_delayed_tox, radio_finish, radio_location, radio_onco = ("NA", )*8
        else:
            radio = "Radiation therapy recieved"
            radio_date = ask.check_date("Date of starting radiotherapy: ")
            radio_type = ask.ask_option("Type of radiotherapy", ["Cobalt", "Linear Accelerator based treatment",
                                                                 "Not known", "Other"])
            imrt = ask.ask_y_n_na("Did the patient opt for Intensity Modulated/3Dimensional conformal radiotherapy ("
                                             "IMRT/3DCRT)")
            if imrt == "Yes":
                imrt = "IMRT/3DCRT_yes"
            if imrt == "No":
                imrt = ask.ask_option("Reasons for not opting for IMRT/3DCRT", ["Financial", "Not advised",
                                                                                              "Not known"])
            radio_tox = ask.ask_option("Did radiotherapy related acute toxicity occur?",
                                                     ["Yes", "No","Not known"])
            if radio_tox == "Yes":
                radio_tox = input("Type of toxicity: ")
            radio_delayed_tox = ask.ask_option("Did radiotherapy related delayed toxicity occur?", ["Yes", "No",
                                                                                                        "Not known"])
            radio_finish = ask.check_date("Date of finishing radiotherapy: ")
            radio_location = input("Location of radiotherapy: ")
            radio_onco = ask.ask_list("Name of Radiation Oncologist", ["Dr. Gautam Sharan", "Other"])
        data_list = [radio, radio_date,  radio_type, imrt, radio_tox, radio_delayed_tox, radio_finish, radio_location,
                     radio_onco, user_name, last_update()]
        col_list =names.names_radiation()
        check = review_input(file_number, col_list, data_list)
    return data_list


def add_data(conn, cursor, file_number, user_name):
    table = "radiotherapy"
    col_list = names.names_radiation()
    data = radiation(file_number, user_name)
    update_multiple(conn, cursor, table, col_list, file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "radiotherapy"
    col_list = names.names_radiation()
    enter = review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = radiation(file_number, user_name)
        update_multiple(conn, cursor, table, col_list, file_number, data)
