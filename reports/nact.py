import modules.ask_y_n_statement as ask_y_n_statement
import pandas as pd
from sql.add_update_sql import review_df, review_input, update_multiple, review_data, delete_rows
from modules.pccm_names import names_nact as names
from additional_tables.chemo_tables import drug_table_enter, tox_table
from datetime import datetime



def nact_test(file_number, user_name):
    col_drug = names("NACT_Drug_Table")
    drug_table = pd.DataFrame(columns=col_drug)
    col_tox = names('NACT_Tox_table')
    toxicity = pd.DataFrame(columns =col_tox)
    check = False
    while not check:
        nact = ask_y_n_statement.ask_y_n_na("Has neo adjuvant therapy been done for the patient?")
        if nact == 'Yes':
            place_nact = ask_y_n_statement.ask_y_n_na("Has neo adjuvant therapy been done at PCCM?", "At PCCM", "Outside",
                                                      "Not Certain, requires follow-up")
            details_nact = ask_y_n_statement.ask_y_n("Are neo adjuvant therapy details available?", "Details Available",
                                                     "Follow-up required")
            nact = "NACT given"
            if details_nact == "Follow-up required":
                plan_nact, date_start_nact, patient_wt, cyc_number, drug_cyc, drug_doses, drug_units, drug_freq,tox_type, \
                tox_grade, tox_treat, tox_response, tox_cycle, change_tox,nact_response_by, nact_response, nact_size, nact_size_unit, \
                nact_size_date, trast_nact, trast_regime, trast_courses,date_complete, reason_incomplete, \
                hormone_therapy,  therapy_type, therapy_duration, therapy_side = (details_nact,)*28
            elif details_nact == "Details Available":
                plan_nact = input("What is the plan of NACT (for eg., 4 cycles AC followed by 12 cycles Paclitaxel):")
                date_start_nact = ask_y_n_statement.check_date("Date of starting neo-adjuvant therapy: ")
                patient_wt = input("Weight of patient at start of therapy (in kgs): ")
                check_wt = ask_y_n_statement.ask_y_n("Is weight at any other time point mentioned in report "
                                                         "(with date, if given)?")
                while check_wt:
                    other_wt = input("Time point at which weight mentioned: ")
                    other_wt = other_wt + " "+ input("Weight of patient at "+other_wt+": ")
                    patient_wt = patient_wt + "; "+other_wt
                    check_wt = ask_y_n_statement.ask_y_n("Is weight at any other time point mentioned in report "
                                                         "(with date, if given)?")
                drug_admin = drug_table_enter(file_number, drug_table)
                data_drug = ['Number_cycle','Drug', 'Drug_dose', 'Dose_unit', 'Cycle_frequency_per_week']
                data_drug_list = []
                for index in data_drug:
                    data_drug = "; ".join(list(drug_admin.loc[:,index]))
                    data_drug_list.append(data_drug)
                cyc_number, drug_cyc, drug_doses, drug_units, drug_freq = data_drug_list
                check_drug_tox = False
                while not check_drug_tox:
                    toxicity = tox_table(file_number, drug_cyc, toxicity)
                    check_drug_tox = review_df(toxicity)
                columns = col_tox
                tox_details = []
                for column in columns:
                    tox_detail = toxicity.loc[:,column].drop_duplicates()
                    tox_details.append(list(tox_detail))
                tox_details = ask_y_n_statement.join_lists(tox_details, "; ")
                file_number_tox, drug_tox, tox_type, tox_grade, tox_treat, tox_response, tox_cycle, change_tox = tox_details
                nact_response_by = ask_y_n_statement.ask_option("Response to NACT measured by",['Mammography', 'SonoMammography'])
                nact_response = ask_y_n_statement.ask_option("Response of tumour",
                                                             ["Partial", "Complete", "No Effect", "Other"])
                nact_size = input("Tumour size (without unit, e.g., 2 x 4 x 5) after treatment: ")
                nact_size_unit = ask_y_n_statement.ask_option("Tumour size unit", ['mm', 'cm'])
                nact_size_date=ask_y_n_statement.check_date("Date tumour size checked: ")
                trast_nact = ask_y_n_statement.ask_y_n("Trastuzumab used?")
                if trast_nact:
                    trast_regime = ask_y_n_statement.ask_option("Trastuzumab use was", ["Sequential", "Concurrent"])
                    trast_nact = "Trastuzumab used"
                    trast_courses = input("Number of courses of trastuzumab/herceptin taken: ")
                else:
                    trast_nact, trast_regime, trast_courses, therapy_side = ("Trastuzumab not used", )*4
                date_complete = ask_y_n_statement.check_date("Date of completion of NACT: ")
                complete_nact = ask_y_n_statement.ask_y_n("Was NACT completed as per schedule? ")
                if complete_nact:
                    reason_incomplete = "NACT completed as per schedule"
                else:
                    reason_incomplete = ask_y_n_statement.ask_option("Reason for discontinuation", ["Toxicity",
                    "Reluctance of patient", "Progression on chemotherapy", "Advised by treating doctor",
                    "Death due to toxicity", "Death due to progressive disease", "Preferred treatment at another centre",
                    "Death due to unrelated cause", "Patient was unable to afford treatment"])
                    reason_incomplete = "NACT incomplete: "+reason_incomplete
                hormone_therapy = ask_y_n_statement.ask_y_n_na("Was hormone therapy given?")
                if hormone_therapy == 'Yes':
                    hormone_therapy = "Hormone therapy given"
                    therapy_type = ask_y_n_statement.ask_option("Hormone therapy type", ["Sequential", "Concurrent"])
                    therapy_duration = input("What was the duration of therapy? ")
                    therapy_side = ask_y_n_statement.ask_y_n_na("Were any side effects observed ?")
                    if therapy_side == 'Yes':
                        therapy_side = input("Please give details of side effects observed: ")
                elif hormone_therapy == 'No':
                    hormone_therapy = "No hormone therapy given"
                    therapy_type, therapy_duration, therapy_side = (hormone_therapy,) * 3
                else:
                    therapy_type, therapy_duration, therapy_side = (hormone_therapy, )*3
            else:
                plan_nact, date_start_nact, cyc_number, drug_cyc, drug_doses, drug_units, drug_freq,tox_type, tox_grade, \
                tox_treat, tox_response, tox_cycle, change_tox,nact_response_by, nact_response, nact_size, nact_size_unit, \
                nact_size_date, trast_nact, trast_regime, trast_courses, hormone_therapy,  therapy_type, \
                therapy_duration, therapy_side, date_complete, reason_incomplete, patient_wt = (details_nact,)*27
        elif nact == 'No':
            place_nact, plan_nact, date_start_nact, cyc_number, drug_cyc, drug_doses, drug_units, drug_freq,tox_type, tox_grade, \
            tox_treat, tox_response, tox_cycle, change_tox, nact_response_by, nact_response, nact_size, nact_size_unit, nact_size_date, \
            trast_nact, trast_regime, trast_courses, hormone_therapy,  therapy_type, therapy_duration, therapy_side,\
            date_complete, reason_incomplete, details_nact, nact, patient_wt = ("NACT not given",)*31
        else:
            place_nact, plan_nact, date_start_nact, cyc_number, drug_cyc, drug_doses, drug_units,  drug_freq, tox_type, tox_grade, \
            tox_treat, tox_response, tox_cycle, change_tox, nact_response_by, nact_response, nact_size, nact_size_unit, nact_size_date, \
            trast_nact, trast_regime, trast_courses, hormone_therapy,  therapy_type, therapy_duration,\
            therapy_side, date_complete, reason_incomplete, details_nact, patient_wt = (nact,)*30
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [nact,  place_nact,  details_nact,  plan_nact,  date_start_nact, patient_wt, drug_cyc,  cyc_number,
                     drug_freq, drug_doses,  drug_units, tox_type, tox_grade, tox_treat, tox_response, tox_cycle,  change_tox,
                     nact_response_by,  nact_response, nact_size, nact_size_unit, nact_size_date,  reason_incomplete,  date_complete,
                     trast_nact, trast_regime,  trast_courses,  hormone_therapy,   therapy_type,  therapy_duration,
                     therapy_side,  user_name,  last_update]
        col_list = names("Neo_Adjuvant_Therapy")
        check = review_input(file_number, col_list, data_list)
    return data_list, drug_table, toxicity

