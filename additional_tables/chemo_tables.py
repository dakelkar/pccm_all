import modules.ask_y_n_statement as ask_y_n_statement
import pandas as pd
import modules.pccm_names as names
from sql.add_update_sql import review_df_row, review_df
from additional_tables import chemo

def tox_table (file_number, drug_cyc, tox_all):
    tox_index = 0
    check_tox = False
    while not check_tox:
        tox = ask_y_n_statement.ask_y_n("Were there any toxic effects in  administration of " + drug_cyc)
        if tox:
                add_tox = True
                while add_tox:
                    tox_present = ask_y_n_statement.ask_option("Toxic effects of type", chemo.toxicity())
                    tox_grade = ask_y_n_statement.ask_option(("the grade of "+tox_present+ "? "),
                                ["Mild", "Moderate", "Severe", "Other"])
                    treatment = input(
                        "Treatment given for " + tox_grade + " " + tox_present + " (include all details): ")
                    resp_treatment = ask_y_n_statement.ask_option(
                        ("Response to treatment given for " + tox_grade + " " + tox_present),
                        ["Partial", "Complete", "No Effect", "Other"])
                    cyc_tox = input("Cycle at which toxicity occurred: ")
                    change_tox = ask_y_n_statement.ask_option("Changes to treatment",
                                                              ["No change",
                                                               "Therapy changed due to toxicity",
                                                               "Therapy stopped  due to toxicity",
                                                               "Therapy changed due to other reasons",
                                                               "Therapy stopped due to other reasons"])
                    if change_tox == "Therapy changed due to toxicity" or change_tox == "Therapy changed due to other reasons":
                        change = input("Please describe changes to Therapy: ")
                        change_tox = change_tox + ": " + change
                    check = False
                    while not check:
                        data = [file_number, drug_cyc, tox_present,tox_grade, treatment, resp_treatment, cyc_tox, change_tox]
                        tox_all.loc[tox_index] = data
                        check = review_df_row(tox_all)
                    tox_index = tox_index + 1
                    add_tox = ask_y_n_statement.ask_y_n('Add another toxicity type?')
        else:
            tox_present, tox_grade,treatment, resp_treatment, cyc_tox, change_tox = ("No Toxicity", )*6
            data = [file_number, drug_cyc, tox_present, tox_grade, treatment, resp_treatment, cyc_tox, change_tox]
            tox_all.loc[tox_index] = data
        check_tox = review_df(tox_all)
    return tox_all

def drug_table_enter(file_number, drug_table):
    drug_add = True
    drug_index = 0
    while drug_add:
        check_drug= False
        while not check_drug:
            drug = ask_y_n_statement.ask_option("Drug used for therapy", chemo.drug_list())
            try:
                dose = input("Dose of " + drug  +" (actual dose ammount without unit, numbers only): ")
                dose_x = float(dose)
            except:
                print ('ERROR: enter numbers only')
                dose = input("Dose of " + drug  +" (actual dose ammount without unit, numbers only): ")
            dose_unit = input("Dose unit: ")
            cyc_freq_week = input("Cycle Frequency (frequency per week, so three weekly is 3 and weekly is 1): ")
            try:
                number_cycle = input("Number of cycles actually given: ")
                dose_x = int(number_cycle)
            except:
                print('ERROR: enter numbers only')
                number_cycle = input("Number of cycles actually given: ")
            try:
                drug_dose = float(dose) * int(number_cycle)
            except:
                drug_dose = 'PLEASE RE-ENTER DATA, DOSE AND NUMBER OF CYCLES MUST BE DIGITS ONLY'
            data_drug = [file_number, number_cycle, drug, str(drug_dose), dose_unit, cyc_freq_week]
            drug_table.loc[drug_index] = data_drug
            check_drug, drug_table = review_df_row(drug_table)
            drug_index = drug_index + 1
        drug_add = ask_y_n_statement.ask_y_n("Add another drug")
    return drug_table

def hormone_therapy_chemo():
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
    return  hormone_therapy, therapy_type, therapy_duration, therapy_side