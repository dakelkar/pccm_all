def drug_add(file_number, cyc_name, cycle_number, week, patient_wt, drug_per_week):
    import modules.ask_y_n_statement as ask
    from sql.add_update_sql import review_df as review
    import tables.chemo as chemo
    drug_index = 0
    drug_add = True
    drug_cyc = []
    while drug_add:
        check_drug= False
        while not check_drug:
            drug_index = drug_index + 1
            drug = ask.ask_option("Drug used for NACT " + cyc_name, chemo.drug_list())
            dose = input("Dose of " + drug + " in " + cyc_name + ": ")
            dose_unit = input("Dose unit: ")
            cyc_freq = input("Cycle Frequency: ")
            data_week = [file_number, cycle_number, week, patient_wt, drug, float(dose), dose_unit, cyc_freq]
            drug_per_week.loc[drug_index] = data_week
            check_drug = review(drug_per_week.loc[drug_index])
            drug_cyc.append(drug)
            drug_index = drug_index + 1
        drug_add = ask.ask_y_n("Add another drug")
    return drug_per_week, drug_cyc
