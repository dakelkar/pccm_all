def nut_supplements(conn, cursor, file_number, table):
    from add_update_sql import review_input
    from breast_cancer_tables import nut_supp_table
    from ask_y_n_statement import ask_y_n
    import pccm_names
    module_name = "nut_supplements"
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
        columns_list = pccm_names.names_info(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def phys_act(conn, cursor, file_number):
    from breast_cancer_tables import physical_activity_table
    from add_update_sql import review_input
    from ask_y_n_statement import ask_y_n
    import pccm_names
    module_name = "phys_act"
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
        columns_list = pccm_names.names_info(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def med_history(conn, cursor, file_number):
    from breast_cancer_tables import med_history_table
    from ask_y_n_statement import ask_y_n
    from add_update_sql import review_input
    import pccm_names
    module_name = "med_history"
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
        columns_list = pccm_names.names_info(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def cancer_history(conn, cursor, file_number):
    from breast_cancer_tables import cancer_table
    from add_update_sql import review_input
    from ask_y_n_statement import ask_y_n
    import pccm_names
    module_name = "cancer_history"
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
        columns_list = pccm_names.names_info(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def family_details(conn, cursor, file_number):
    from add_update_sql import review_input
    from ask_y_n_statement import ask_option, ask_y_n
    import pccm_names
    import breast_cancer_tables
    module_name = "family_details"
    check = False
    while not check:
        marital_status = input('Marital Status :')
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
        if number_pregnancy == "0":
            age_first_preg, age_last_preg, number_term, number_abortion, age_first, age_last, twice_birth, \
            breast_feeding_data, kid_feeding, duration_feeding, breast_usage = ('NA',) * 11
        else:
            number_term = input("Pregnancy carried to term (include abortion after 6 months): )")
            number_abortion = input("Number of abortions: ")
            age_first_preg = input("Age at first pregnancy: ")
            sql = ('SELECT Age_yrs FROM Patient_Information_History WHERE File_number = \'' + file_number + "'")
            cursor.execute(sql)
            age = cursor.fetchall()
            age_mother = age[0][0]
            if children_number == 'No Children':
                age_first, age_last, twice_birth, breast_feeding_data, kid_feeding, \
                duration_feeding, breast_usage = ('NA',) * 7
            else:
                age_first = input("Age of first child: ")
                if int(children_number) > 1:
                    age_last = input("Age of last child: ")
                else:
                    age_last = age_first
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
                feed_details = breast_cancer_tables.feed_duration(conn, cursor, file_number, children_number)
            else:
                breast_feeding_data = "No Breast feeding"
                feed_details = ("NA",) * 3
            kid_feeding, duration_feeding, breast_usage = feed_details
        fert_treat_y_n = ask_y_n("Fertility_treatment_y_n")
        if fert_treat_y_n:
            fert_treat = "Fertility Treatment used"
            type_fert = input("Type of fertility treatment used: ")
            detail_fert = input ("Details of fertility treatment used:")
            cycles_fert = input("Number of cycles of fertility treatment taken: ")
            success_fert = ask_y_n("Did fertility treatment result in successful pregnancy? ", "Pregnancy from Treatment", "No pregnancy from treatment")
        else:
            fert_treat = "No Fertility Treatment used"
            type_fert, detail_fert, cycles_fert, success_fert = ("NA", )* 4
        type_birth_control = input("Type of birth control used: ")
        if str.lower(type_birth_control) == "na":
            type_birth_control, detail_birth_control, duration_birth_control = ("NA",) * 3
        else:
            detail_birth_control = input("Details of birth control used: ")
            duration_birth_control = input("Duration of birth control use: ")
        data_list = [marital_status, siblings_number, sisters, brothers, children_number, daughters, sons, menarche,
                     menopause, menopause_age, lmp, period_type, number_pregnancy, number_term,
                     number_abortion, age_first, age_first_preg, age_last, age_last_preg, twice_birth,
                     breast_feeding_data, kid_feeding, duration_feeding, breast_usage, fert_treat, type_fert,
                     detail_fert, cycles_fert, success_fert, type_birth_control, detail_birth_control,
                     duration_birth_control]
        columns_list = pccm_names.names_info(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def breast_symptoms(file_number):
    from ask_y_n_statement import ask_y_n
    from add_update_sql import review_input
    import pccm_names
    import textwrap
    module_name = "breast_symptoms"
    check = False
    while not check:
        note = "Pain or tenderness; Lumps, Nipple Discharge - Milky/water discharge on pressing nippple, " \
               "Nipple Retraction - nipple reagion goes inside, Dimpling small pits anwywhere on breast, " \
               "Discolouration - may occur after surgery, Ulceration (small boils on surface), " \
               "Eczema - Reddish spots with without itching"
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=note)
        print(string)
        symp_state = ["Pain or tenderness", "Lumps", "Nipple Discharge", "Nipple Retraction", "Dimpling", \
                      "Discolouration", "Ulceration", "Eczema"]
        rb_symp_list = []
        rb_dur_list = []
        lb_symp_list = []
        lb_dur_list = []
        for index in symp_state:
            symp = ask_y_n("Is " + index + " present")
            if symp:
                RB = ask_y_n(index + " in Right Breast?")
                if RB:
                    rb_symp = index
                    rb_dur = input("Duration of " + index + ": ")
                    rb_symp_list.append(rb_symp)
                    rb_dur_list.append(rb_dur)
                LB = ask_y_n(index + " in Left Breast?")
                if LB:
                    lb_symp = index
                    lb_dur = input("Duration of " + index + ": ")
                    lb_symp_list.append(lb_symp)
                    lb_dur_list.append(lb_dur)
        rb_symps = "; ".join(rb_symp_list)
        rb_duration = "; ".join(rb_dur_list)
        lb_symps = "; ".join(lb_symp_list)
        lb_duration = "; ".join(lb_dur_list)
        data_list_symp = [rb_symps, rb_duration, lb_symps, lb_duration]
        for index in range(0, len(data_list_symp)):
            if data_list_symp[index] == '':
                data_list_symp[index] = "NA"
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
        data_list_other = [rb_symps_other, rb_duration_other, lb_symps_other, lb_duration_other]
        for index in range(0, len(data_list_other)):
            if data_list_other[index] == '':
                data_list_other[index] = "NA"
        met = []
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
        if met_flat == []:
            data_met = "No Metastatis Symptoms"
        columns_list = pccm_names.names_info(module_name)
        data_list = data_list_symp + data_list_other + [data_met]
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))



def habits(file_number):
    import pccm_names
    from add_update_sql import review_input
    from ask_y_n_statement import ask_option, ask_y_n
    module_name = "habits"
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
        data_list_alc = [diet, alcohol_consump, alcohol_age, alcohol_quant, alcohol_duration, alcohol_comments]
        tobacco = ask_y_n("Tobacco exposure (Passive and/or Active)")
        if tobacco:
            tobacco = "Tobacco consumption"
            exposure_type = ask_option("Mode of exposure to Tobacco", ["Passive", "Active", "Other"])
            if exposure_type =="Passive":
                tobacco_type_partic = ask_option("Mode of passive consumption", ["Home", "Work", "Commute",  "Social Interactions"])
                if tobacco_type_partic == "Home":
                    tobacco_type_who = input ("What is the specific source?")
                    tobacco_passive = tobacco_type_partic + (" : ") + tobacco_type_who

                else:
                    tobacco_passive = tobacco_type_partic
            else:
                tobacco_passive = "NA"
            tobacco_type = ask_option("Type of tobacco use", ["Cigarette", "Beedi", "Gutkha", "Pan Masala", "Jarda/Maava", "Hookah", "Nicotine Patch", "Mishri", "Other"])
            tobacco_age = input("Consumption of tobacco from which age (yrs): ")
            tobacco_freq = input ("Frequency of tobacco consumption: ")
            tobacco_quant = input("Quantity of tobacco consumed per week: ")
            tobacco_duration = input("Duration of tobacco consumption: ")
            tobacco_comments = input("Additional comments for tobacco consumption: ")
        else:
            tobacco = "No Tobacco Consumption"
            exposure_type, tobacco_type, tobacco_passive, tobacco_age, tobacco_freq, tobacco_quant, tobacco_duration, \
            tobacco_comments = ("NA",) * 8
        other_del_habits = input("Other Deleterious Habits (if present give details): ")
        data_list_tob = [tobacco, exposure_type, tobacco_passive,tobacco_type, tobacco_age, tobacco_freq, tobacco_quant, tobacco_duration, tobacco_comments, other_del_habits]
        columns_list = pccm_names.names_info(module_name)
        data_list = data_list_alc + data_list_tob
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))