def clip_information(file_number):
    check = False
    while not check:
        clip = ask_y_n_statement.ask_y_n("Was Clip inserted for surgery?")
        if clip:
            clip_number = input("Number of clips inserted: ")
            clip_date = ask_y_n_statement.check_date("Date of clip insertion: ")
            clip_cycle = input("Clip inserted after cycle? ")
        else:
            clip_date, clip_number, clip_cycle = ("NA", )*3
        data_list = clip_number, clip_date, clip_cycle
        col_list = names("clip_information")
        check = review_input(file_number, col_list, data_list)
    return data_list

def add_data(conn, cursor, file_number, user_name):
    table = "Neo_Adjuvant_Therapy"
    data = nact_test(file_number, user_name)
    data_sql, drug_table, tox_response = data
    update_multiple(conn, cursor, table, names(table), file_number, data_sql)
    drug_table.to_sql("NACT_Drug_Table", conn, index=False, if_exists="append")
    tox_response.to_sql("NACT_Tox_table", conn, index=False, if_exists="append")
    enter = ask_y_n_statement.ask_y_n("Input Clip Information")
    if enter:
        data = clip_information(file_number)
        col_list = names("clip_information")
        update_multiple(conn, cursor, table, col_list, file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "Neo_Adjuvant_Therapy"
    enter = review_data(conn, cursor, table, file_number, names(table))
    if enter:
        delete_rows(cursor, 'NACT_Drug_Table', "File_number", file_number)
        delete_rows(cursor, 'NACT_Tox_table', "File_number", file_number)

        data = nact_test(file_number, user_name)
        data_sql, drug_table, tox_response = data

        update_multiple(conn, cursor, table, names(table), file_number, data_sql)
        drug_table.to_sql("NACT_Drug_Table", conn, index=False, if_exists="append")
        tox_response.to_sql("NACT_Tox_table", conn, index=False, if_exists="append")

    print("Clip Information")
    module = "clip_information"
    col_list = names(module)
    enter = review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = clip_information(file_number)
        update_multiple(conn, cursor, table, col_list, file_number, data)