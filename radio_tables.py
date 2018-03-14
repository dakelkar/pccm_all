def multiple_mass(table, conn, cursor, file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    data_return = []
    mass_number = int(input("Number of masses detected"))
    if table == "SonnoMammography_Multiple_Mass":
        sonno_quad, sonno_location, sonno_clock, sonno_shape, sonno_orientation, sonno_margin, sonno_echo, \
        sonno_posterior = [list([]) for _ in range(8)]
    if table == "Mammography_Multiple_Mass":
        location, quad, shape, margin, density = [list([]) for _ in range(5)]
    if table == "MRI_Multiple_Mass":
        location, quad, shape, margin, internal = [list([]) for _ in range(5)]
    for index in range(0, mass_number):
        check = False
        while not check:
            mass_id = index + 1
            if table == "Mammography_Multiple_Mass":
                mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                             ["Right Breast", "Left Breast"])
                location.append(mass_location)
                location_quad = ask_y_n_statement.ask_option("Location Quadrant",
                                                             ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"])
                quad.append(location_quad)
                mammo_mass_shape = ask_y_n_statement.ask_option("Shape of mass", ["Oval", "Round", "Irregular"])
                shape.append(mammo_mass_shape)
                mammo_mass_margin = ask_y_n_statement.ask_option("Margins of mass",
                                                             ["Circumscribed", "Obscured", "Microlobulated", "Indistinct",
                                                              "Spiculated"])
                margin.append(mammo_mass_margin)
                mammo_mass_density = ask_y_n_statement.ask_option("Density of mass",
                                                              ["High density", "Equal density", "Low density",
                                                               "Fat-containing"])
                density.append(mammo_mass_density)
                data_list = [file_number, mass_location, location_quad, mammo_mass_shape,mammo_mass_margin,
                             mammo_mass_density]
            elif table == "MRI_Multiple_Mass":
                mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                             ["Right Breast", "Left Breast"])
                location.append(mass_location)
                location_quad = ask_y_n_statement.ask_option("Location Quadrant",
                                                             ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"])
                quad.append(location_quad)
                mri_mass_shape = ask_y_n_statement.ask_option("Shape of mass", ["Oval", "Round", "Irregular"])
                shape.append(mri_mass_shape)
                mri_mass_margin = ask_y_n_statement.ask_option("Margins of mass",
                                                                 ["Circumscribed", "Not circumscribed"])
                if mri_mass_margin == "Not circumscribed":
                    mri_mass_notc = ask_y_n_statement.ask_option("Not circumscribed margins of mass", ["Irregular",
                                                                                                         "Spiculated"])
                    mri_mass_margin = mri_mass_margin +": "+mri_mass_notc

                margin.append(mri_mass_margin)
                mri_mass_internal = ask_y_n_statement.ask_option("Internal enhancement characteristics",
                                                                  ["Homogeneous", "Heterogeneous", "Rim enhancement",
                                                                   "Dark internal septations"])
                internal.append(mri_mass_internal)
                mass_id = "Mass " + str(index + 1)
                data_list = [file_number, mass_id, mass_location, location_quad, mri_mass_shape, mri_mass_margin,
                             mri_mass_internal]
            elif table == "SonnoMammography_Multiple_Mass":
                mass_location = ask_y_n_statement.ask_option("Location of mass "+str(mass_id), ["Right Breast", "Left Breast"])
                sonno_location.append(mass_location)
                location_quad = lesion_location(mass_location)
                sonno_quad.append(location_quad)
                location_clock = input("What is the clock position of mass "+str(mass_id)+"?")
                location_clock = location_clock +" o'clock"
                sonno_clock.append(location_clock)
                mass_shape = ask_y_n_statement.ask_option("Shape of mass " + str(mass_id), ["Oval", "Round", "Irregular"])
                sonno_shape.append(mass_shape)
                mass_orientation = ask_y_n_statement.ask_option("Orientation of mass " + str(mass_id), ["Parallel", "Not parallel"])
                sonno_orientation.append(mass_orientation)
                mass_margin = ask_y_n_statement.ask_option("Margin of mass " + str(mass_id), ["Circumscribed", "Not circumscribed"])
                if mass_margin == "Not circumscribed":
                    mass_margin = ask_y_n_statement.ask_option("Is Not circumscribed margin" , ["Indistinct", "Angular",
                                "Microlobulated", "Spiculated"])
                sonno_margin.append(mass_margin)
                mass_echo = ask_y_n_statement.ask_option("Echo patter of mass "+ str(mass_id), ["Anechoic", "Hyperechoic",
                            "Complex cystic and solid", "Hypoechoic", "Isoechoic", "Heterogeneous"])
                sonno_echo.append(mass_echo)
                mass_posterior = ask_y_n_statement.ask_option("Posterior features", ["No posterior features", "Enhancement",
                                "Shadowing", "Combined pattern"])
                sonno_posterior.append(mass_posterior)
                mass_id = "Mass "+ str(index+1)
                data_list = [file_number, mass_id, mass_location, location_quad, location_clock, mass_shape,
                             mass_orientation, mass_margin, mass_echo, mass_posterior]
            col_list = pccm_names.mammo_tables(table)
            check = add_update_sql.review_input(file_number, col_list, data_list)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data_list)
    if table == "SonnoMammography_Multiple_Mass":
        all_data = [[str(mass_number)],sonno_quad, sonno_location, sonno_clock, sonno_shape, sonno_orientation,
                    sonno_margin, sonno_echo, sonno_posterior]
    elif table == "Mammography_Multiple_Mass":
        all_data = [[str(mass_number)],location, quad, shape, margin, density]
    elif table == "MRI_Multiple_Mass":
        all_data = [[str(mass_number)],location, quad, shape, margin, internal]
    else:
        all_data = []
    for index in all_data:
        data_joint = "; ".join(index)
        data_return.append(data_joint)
    return tuple(data_return)

