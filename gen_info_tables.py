def nut_supplements(conn, cursor, file_number, table):
    from add_update_sql import update_multiple, review_input
    from breast_cancer_tables import nut_supp_table
    from ask_y_n_statement import ask_y_n
    check = False
    while not check:
        nut_supplements = ask_y_n("Nutritional supplements taken")
        if nut_supplements:
            nuts = nut_supp_table(conn, cursor, file_number)
            nut_supplements = "Nutritional supplements taken"
        else:
            nut_supplements = "No nutritional supplements taken"
            nuts = ("NA",) * 3
        nuts_type, nuts_quant, nuts_dur = nuts
        data_list = [nut_supplements, nuts_type, nuts_quant, nuts_dur]
        columns_list = ["Nutritional_supplements_y_n", "Type_Nutritional_supplements",
                        "Quantity_Nutritional_supplements", \
                        "Duration_Nutritional_supplements"]
        check = review_input(file_number, columns_list, data_list)
    data = nut_supplements, nuts_type, nuts_quant, nuts_dur
    columns = "Nutritional_supplements_y_n", "Type_Nutritional_supplements", "Quantity_Nutritional_supplements", \
              "Duration_Nutritional_supplements"
    update_multiple(conn, cursor, table, columns, file_number, data)


def phys_act(conn, cursor, file_number, table):
    from breast_cancer_tables import physical_activity_table
    from add_update_sql import update_multiple, review_input
    from ask_y_n_statement import ask_y_n
    check = False
    while not check:
        phys_act = ask_y_n("Any Physical Activities ?")
        if phys_act:
            phys = physical_activity_table(conn, cursor, file_number)
            phys_act = "Physical Activities Performed"
            phys_act_done, phys_act_freq = phys
        else:
            phys_act = "No Physical Activities"
            phys_act_done, phys_act_freq = ("NA",) * 2
        data_list = [phys_act, phys_act_done, phys_act_freq]
        columns_list = ["Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"]
        check = review_input(file_number, columns_list, data_list)
    data = phys_act, phys_act_done, phys_act_freq
    columns = "Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"
    update_multiple(conn, cursor, table, columns, file_number, data)


def med_history(conn, cursor, file_number, table):
    from breast_cancer_tables import med_history_table
    from ask_y_n_statement import ask_y_n
    from add_update_sql import update_multiple, review_input
    check = False
    while not check:
        medical_history_y_n = ask_y_n("Other Medical History ?")
        if medical_history_y_n:
            med_hist = med_history_table(conn, cursor, file_number)
            medical_history_y_n = "Previous medical history present"
        else:
            medical_history_y_n = "No previous medical history present"
            med_hist = ("NA",) * 3
        condition_hist, diagnosis_date_hist, treatment_hist = med_hist
        data_list = [medical_history_y_n, condition_hist, diagnosis_date_hist, treatment_hist]
        columns_list = ["Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History",
                        "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History"]
        check = review_input(file_number, columns_list, data_list)
    data = medical_history_y_n, condition_hist, diagnosis_date_hist, treatment_hist
    columns = "Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History", "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History"
    update_multiple(conn, cursor, table, columns, file_number, data)


def cancer_history(conn, cursor, file_number, table):
    from breast_cancer_tables import cancer_table
    from add_update_sql import update_multiple, review_input
    from ask_y_n_statement import ask_y_n
    check = False
    while not check:
        previous_cancer_history_y_n = ask_y_n("Previous history of cancer ?")
        if previous_cancer_history_y_n:
            previous_cancer = cancer_table(conn, cursor, file_number)
            previous_cancer_history_y_n = "Previous history of cancer"
        else:
            previous_cancer_history_y_n = "No previous history of cancer"
            previous_cancer = ("NA",) * 5
        type_of_cancer_list, year_diagnosis_list, treat_all, type_all, duration_all = previous_cancer
        data_list = [previous_cancer_history_y_n, type_of_cancer_list, year_diagnosis_list, treat_all, type_all, duration_all]
        columns_list = ["Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer", \
                        "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer",
                        "Treatment_Duration_Previous_Cancer"]
        check = review_input(file_number, columns_list, data_list)
    data = previous_cancer_history_y_n, type_of_cancer_list, year_diagnosis_list, treat_all, type_all, duration_all
    columns = "Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer", \
              "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer", "Treatment_Duration_Previous_Cancer"
    update_multiple(conn, cursor, table, columns, file_number, data)


