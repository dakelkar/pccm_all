def nact_regime(file_number):
    import modules.ask_y_n_statement as ask_y_n_statement
    import sql.add_update_sql as add_update_sql
    import modules.pccm_names as pccm_names
    import tables.chemo as chemo
    import pandas as pd
    table = "NACT_Drug_Regimen"
    cyc_drug = []
    check = False
    col_list_tox = "File_number", "Week","Cycle_name", "Toxicity_type", "Toxicity_grade", "Treatment", "Response_Treatment"
    tox_all = pd.DataFrame(columns=col_list_tox)
    col_drug = "File_number","Cycle_number", "Week", "Patient_wt_kg", "Drugs", "Dose", "Dose_unit", "Cycle_frequency"
    drug_per_cyc = pd.DataFrame(columns=col_drug)
    col_response = "File_number","Cycle_number", "Response_check", "Response_nact"
    col_drug_response = "File_number", "Cycle_number", "Week", "Drug", "Toxicity", "Toxicity_Grade", "Toxicity_Response", "Toxicity_Treatment"
    data_tox_response_all = pd.DataFrame(columns=col_drug_response)
    response_all = pd.DataFrame(columns=col_response)
    col_data_cycle_weekly = ["Week_number", "Patient Weight", "Drug", "Toxicity_type", "Toxicity_grade", "Treatment", "Response_Treatment"]
    data_cycle_weekly = pd.DataFrame(columns=col_data_cycle_weekly)
    while not check:
        nact = ask_y_n_statement.ask_y_n("Has neo adjuvant therapy been done for the patient?")
        if nact:
            date_nact = input ("Date of starting neo-adjuvant therapy: ")
            plan_nact = input ("Type of NACT plan: ")
            combo_nact, dose_nact = [list([]) for _ in range(2)]
            cycle_drug_response = []
            cycle_number = 0
            week_number = 0
            drug_cycle = True
            tox_response_list = []
            data_cycle_weekly = []
            while drug_cycle:
                cycle_number = cycle_number+1
                cyc_name = "Cycle " + str(cycle_number)
                print(cyc_name)
                week_add = True
                while week_add:
                    week_number = week_number +1
                    week = "Week "+str(week_number)
                    print (week)
                    week_check = ask_y_n_statement.ask_y_n("Is week correct?")
                    if not week_check:
                        week = "Week"+input("Week number? ")
                    patient_wt = input("Patient weight (in kg): ")
                    drug_add = True
                    drug_cyc, dose_cyc, dose_unit_cyc, cyc_freq_drug = [list([])for _ in range(4)]
                    while drug_add:
                        drug = ask_y_n_statement.ask_option("Drug used for NACT "+ cyc_name, chemo.drug_list())
                        dose = input("Dose of "+drug+ " in "+cyc_name+": ")
                        dose_unit = input("Dose unit: ")
                        cyc_freq= input("Cycle Frequency: ")
                        drug_cyc.append(drug)
                        dose_unit_cyc.append(dose_unit)
                        cyc_freq_drug.append(cyc_freq)
                        data_cycle = [file_number, cycle_number, week, float(patient_wt), drug, float(dose), dose_unit, cyc_freq]
                        drug_this_cyc = pd.DataFrame([data_cycle], columns=col_drug)
                        drug_per_cyc = drug_per_cyc.append(drug_this_cyc)
                        drug_add = ask_y_n_statement.ask_y_n("Add another drug")
                    tox_response, tox_data = tox_table(file_number, cyc_name, week, drug_cyc)
                    tox_all = tox_all.append(tox_data)
                    tox_response_list.append(tox_response)
                    #tox_data.to_sql(table, conn, index=False, if_exists="append")
                    tox_week =[]
                    for index in range(len(tox_response)):
                        week_data = week + ": " + tox_response[index]
                        tox_week.append(week_data)
                    week_drug = week + ": " + "/".join(drug_cyc)
                    week_weight = week + ": " + "/".join(patient_wt)
                    data = [week_number, week_weight, week_drug]
                    week_data = pd.DataFrame([data], columns= ["Week_number", "Patient Weight","Drug"])
                    week_tox = pd.DataFrame([tox_week], columns=["Toxicity_type", "Toxicity_grade", "Treatment", "Response_Treatment"])
                    data_week = pd.concat([week_data.reset_index(drop=True), week_tox], axis=1)
                    data_cycle_weekly.append(data_week)
                    tox_grade, tox, tox_treatment, tox_response = tox_response
                    data_tox_response = [file_number, cycle_number, week, "/".join(drug_cyc), tox, tox_grade, tox_treatment, tox_response]
                    data_tox_response_df = pd.DataFrame([data_tox_response], columns = col_drug_response)
                    data_tox_response_all = data_tox_response_all.append(data_tox_response_df)
                    week_add = ask_y_n_statement.ask_y_n("Add another week to "+cyc_name+" ?")
                data_cycle = ask_y_n_statement.join_lists(data_cycle, "|")
                response_check = ask_y_n_statement.ask_option("Method used to check response to NACT in this cycle", ["Response not checked", "Other"])
                if response_check != "Response not checked":
                    response_nact = ask_y_n_statement.ask_option("Response to NACT treatment",
                                                                 ["Partial", "Complete", "Progressing", "Static", "Other"])
                    data = [file_number, cycle_number, response_check, response_nact]
                    response_df = pd.DataFrame([data], columns = col_response)
                    response_all = response_all.append(response_df)
                    data_cycle = data_cycle, [response_check], [response_nact]
                else:
                    response_nact = "NA"
                    data = [file_number, cycle_number, response_check, response_nact]
                    response_df = pd.DataFrame([data], columns=col_response)
                    response_all = response_all.append(response_df)
                drug_cycle = ask_y_n_statement.ask_y_n ("Add another cycle? ")
        check = True
                # extract drug_cycle from unique drug column of drug_per_cyc and add; add cycle size end wek of cycle 1; add dose up per cycle.
                #table of cycle/weeks per cycle/drugs per cycle/patient wt/???
                #add
                # drug_per_cyc.to_sql(table = "??", conn, index=False, if_exists="append")

    return response_all, tox_all, drug_per_cyc, data_tox_response_all
