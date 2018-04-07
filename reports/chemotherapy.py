import modules.ask_y_n_statement as ask_y_n_statement
import tables.chemo as chemo
import pandas as pd
from sql.add_update_sql import review_df, review_input, update_multiple, review_data
from modules.pccm_names import names_chemotherapy as names
from tables.chemo_tables import drug_add

def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Chemotherapy (File_number) VALUES ('" + file_number + "')")

def chemotherapy_regime(file_number):
    col_drug = names("Chemo_Drug_per_week")
    drug_per_week = pd.DataFrame(columns=col_drug)
    col_cycle_all = names("Chemo_Drug_Cycle")
    data_per_cycle = pd.DataFrame(columns=col_cycle_all)
    col_drug_response = names("Chemo_Toxicity")
    tox_response_all = pd.DataFrame(columns=col_drug_response)
    check = False
    while not check:
        chemotherapy = ask_y_n_statement.ask_y_n("Has Chemotherapy been done for the patient?")
        if chemotherapy:
            date_chemotherapy = input("Date of starting Chemotherapy: ")
            plan_chemotherapy = input("Type of Chemo plan: ")
            cycle_number, week_number = (1,)*2
            week_end, cycle_index, week_index,  = (0,)*3
            add_cycle = True
            while add_cycle:
                check_cycle = False
                while not check_cycle:
                    cyc_name = "Cycle " + str(cycle_number)
                    print(cyc_name)
                    week_add = True
                    while week_add:
                        check_drug_tox = False
                        while not check_drug_tox:
                            week = "Week " + str(week_number)
                            print(week)
                            week_check = ask_y_n_statement.ask_y_n("Is week correct?")
                            if not week_check:
                                week_number = input("Week number? ")
                                week_number = int(week_number)
                                week = "Week " + str(week_number)
                            patient_wt = input("Patient weight (in kg): ")
                            drug_per_week, drug_cyc = drug_add(file_number, cyc_name, cycle_number, week, patient_wt, drug_per_week)
                            tox_response = chemo.tox_table(file_number, cyc_name, week, drug_cyc)
                            tox_grade, tox, tox_treatment, tox_response = tox_response
                            change_tox = ask_y_n_statement.ask_option("Changes to Chemo treatment due to toxicity", ["No change", "Chemo regime changed", "Chemo stopped"])
                            if change_tox =="Chemo regime changed":
                                change = input("Please describe changes to Chemo regime: ")
                                change_tox = change_tox+": "+change
                            data_tox_response = [file_number, cycle_number, week, "/".join(drug_cyc), tox, tox_grade, tox_treatment,
                                                 tox_response, change_tox]
                            tox_response_all.loc[week_index] = data_tox_response
                            check_drug_tox = review_df(tox_response_all.loc[week_index])
                            week_number = week_number + 1
                            week_index = week_index + 1
                        week_add = ask_y_n_statement.ask_y_n("Add another week to " + cyc_name + " ?")
                    patient_wt_end_cycle = patient_wt
                    drug_cycle = drug_per_week.query('Cycle_number==' + str(cycle_number))
                    tox_cycle = tox_response_all.query('Cycle_number==' + str(cycle_number))
                    data_cycle, drug_dose = chemo.get_cycle_data(drug_cycle, tox_cycle)
                    drug_week, tox_week, tox_grade_week, tox_treatment_week, tox_response_week, change_tox_week \
                        = data_cycle
                    response_check = ask_y_n_statement.ask_option("Method used to check response to Chemo in this cycle",
                                                                  ["Response not checked", "Other"])
                    if response_check != "Response not checked":
                        response_chemotherapy = ask_y_n_statement.ask_option("Tumour response to Chemo treatment",
                                                                     ["Partial", "Complete", "Progressing", "Static", "Other"])
                        response_size = input("Tumour Size as assessed by " + response_check+" (cm): ")
                        date = input("Date of tumour size assessment: ")
                    else:
                        response_chemotherapy, response_size, date  = ("NA", )*3
                    week_end = week_number - week_end -1
                    weeks = str(week_end)+" Weeks"
                    data_cycle_all = [file_number, cyc_name, weeks, patient_wt_end_cycle, drug_week, tox_week, tox_grade_week,
                                      tox_treatment_week, tox_response_week, change_tox_week, drug_dose, response_check,
                                      response_chemotherapy, response_size, date]
                    data_per_cycle.loc[cycle_index] = data_cycle_all
                    check_cycle = review_df(data_per_cycle.loc[cycle_index])
                    cycle_number = cycle_number + 1
                    cycle_index = cycle_index + 1
                add_cycle = ask_y_n_statement.ask_y_n("Add another cycle? ")
            trast_chemotherapy = ask_y_n_statement.ask_y_n("Trastuzumab used?")
            if trast_chemotherapy:
                trast_regime = ask_y_n_statement.ask_option("Trastuzumab use was", ["Sequential", "Concurrent"])
                trast_chemotherapy = "Trastuzumab used"
                trast_courses = input("Number of courses of trastuzumab/herceptin taken: ")
            else:
                trast_chemotherapy = "Trastuzumab not used"
                trast_regime, trast_courses = ("NA",)*2

            date_complete = input("Date of completion of Chemo: ")
            complete_chemotherapy = ask_y_n_statement.ask_y_n("Was Chemo completed as per schedule?")
            if complete_chemotherapy:
                reason_incomplete = "Chemo completed as per schedule"
            else:
                reason_incomplete = ask_y_n_statement.ask_option("Reason for discontinuation", ["Toxicity",
                "Reluctance of patient", "Progression on chemotherapy", "Advised by treating doctor",
                "Death due to toxicity", "Death due to progressive disease", "Preferred treatment at another centre",
                "Death due to unrelated cause", "Patient was unable to afford treatment"])
                reason_incomplete = "Chemo incomplete: "+reason_incomplete
            menopause = ask_y_n_statement.ask_option("Menopausal Status", ["Pre-menopausal", "Peri-menopausal",
                                                                           "Post-Menopausal", "Other"])
            if menopause == "Pre-menopausal":
                ovary_status = ask_y_n_statement.ask_option("Status of ovarian function after Chemo",
                               ["Menses ongoing", "Amenorrhoea on Chemo", "Amenorrhoea post Chemo"])
            else:
                ovary_status = "Not Pre-Menopausal"
            number_cycles = data_per_cycle.shape[0]
            number_weeks = week_number -1
            drug_dose = []
            drug_dose_unit_df = drug_per_week.loc[:,("Drugs", "Dose_unit")].drop_duplicates()
            for index in range(1, 2):
                dose_ = drug_per_week.loc[:, ("Drugs", "Dose")]
                dose_sum_cycle = dose_.groupby("Drugs").sum()
            for index in range(0, len(list(dose_sum_cycle.index))):
                dose_unit_ = list(drug_dose_unit_df.loc[:, "Dose_unit"])[index]
                data = list(dose_sum_cycle.index)[index] + ": " + str(
                    list(dose_sum_cycle.loc[:, "Dose"])[index]) + " " + dose_unit_
                drug_dose.append(data)
            drug_admin = "; ".join(drug_dose)
            hormone_therapy = ask_y_n_statement.ask_y_n("Was hormone therapy given?")
            if hormone_therapy:
                hormone_therapy = "Hormone therapy given"
                therapy_type = ask_y_n_statement.ask_option("Hormone therapy type", ["Sequential", "Concurrent"])
                therapy_duration = input("What was the duration of therapy? ")
                therapy_side = ask_y_n_statement.ask_y_n("Were any side effects observed ?")
                if therapy_side:
                    therapy_side = input("Please give details of side effects observed: ")
                else:
                    therapy_side = "NA"
            else:
                hormone_therapy = "No hormone therapy given"
                therapy_type, therapy_duration, therapy_side = ("NA", )*3
            chemotherapy = "Neo Adjuvant therapy given"
        else:
            chemotherapy = "No NeoAdjuvant Therapy given"
            date_chemotherapy, plan_chemotherapy, drug_admin, number_weeks, number_cycles, response_check, response_chemotherapy, response_size, \
            date, ovary_status, reason_incomplete, date_complete, trast_chemotherapy, trast_regime, trast_courses, \
            hormone_therapy, therapy_type, therapy_duration, therapy_side = ("NA",)*19
        data_list = [chemotherapy, date_chemotherapy, plan_chemotherapy, drug_admin,str(number_weeks), str(number_cycles),
                     response_check, response_chemotherapy, response_size, date, ovary_status, reason_incomplete, date_complete,
                     trast_chemotherapy, trast_regime, trast_courses, hormone_therapy, therapy_type, therapy_duration, therapy_side]
        col_list = names("Chemotherapy")
        check = review_input(file_number, col_list, data_list)
    return data_list,  tox_response_all, drug_per_week, data_per_cycle

def add_data(conn, cursor, file_number):
    file_row(cursor, file_number)
    data = chemotherapy_regime(file_number)
    data_sql, tox_response_all, drug_per_week, data_per_cycle = data
    update_multiple(conn, cursor, "Chemotherapy", names("Chemotherapy"), file_number, data_sql)
    tox_response_all.to_sql("Chemo_Toxicity", conn, index=False, if_exists="append")
    drug_per_week.to_sql("Chemo_Drug_per_week", conn, index=False, if_exists="append")
    data_per_cycle.to_sql("Chemo_Drug_Cycle", conn, index=False, if_exists="append")


def edit_data(conn, cursor, file_number):
    table = "Chemotherapy"
    enter = review_data(conn, cursor, table, file_number, names(table))
    if enter:
        data = chemotherapy_regime(file_number)
        data_sql, tox_response_all, drug_per_week, data_per_cycle = data
        update_multiple(conn, cursor, table, names(table), file_number, data_sql)
        tox_response_all.to_sql("Chemo_Toxicity", conn, index=False, if_exists="append")
        drug_per_week.to_sql("Chemo_Drug_per_week", conn, index=False, if_exists="append")
        data_per_cycle.to_sql("Chemo_Drug_Cycle", conn, index=False, if_exists="append")