def family_details(conn, cursor, file_number, table):
    from add_update_sql import update_multiple, review_input
    from ask_y_n_statement import ask_y_n
    check = False
    while not check:
        marital_status = input('Marital_Status :')
        siblings = ask_y_n('Siblings')
        if siblings:
            siblings_number = input("Number of siblings: ")
            sisters = input('Sisters :')
            brothers = input('Brothers :')
        else:
            siblings_number, sisters, brothers = "No Siblings", "0", "0"
        children_y_n = ask_y_n('Children')
        if children_y_n:
            children_number = input("Number of children: ")
            daughters = input('Daughters :')
            sons = input('Sons :')
        else:
            children_number, daughters, sons = "No Children", "0", "0"
        columns_list = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"]
        data_list = [marital_status, siblings_number, sisters, brothers, children_number, daughters, sons]
        check = review_input(file_number, columns_list, data_list)
    columns = "Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"
    new_data = marital_status, siblings_number, sisters, brothers, children_number, daughters, sons
    update_multiple(conn, cursor, table, columns, file_number, new_data)


def repro_details(conn, cursor, file_number, table):
    from add_update_sql import update_multiple, review_input
    from breast_cancer_tables import feed_duration
    from ask_y_n_statement import ask_option, ask_y_n
    check = False
    while not check:
        menarche = input('Age at menarche (yrs): ')
        category = "Menopausal Status"
        options = ["Pre-menopausal", "Peri-menopausal", "Post-Menopausal", "Other"]
        menopause = ask_option(category, options)
        menopause_age = menopause
        if menopause == "Post-Menopausal":
            menopause_age = input('Age at menopause (yrs): ')
            lmp = "Last menstrual period " + menopause_age + " yrs"
            period_type = "NA"
        else:
            lmp = input("Date of last menstrual period: ")
            category = "Type of Period"
            options = ["Regular", "Irregular", "Other"]
            period_type = ask_option(category, options)
        number_pregnancy = input("Number of pregnancies: ")
        number_term = input("Pregnancy carried to term (include abortion after 6 months): )")
        number_abortion = input("Number of abortions: ")
        sql = ('SELECT Children FROM Patient_Information_History WHERE File_number = \'' + file_number + "'")
        cursor.execute(sql)
        kids = cursor.fetchall()
        children_number = kids[0][0]
        sql = ('SELECT Age_yrs FROM Patient_Information_History WHERE File_number = \'' + file_number + "'")
        cursor.execute(sql)
        age = cursor.fetchall()
        age_mother = age[0][0]
        if children_number == 'No Children':
            age_first, age_last = ('NA',) * 2
        else:
            age_first = input("Age of first child: ")
            if int(children_number) > 1:
                age_last = input("Age of last child: ")
            else:
                age_last = age_first
        age_first_preg = input("Age at first pregnancy: ")
        if age_first_preg == "NA":
            age_first_preg = str(int(age_mother) - int(age_first))
        age_last_preg = input("Age at last pregnancy: ")
        if age_last_preg == "NA":
            age_last_preg = str(int(age_mother) - int(age_last))
        twice_birth = ask_y_n("Two births in a year (not twins) y/n: ", "Two births in a year",
                              "No two births in a year")
        breast_feeding = ask_y_n("Breast feeding?")
        if breast_feeding:
            breast_feeding_data = "Breast feeding"
            feed_details = feed_duration(conn, cursor, file_number, children_number)
        else:
            breast_feeding_data = "No Breast feeding"
            feed_details = ("NA",) * 3
        kid_feeding, duration_feeding, breast_usage = feed_details
        type_birth_control = input("Type of birth control used: ")
        if str.lower(type_birth_control) == "na":
            type_birth_control, detail_birth_control, duration_birth_control = ("NA",) * 3
        else:
            detail_birth_control = input("Details of birth control used: ")
            duration_birth_control = input("Duration of birth control use: ")
        data_list = [menarche, menopause, menopause_age, lmp, period_type, number_pregnancy, number_term,
                     number_abortion,age_first, age_first_preg, age_last, age_last_preg, twice_birth,
                     breast_feeding_data, kid_feeding, duration_feeding, breast_usage, type_birth_control,
                     detail_birth_control, duration_birth_control]
        columns_list = ["Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period",
                        "Period_Type", "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child","Age_first_pregnancy", \
                        "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding",
                        "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding",
                        "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"]
        check = review_input(file_number, columns_list, data_list)
    data = menarche, menopause, menopause_age, lmp, period_type, number_pregnancy, number_term, number_abortion,\
           age_first, age_first_preg, age_last, age_last_preg, twice_birth, breast_feeding_data, kid_feeding, \
           duration_feeding, breast_usage, type_birth_control, detail_birth_control, duration_birth_control
    columns = "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period", "Period_Type", \
              "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child", \
              "Age_first_pregnancy", "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding", \
              "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding", \
              "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"
    update_multiple(conn, cursor, table, columns, file_number, data)