def add_data(conn, tox_all):
    import pandas
    for_tox_table = tox_all[
        ["File_number", "Week", "Cycle_name", "Toxicity_type", "Toxicity_grade", "Treatment", "Response_Treatment"]]
    table = "NACT_Toxicity"
    for_tox_table.to_sql(table, conn, index=False, if_exists="append")
                #cycle_data_lists = [drug_cyc, dose_cyc, dose_unit_cyc, cyc_freq_drug]
                #cycle_data_lists = tuple(ask_y_n_statement.join_lists(cycle_data_lists, "; "))
                #drug, dose, dose_unit, cyc_freq = cycle_data_lists
                #tox_grade, tox, tox_treatment, tox_response = tox_table(conn, cursor, file_number, cyc_name)
                #response_check = ask_y_n_statement.ask_option("Method used to check response to NACT in this cycle", ["Response not checked", "Other"])
                #response_nact = ask_y_n_statement.ask_option("Response to NACT treatment",
                #                                             ["Partial", "Complete", "Progressing", "Static", "Other"])
                #data_response = [response_check, response_nact]
                #response_cyc = pd.DataFrame([data_response], columns=col_drug[6:8])
                #drug_per_cyc = drug_per_cyc.append(response_cyc)
                #data_list = [file_number, cyc_name, week, patient_wt, drug, dose, dose_unit, cyc_freq, tox, tox_grade, tox_treatment, tox_response, response_check, response_nact]
                #col_list = pccm_names.names_nact(table)
                #check = add_update_sql.review_input(file_number, col_list, data_list)
                #add_update_sql.insert(conn, cursor, table, ", ".join(col_list), tuple(data_list))
                #cycle_number = cycle_number + 1
                #drug_cycle = ask_y_n_statement.ask_y_n("Add another cycle?")
                #trast_nact = ask_y_n_statement.ask_y_n("Trastuzumab used")
                #if trast_nact:
                #    trast_regime = ask_y_n_statement.ask_option("Trastuzumab use was", ["Sequential", "Concurrent"])
                #    trast_nact = "Trastuzumab used: "+trast_regime
                #else:
                #    trast_nact = "Trastuzumab not used"
                #course_nact = input("Number of cycles of NACT given: ")


def tox_table (file_number, cyc_name, week, drug_cyc):
    import modules.ask_y_n_statement as ask_y_n_statement
    import tables.chemo as chemo
    import pandas as pd
    col_list =  ["File_number", "Week","Cycle_name","Drug_Administered", "Toxicity_type", "Toxicity_grade", "Treatment", "Response_Treatment"]
    tox_data = pd.DataFrame(columns = col_list)
    drugs = "/".join(drug_cyc)
    tox = ask_y_n_statement.ask_y_n("Were there any toxic effects in  " + week + " of "+cyc_name)
    tox_grade_list, tox_list, tox_treatment, resp_treatment_list = [list([]) for _ in range(4)]
    if tox:
        for index in chemo.toxicity():
            tox_grade = ask_y_n_statement.ask_option(("the grade of "+index+" in "+cyc_name +"? "),
                        ["Mild", "Moderate", "Severe", "Not Present", "Other"])
            if tox_grade not in {"Not Present"}:
                treatment = input("Treatment given for "+ tox_grade +" "+index)
                resp_treatment = ask_y_n_statement.ask_option(("Response to treatment given for " + tox_grade + " "
                                + index), ["Partial", "Complete", "Progressing", "Static", "Other"])
                tox_grade_list.append(tox_grade)
                tox_list.append(index)
                tox_treatment.append(treatment)
                resp_treatment_list.append(resp_treatment)
                data = [file_number, week, cyc_name, drugs, index, tox_grade, treatment, resp_treatment]
                tox_this = pd.DataFrame([data], columns=col_list)
                tox_data = tox_data.append(tox_this)
    else:
        tox_grade, tox, treatment, resp_treatment = ("NA", )*4
        tox_grade_list, tox_list, tox_treatment, resp_treatment_list = [["NA"]]*4
        data = [file_number, week, cyc_name, drugs, "No toxicity", tox_grade, treatment, resp_treatment]
        tox_this = pd.DataFrame([data], columns=col_list)
        tox_data = tox_data.append(tox_this)
    all_data = [tox_grade_list, tox_list, tox_treatment, resp_treatment_list]
    response = ask_y_n_statement.join_lists(all_data, "; ")
    return response, tox_data
