import modules.ask_y_n_statement as ask_y_n_statement
import sql.add_update_sql as add_update_sql
import modules.pccm_names as pccm_names
import pandas as pd

def clinical_tests():
    import modules.ask_y_n_statement as ask_y_n_statement
    other_tests = {'USG Abdomen': ['Abnormal'], 'CECT Abdomen and Thorax': ['Visceral Metastasis'],
                   'PET Scan': ['Visceral Metastasis', 'Skeletal Metastasis'], 'Bone Scan': ['Skeletal Metastasis']}
    test_key = list(other_tests.keys())
    data_list = []
    for test in test_key:
        test_name = test
        test_done = ask_y_n_statement.ask_y_n("Has "+test_name+" been done?")
        if test_done:
            test_done = test_name+" done"
            data_list.append(test_done)
            abnormal = other_tests[test]
            for diagnosis in abnormal:
                test_diag = ask_y_n_statement.ask_y_n('Is the result ' + diagnosis + '?')
                if test_diag:
                    test_details = input("Please provide details of " + diagnosis + " diagnosis: ")
                else:
                    diagnosis = 'Normal'
                    test_details = "NA"
                data_list.append(diagnosis)
                data_list.append(test_details)
        else:
            test_done = test_name+"_not_done"
            data_list.append(test_done)
            abnormal = other_tests[test]
            for i in range(2*len(abnormal)):
                i = 'NA'
                data_list.append(i)
    return data_list


def multiple_mass(table, mammo_breast = "Right Breast"):
    number_mass = input("Number of masses detected: ")
    try:
        mass_number = int(number_mass)
    except:
        mass_number = 1
    col_list = pccm_names.names_radio_df(table)
    mass_df = pd.DataFrame(columns=col_list)
    for index in range(0, mass_number):
        mass_id = index + 1
        if table == "mammography_mass":
            check = False
            while not check:
                if mammo_breast == "Bilateral":
                    mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                                     ["Right Breast", "Left Breast"])
                else:
                    mass_location = mammo_breast
                location_quad = lesion_location(mass_location)
                mammo_mass_shape = ask_y_n_statement.ask_option("Shape of mass",
                                                                ["Oval", "Round", "Irregular", "Other"])
                mammo_mass_margin = ask_y_n_statement.ask_option("Margins of mass",
                                                                 ["Circumscribed", "Obscured",
                                                                  "Microlobulated", "Indistinct",
                                                                  "Spiculated", "Other"])
                mass_nipple = input("Distance from nipple (cm): ")
                mass_size = input("Mass dimensions (without unit): ")
                mass_size_unit = input ("Mass dimensions unit: ")
                mass_id = "Mass " + str(index + 1)
                data_list = [mass_id, location_quad, mammo_mass_shape, mammo_mass_margin, mass_nipple, mass_size, mass_size_unit]
                mass_df.loc[index] = data_list
                check, mass_df = add_update_sql.review_df_row(mass_df)
            data_list = []
            for index in col_list:
                data_mass = "; ".join(list(mass_df.loc[:, index]))
                data_list.append([data_mass])
            data_df = ask_y_n_statement.join_lists(data_list, "; ")
            mass_id_, location_quad, mammo_mass_shape, mammo_mass_margin, mass_nipple, \
            mass_size, mass_size_unit  = data_df
            data_return = number_mass, location_quad, mammo_mass_shape, mammo_mass_margin, mass_nipple, mass_size, mass_size_unit
        elif table == "sonnomammography_mass":
            check = False
            while not check:
                if mammo_breast == "Bilateral":
                    mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                                 ["Right Breast", "Left Breast"])
                else:
                    mass_location = mammo_breast
                location_clock = input("What is the clock position of mass " + str(mass_id) + "?")
                location_clock = location_clock + " o'clock"
                mass_shape = ask_y_n_statement.ask_option("Shape of mass " + str(mass_id), ["Oval", "Round",
                                                                                            "Irregular", "Other"])
                mass_size = input("Mass dimensions (without unit): ")
                mass_size_unit = input("Mass dimensions unit: ")
                mass_margin = ask_y_n_statement.ask_option("Margin of mass " + str(mass_id), ["Circumscribed",
                                                                                              "Indistinct", "Angular",
                                                                                                "Microlobulated"])
                mass_echo = ask_y_n_statement.ask_option("Echo pattern of mass "+ str(mass_id), ["Anechoic",
                                                                                                 "Hyperechoic",
                                                                                                 "Complex cystic "
                                                                                                 "and solid",
                                                                                                 "Hypoechoic",
                                                                                                 "Isoechoic",
                                                                                                 "Heterogeneous",
                                                                                                 "Other"])
                mass_id = "Mass " + str(index + 1)
                data_list = [mass_id, mass_location, location_clock, mass_shape, mass_margin, mass_echo, mass_size, mass_size_unit]
                mass_df.loc[index] = data_list
                check, mass_df= add_update_sql.review_df_row(mass_df)
            data_list = []
            for index in col_list:
                data_mass = "; ".join(list(mass_df.loc[:, index]))
                data_list.append([data_mass])
            data_df = ask_y_n_statement.join_lists(data_list, "; ")
            mass_id_, mass_location, location_clock, mass_shape, mass_margin, mass_echo, mass_size, mass_size_unit = data_df
            if mammo_breast != 'Bilateral':
                mass_location = mammo_breast
            data_return = number_mass, mass_location,location_clock, mass_shape, mass_margin, mass_echo, mass_size, mass_size_unit
        elif table == "mri_mass":
            check = False
            while not check:
                if mammo_breast == "Bilateral":
                    mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                                 ["Right Breast", "Left Breast"])
                else:
                    mass_location = mammo_breast
                mri_mass_shape = ask_y_n_statement.ask_option("Shape of mass", ["Oval", "Round", "Irregular", "Other"])
                mri_mass_margin = ask_y_n_statement.ask_option("Margins of mass",
                                                               ["Circumscribed", "Irregular", "Spiculated"])

                mri_mass_internal = ask_y_n_statement.ask_option("Internal enhancement characteristics", ["Homogeneous", "Heterogeneous", "Rim enhancement",
                                                                                                          "Dark internal septations"])
                mass_id = "Mass " + str(index + 1)
                data_list = [str(mass_id), mass_location, mri_mass_shape, mri_mass_margin,
                             mri_mass_internal]
                mass_df.loc[index]= data_list
                check, mass_df= add_update_sql.review_df_row(mass_df)
            data_list = []
            for index in col_list:
                data_mass = "; ".join(list(mass_df.loc[:, index]))
                data_list.append([data_mass])
            data_df = ask_y_n_statement.join_lists(data_list, "; ")
            mass_id_, mass_location, mri_mass_shape, mri_mass_margin, mri_mass_internal = data_df
            if mammo_breast != 'Bilateral':
                mass_location = mammo_breast
            data_return = number_mass, mass_location, mri_mass_shape, mri_mass_margin, mri_mass_internal
        else:
            data_return = "Table does not exist"
    return data_return