def metastasis_symp (file_number):
    import pccm_names
    from add_update_sql import review_input
    from ask_y_n_statement import ask_y_n
    module_name = "metastasis_symp"
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
        columns_list= pccm_names.names_info(module_name)
        check = review_input(file_number, columns_list, [data_met])
    return (str(data_met))


def det_by(file_number):
    from add_update_sql import review_input
    from ask_y_n_statement import ask_option
    import pccm_names
    module_name = "det_by"
    check = False
    while not check:
        category = "Current Breast Cancer Detected by"
        options = ["Self", "Physician", "Screening Camp", "Other"]
        determined_by = ask_option(category, options)
        if determined_by == "Screening Camp":
            sc_id = input("Screening Camp ID: ")
            determined_by = "Screening Camp ID " + sc_id
        det_date = input("Date of current breast cancer detection: ")
        columns_list =pccm_names.names_info(module_name)
        data_list = [determined_by, det_date]
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))



def family_cancer(conn, cursor, file_number):
    from add_update_sql import review_input
    from breast_cancer_tables import family_cancer_table
    from ask_y_n_statement import ask_y_n
    import  pccm_names
    module_name = "family_cancer"
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
        columns_list = pccm_names.names_info(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def bio_info(file_number):
    import add_update_sql
    import ask_y_n_statement
    import pccm_names
    module_name = "bio_info"
    check = False
    while not check:
        mr_number = input('MR_number :')
        name = input('Name :')
        consent = ask_y_n_statement.ask_y_n("Is consent form with signature present in file", "Consent Taken",
                                            "Consent form not present")
        aadhaar_card = input("Aadhaar card number (if available): ")
        date_first = input("Date of first visit: ")
        permanent_address = input('Permanent Address :')
        current_address_check = ask_y_n_statement.ask_option('Current Address', ["Same as Permanent", "Different"])
        if current_address_check == "Different":
            current_address = input("Current Address: ")
        else:
            current_address = permanent_address
        phone = input('Phone :')
        email_id = input('Email_ID :')
        gender = ask_y_n_statement.ask_option('Gender', ["Female", "Male", "Other"])
        age_yrs = input('Age (yrs) :')
        date_of_birth = input('Date of Birth (mm/dd/yyyy):')
        place_birth = input('Place of Birth :')
        height = ask_y_n_statement.ask_option("Height unit", ["cm", "feet/inches"])
        if height == "cm":
            height_cm = input('Height (cm) :')
        else:
            height_feet = float(input("Height (feet)"))
            height_inch = float(input("Height (inches)"))
            height_inch = height_inch + 12 * height_feet
            height_cm = str(height_inch * 2.54)
        weight_kg = input('Weight (kg) :')
        height = float(height_cm) / 100
        weight = float(weight_kg)
        BMI = str(round(weight / (height * height)))
        columns_list = pccm_names.names_info(module_name)
        new_data = [mr_number, name, consent, aadhaar_card, date_first, permanent_address, current_address, phone,
                    email_id, gender, age_yrs, date_of_birth, place_birth, height_cm, weight_kg, BMI]
        check = add_update_sql.review_input(file_number, columns_list, new_data)
    return (tuple(new_data))