def birads ():
    import ask_y_n_statement
    mammo_birads = ask_y_n_statement.ask_option("BI-RADS", ["0", "I", "II", "III", "IV", "IVA", "IVB", "IVC" "V"])
    check = False
    while not check:
        if mammo_birads == "0":
            mammo_birads_det = "Incomplete – Need Additional Imaging Evaluation"
        elif mammo_birads == "I":
            mammo_birads_det = "Negative"
        elif mammo_birads == "II":
            mammo_birads_det = "Benign"
        elif mammo_birads == "III":
            mammo_birads_det = "Probably Benign"
        elif mammo_birads == "IV":
            mammo_birads_det = "Suspicious"
        elif mammo_birads == "IVA":
            mammo_birads_det = "Low suspicion for malignancy"
        elif mammo_birads == "IVB":
            mammo_birads_det = "Moderate suspicion for malignancy"
        elif mammo_birads == "IVC":
            mammo_birads_det = "High suspicion for malignancy"
        elif mammo_birads == "V":
            mammo_birads_det = "Highly Suggestive of Malignancy"
        else:
            mammo_birads_det = input("Details of BI-RADS category: ")
        print ("BI-RAD " + mammo_birads +": "+mammo_birads_det)
        check = ask_y_n_statement.ask_y_n("Is this correct?")
    data_list = [mammo_birads, mammo_birads_det]
    return (tuple(data_list))

def cal_table (file_number, conn, cursor):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    table = "Calcification_Mammography"
    data_return = []
    mass_number = int(input("Number of calcifications detected"))
    location, quad, type, calc_type, dist= [list([]) for _ in range(5)]
    for index in range(0, mass_number):
        check = False
        while not check:
            mass_id = index + 1
            mass_location = ask_y_n_statement.ask_option("Location of mass " + str(mass_id),
                                                         ["Right Breast", "Left Breast"])
            location.append(mass_location)
            location_quad = lesion_location(mass_location)
            quad.append(location_quad)

            mammo_calcification = ask_y_n_statement.ask_option("Calcification Type",
                                                       ["Skin", "Vascular", "Coarse or 'Popcorn-like'",
                                                        "Large Rod-like", "Round and punctate", "Eggshell or Rim",
                                                        "Dystrophic", "Suture", "Amorphous", "Coarse Heterogeneous",
                                                        "Fine Pleomorphic", "Fine Linear or Fine Linear Branching",
                                                        "Other"])
            type.append(mammo_calcification)
            if mammo_calcification in {"Skin", "Vascular", "Coarse or 'Popcorn-like'", "Large Rod-like", "Round and punctate",
                                       "Eggshell or Rim", "Dystrophic", "Suture"}:
                mammo_calcification_type = "Typically Benign"
                print("Calcification Type is " + mammo_calcification_type)
                check = ask_y_n_statement.ask_y_n("Is Calcification type correct?")
            elif mammo_calcification in {"Amorphous", "Coarse Heterogeneous", "Fine Pleomorphic",
                                         "Fine Linear or Fine Linear Branching"}:
                mammo_calcification_type = "Suspicious Morphology"
                print("Calcification Type is " + mammo_calcification_type)
                check = ask_y_n_statement.ask_y_n("Is Calcification type correct?")
            else:
                mammo_calcification_type = input("Calcification type " + mammo_calcification + "? ")
            if not check:
                mammo_calcification_type = input("Calcification type " + mammo_calcification + "? ")
            calc_type.append(mammo_calcification_type)

            mammo_calcification_distribution = ask_y_n_statement.ask_option("Distribution of calcification",
                                                                    ["Diffuse", "Regional", "Grouped", "Linear",
                                                                     "Segmental"])
            dist.append(mammo_calcification_distribution)
            mass_id = "Mass " + str(index + 1)
            data_list = [file_number, mass_id, mass_location, location_quad,mammo_calcification,
                         mammo_calcification_type, mammo_calcification_distribution]
            col_list = pccm_names.mammo_tables(table)
            check = add_update_sql.review_input(file_number, col_list, data_list)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data_list)
    all_data = [[str(mass_number)], location, quad, type, calc_type, dist]
    for index in all_data:
        data_joint = "; ".join(index)
        data_return.append(data_joint)
    return tuple(data_return)

def lesion_location(lesion, category = ["Location on Right Breast", "Location on Left Breast"],
                    option = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"] ):
    import ask_y_n_statement
    lesion_data =[]
    if lesion in {"Right Breast", "Both"}:
        lesion_rb = ask_y_n_statement.ask_option(category[0], option)
        lesion_rb_data = "RB-" + lesion_rb
        lesion_data.append(lesion_rb_data)
    if lesion in {"Left Breast", "Both"}:
        lesion_lb = ask_y_n_statement.ask_option(category[1],option)
        lesion_lb_data = "LB-" + lesion_lb
        lesion_data.append(lesion_lb_data)
    lesion_data = "; ".join(lesion_data)
    return lesion_data