def birads ():
    import modules.ask_y_n_statement as ask_y_n_statement

    check = False
    while not check:
        mammo_birads = ask_y_n_statement.ask_option("BI-RADS Category", ["Category 0", "Category 1", "Category 2", "Category 3",
                                                            "Category 4", "Category 4A", "Category 4B", "Category 4C",
                                                            "Category 5", "Other"])
        if mammo_birads == "Category 0":
            mammo_birads_det = "Incomplete – Need Additional Imaging Evaluation"
        elif mammo_birads == "Category 1":
            mammo_birads_det = "Negative"
        elif mammo_birads == "Category 2":
            mammo_birads_det = "Benign"
        elif mammo_birads == "Category 3":
            mammo_birads_det = "Probably Benign"
        elif mammo_birads == "Category 4":
            mammo_birads_det = "Suspicious"
        elif mammo_birads == "Category 4A":
            mammo_birads_det = "Low suspicion for malignancy"
        elif mammo_birads == "Category 4B":
            mammo_birads_det = "Moderate suspicion for malignancy"
        elif mammo_birads == "Category 4C":
            mammo_birads_det = "High suspicion for malignancy"
        elif mammo_birads == "Category 5":
            mammo_birads_det = "Highly Suggestive of Malignancy"
        else:
            mammo_birads_det = input("Details of BI-RADS category: ")
        birad = mammo_birads + ": "+ mammo_birads_det
        print (birad)
        check = ask_y_n_statement.ask_y_n("Is this correct?")
    data_list = birad
    return data_list


def cal_table (file_number, mammo_breast):
    import modules.ask_y_n_statement as ask_y_n_statement
    import sql.add_update_sql as add_update_sql
    import modules.pccm_names as pccm_names
    table = "calcification_mammography"
    mass_number = input("Number of groups of calcifications detected? ")
    try:
        number_calc = int(mass_number)
    except:
        number_calc = 1
    location, calc_type, calicification_comments = [list([]) for _ in range(3)]
    for index in range(0, number_calc):
        check = False
        while not check:
            mass_id = index + 1
            if mammo_breast == "Bilateral":
                mass_location = ask_y_n_statement.ask_option("Location of calcification group " + str(mass_id),
                                                         ["Right Breast", "Left Breast"])
            else:
                mass_location = mammo_breast
            location.append(mass_location)
            mammo_calcification = ask_y_n_statement.ask_option("Calcification Type ",
                                                       ["Skin", "Vascular", "Coarse or 'Popcorn-like'",
                                                        "Large Rod-like", "Round and punctate", "Eggshell or Rim",
                                                        "Dystrophic", "Suture", "Amorphous", "Coarse Heterogeneous",
                                                        "Fine Pleomorphic", "Fine Linear or Fine Linear Branching",
                                                        "Other"])
            calc_type.append(mammo_calcification)
            mass_id = "Group " + str(index + 1)
            comment = input('Additional comments for calcification: ')
            calicification_comments.append(comment)
            data_list = [file_number, mass_id, mass_location, mammo_calcification, comment]
            col_list = pccm_names.names_radio_df(table)
            check = add_update_sql.review_input(file_number, col_list, data_list)
    all_data = [[str(mass_number)], location, calc_type, calicification_comments]
    data_return = ask_y_n_statement.join_lists(all_data, "; ")
    return tuple(data_return)

def lesion_location(lesion, category = ["Location on Right Breast", "Location on Left Breast"],
                    option = ["UOQ", "UIQ","UCQ", "LOQ","LIQ","LCQ", "COQ", "CIQ","CCQ", "Data not available", "Other"]):
    import modules.ask_y_n_statement as ask_y_n_statement
    lesion_data =[]
    if lesion in {"Right Breast", "Both"}:
        lesion_rb = ask_y_n_statement.ask_option(category[0], option)
        lesion_rb_data = "RB-" + lesion_rb
        lesion_data.append(lesion_rb_data)
    if lesion in {"Left Breast", "Both"}:
        lesion_lb = ask_y_n_statement.ask_option(category[1],option)
        lesion_lb_data = "LB-" + lesion_lb
        lesion_data.append(lesion_lb_data)
    lesion_data = "|".join(lesion_data)
    return lesion_data