def breast_symptoms(conn, cursor, file_number, table):
    from ask_y_n_statement import get_symptom, get_rb_lb, ask_y_n
    from add_update_sql import update_multiple, review_input
    from breast_cancer_tables import other_symp
    check = False
    while not check:
        symp_state = ["Pain or tenderness", "Lumps", "Nipple Discharge", "Nipple Retraction", "Dimpling", \
                     "Discolouration", "Ulceration", "Eczema"]
        rb_symp_list = []
        rb_dur_list= []
        lb_symp_list = []
        lb_dur_list = []
        for index in symp_state:
            RB = ask_y_n(index + " in Right Breast?")
            if RB:
                rb_symp = index
                rb_dur = input ("Duration of "+ index+": ")
                rb_symp_list.append(rb_symp)
                rb_dur_list.append(rb_dur)
            LB = ask_y_n(index + " in Left Breast?")
            if LB:
                lb_symp = index
                lb_dur = input ("Duration of "+ index+": ")
                lb_symp_list.append(lb_symp)
                lb_dur_list.append(lb_dur)
        rb_symps = "; ".join(rb_symp_list)
        rb_duration = "; ".join(rb_dur_list)
        lb_symps = "; ".join(lb_symp_list)
        lb_duration = "; ".join(lb_dur_list)
        data_list = [rb_symps, rb_duration, lb_symps, lb_duration]
        for index in range(0, len(data_list)):
            if data_list[index] == '':
                data_list[index] = "NA"
        columns_list = ["RB_symptoms", "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration"]
        check = review_input(file_number, columns_list, data_list)
    data = tuple(data_list)
    columns = "RB_symptoms", "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration"
    update_multiple(conn,cursor, table, columns, file_number, data)
    check = False
    while not check:
        rb_symp_list = []
        rb_dur_list = []
        lb_symp_list = []
        lb_dur_list = []
        other_symptom = ask_y_n("Other Symptoms?")
        if other_symptom:
            check = True
            while check:
                type = input("Other Symptoms type? ")
                RB = ask_y_n(type + " in Right Breast?")
                if RB:
                    rb_symp = type
                    rb_dur = input("Duration of " + type)
                    rb_symp_list.append(rb_symp)
                    rb_dur_list.append(rb_dur)
                LB = ask_y_n(type + " in Left Breast?")
                if LB:
                    lb_symp = type
                    lb_dur = input("Duration of " + type)
                    lb_symp_list.append(lb_symp)
                    lb_dur_list.append(lb_dur)
                check = ask_y_n("Additional Symptoms?")
        rb_symps_other = "; ".join(rb_symp_list)
        rb_duration_other = "; ".join(rb_dur_list)
        lb_symps_other = "; ".join(lb_symp_list)
        lb_duration_other = "; ".join(lb_dur_list)
        data_list = [rb_symps_other, rb_duration_other , lb_symps_other , lb_duration_other]
        for index in range(0, len(data_list)):
            if data_list[index] == '':
                data_list[index] = "NA"
        columns_list = ["RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "LB_Other_Symptoms_duration"]
        check = review_input(file_number, columns_list, data_list)
    data = tuple(data_list)
    columns = "RB_Other_Symptoms", "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "LB_Other_Symptoms_duration"
    update_multiple(conn, cursor, table, columns, file_number, data)



def habits(conn, cursor, file_number, table):
    from add_update_sql import update_multiple, review_input
    from ask_y_n_statement import ask_option, ask_y_n
    check = False
    while not check:
        category = "Diet"
        options = ["Vegetarian", "Non-Vegetarian", "Ovo-Vegetarian", "Other"]
        diet = ask_option(category, options)
        alcohol = ask_y_n("Alcohol consumption")
        if alcohol:
            alcohol_consump = "Alcohol Consumption"
            alcohol_age = input("Consumption of alcohol from which age (yrs): ")
            alcohol_quant = input("Quantity of alcohol consumed per week: ")
            alcohol_duration = input("Duration of alcohol consumption: ")
            alcohol_comments = input("Additional comments for alcohol consumption: ")
        else:
            alcohol_consump = "No Alcohol Consumption"
            alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments = ("NA",) * 4
        columns_list = ["Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week",
                        "Duration_alcohol", "Comments_alcohol"]
        data_list = [diet, alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments]
        check = review_input(file_number, columns_list, data_list)
    columns = "Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week", "Duration_alcohol", "Comments_alcohol"
    new_data = diet, alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments
    update_multiple(conn, cursor, table, columns, file_number, new_data)
    check = False
    while not check:
        tobacco = ask_y_n("Tobacco consumption")
        if tobacco:
            tobacco = "Tobacco consumption"
            tobacco_type = input("Type of tobacco consumption: ")
            tobacco_age = input("Consumption of tobacco from which age (yrs): ")
            tobacco_quant = input("Quantity of tobacco consumed per week: ")
            tobacco_duration = input("Duration of tobacco consumption: ")
            tobacco_comments = input("Additional comments for tobacco consumption: ")
        else:
            tobacco = "No Tobacco Consumption"
            tobacco_type, tobacco_age, tobacco_quant, tobacco_duration, tobacco_comments = ("NA",) * 5
        other_del_habits = input("Other Deleterious Habits (if present give details): ")
        columns_list = ["Tobacco_y_n", "Type_tobacco", "Tobacco_consumption_age_yrs", "Quantity_tobacco_per_week",
                        "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"]
        data_list = [tobacco, tobacco_type, tobacco_age, tobacco_quant, tobacco_duration, tobacco_comments,
                     other_del_habits]
        check = review_input(file_number, columns_list, data_list)
    columns = "Tobacco_y_n", "Type_tobacco", "Tobacco_consumption_age_yrs", "Quantity_tobacco_per_week", \
              "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"
    data = tobacco, tobacco_type, tobacco_age, tobacco_quant, tobacco_duration, tobacco_comments, other_del_habits
    update_multiple(conn, cursor, table, columns, file_number, data)


def metastasis_symp (conn, cursor, file_number, table):
    from add_update_sql import update_single, review_input
    from ask_y_n_statement import ask_y_n
    check = False
    while not check:
        met_none = ask_y_n("Metastatis Symptoms Present?")
        met = []
        if not met_none:
            met = [["No Metastatis Symptoms"]]
        else:
            met_bone = ask_y_n("Bone Pain")
            if met_bone:
                met.append(["Bone Pain"])
            met_cough = ask_y_n("Cough")
            if met_cough:
                met.append(["Cough"])
            met_jaundice = ask_y_n("Jaundice")
            if met_jaundice:
                met.append(["Jaundice"])
            met_headache = ask_y_n("Headache")
            if met_headache:
                met.append(["Headache"])
            met_weight = ask_y_n("Weight loss")
            if met_weight:
                met.append(["WeightLoss"])
        met_flat = [item for sublist in met for item in sublist]
        data_met = "; ".join(met_flat)
        check = review_input(file_number, ["Metastasis_Symptoms"], [data_met])
    update_single(conn, cursor, table, "Metatasis_Symptoms", file_number, data_met)


def det_by(conn, cursor, table, file_number):
    from add_update_sql import update_multiple, review_input
    from ask_y_n_statement import ask_option
    check = False
    while not check:
        category = "Current Breast Cancer"
        options = ["Self", "Physician", "Screening Camp", "Other"]
        determined_by = ask_option(category, options)
        if determined_by == "Screening Camp":
            sc_id = input("Screening Camp ID: ")
            determined_by = "Screening Camp ID " + sc_id
        det_date = input("Date of current breast cancer detection: ")
        columns_list = ["Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date"]
        data_list = [determined_by, det_date]
        check = review_input(file_number, columns_list, data_list)
    columns = "Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date"
    data = determined_by, det_date
    update_multiple(conn, cursor, table, columns, file_number, data)


def family_cancer(conn, cursor, file_number, table):
    from add_update_sql import update_multiple, review_input
    from breast_cancer_tables import family_cancer_table
    from ask_y_n_statement import ask_y_n
    check = False
    while not check:
        family_cancer_history_y_n = ask_y_n('Cancer history in Family')
        if family_cancer_history_y_n:
            family_cancer = family_cancer_table(conn, cursor, file_number)
            family_cancer_history_y_n = "Family History of Cancer"
        else:
            family_cancer_history_y_n = "No Family History of Cancer"
            family_cancer = "NA"
        data_list = [family_cancer_history_y_n, family_cancer]
        columns_list = ["FamilyCancer_history_y_n", "Type_DegreeRelation_TypeRelation_Age_FamilyCancer"]
        check = review_input(file_number, columns_list, data_list)
    data = family_cancer_history_y_n, family_cancer
    columns = "FamilyCancer_history_y_n", "Type_DegreeRelation_TypeRelation_Age_FamilyCancer"
    update_multiple(conn, cursor, table, columns, file_number, data)


def bio_info(conn, cursor, file_number, table):
    import add_update_sql
    import ask_y_n_statement
    check = False
    while not check:
        mr_number = input('MR_number :')
        name = input('Name :')
        consent = ask_y_n_statement.ask_y_n("Is consent form with signature present in file", "Consent Taken",
                                            "Consent form not present")
        aadhaar_card = input("Aadhaar card number (if available): ")
        date_first = input("Date of first visit: ")
        permanent_address = input('Permanent_Address :')
        current_address = input('Current_Address :')
        phone = input('Phone :')
        email_id = input('Email_ID :')
        gender = input('Gender :')
        age_yrs = input('Age (yrs) :')
        date_of_birth = input('Date of Birth :')
        place_birth = input('Place of Birth :')
        height_cm = input('Height (cm) :')
        weight_kg = input('Weight (kg) :')
        height = float(height_cm) / 100
        weight = float(weight_kg)
        BMI = str(round(weight / (height * height)))
        columns_list = ["MR_number", "Name", "Consent", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address",
                        "Current_Address", "Phone", "Email_ID", "Gender", "Age_yrs", "Date_of_Birth", "Place_Birth",
                        "Height_cm", "Weight_kg", "BMI"]
        new_data = [mr_number, name, consent, aadhaar_card, date_first, permanent_address, current_address, phone,
                    email_id, gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg, BMI]
        check = add_update_sql.review_input(file_number, columns_list, new_data)
    columns = "MR_number", "Name", "Consent", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address", "Current_Address", \
              "Phone", "Email_ID", "Gender", "Age_yrs", "Date_of_Birth", "Place_Birth", "Height_cm", "Weight_kg", "BMI"
    data = mr_number, name, consent, aadhaar_card, date_first, permanent_address, current_address, phone, email_id, \
           gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg, BMI
    add_update_sql.update_multiple(conn, cursor, table, columns, file_number, data)
