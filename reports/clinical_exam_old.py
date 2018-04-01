def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Clinical_Exam(File_number) VALUES ('" + file_number + "')")

def clinical_exam_initial (file_number):
    import ask_y_n_statement
    import add_update_sql
    import  pccm_names
    module_name = "clinical_exam_initial"
    check = False
    while not check:
        con_stat = ask_y_n_statement.ask_y_n("Has consent been taken from patient?", "Consent Taken", "No Consent")
        if con_stat == "Consent Taken":
            con_form = ask_y_n_statement.ask_y_n("Is consent form with signature present in file ?",
                                             "Consent form with signature present in folder", "Completed consent form not present in folder")
        else:
            con_form = "NA"
        prov_diag = input ("Provisional Diagnosis: ")
        options = ["Definite", "Vague", "Diffuse", "Nil", "Other"]
        lump_palp = ask_y_n_statement.ask_option("Palpable lump in the breast?", options)
        lump_location = ask_y_n_statement.ask_option("Location of lump", ["Right Breast", "Left Breast", "Both", "Not present"])
        lump_location_data = []
        if lump_location == "Right Breast" or lump_location == "Both":
            category = "Lump location on Right Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            lump_location_rb = ask_y_n_statement.ask_option(category, options)
            lump_location_rb_data = "RB-"+lump_location_rb
            lump_location_data.append(lump_location_rb_data)
        if lump_location == "Left Breast" or lump_location == "Both":
            category = "Lump location on Left Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            lump_location_lb = ask_y_n_statement.ask_option(category, options)
            lump_location_lb_data = "LB-" + lump_location_lb
            lump_location_data.append(lump_location_lb_data)
        lump_location_data = "; ".join(lump_location_data)
        if lump_location == "Not present":
            lump_location_data = "Lump " + lump_location
            lump_size, lump_number,lump_consistency,lump_fixity  = ("NA",)*4
        else:
            lump_size = ask_y_n_statement.ask_option("Lump size", ["< 2cm", "2-5 cm", ">5 cm"])
            lump_number = ask_y_n_statement.ask_option("Number of lumps", ["Single", "Multiple", "Other"])
            lump_consistency = ask_y_n_statement.ask_option("Consistency of lumps", ["Soft", "Firm", "Hard", "Cystic",
                                                                                     "Mobile", "Other"])
            lump_fixity = ask_y_n_statement.ask_option("Lump fixity to ", ["Skin", "Chest wall", "Pectoral major muscle",
                                                                           "No Fixation", "Other"])
        mastitis_location = ask_y_n_statement.ask_option("Location of mastitis",
                                                     ["Right Breast", "Left Breast", "Both", "Not present"])
        mastitis_location_data = []
        if mastitis_location == "Right Breast" or mastitis_location == "Both":
            category = "Mastitis location on Right Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            mastitis_location_rb = ask_y_n_statement.ask_option(category, options)
            mastitis_location_rb_data = "RB-" + mastitis_location_rb
            mastitis_location_data.append(mastitis_location_rb_data)
        if mastitis_location == "Left Breast" or mastitis_location == "Both":
            category = "Mastitis location on Left Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            mastitis_location_lb = ask_y_n_statement.ask_option(category, options)
            mastitis_location_lb_data = "LB-" + mastitis_location_lb
            mastitis_location_data.append(mastitis_location_lb_data)
        mastitis_location_data = "; ".join(mastitis_location_data)
        if mastitis_location == "Not present":
            mastitis_location_data = "mastitis " + mastitis_location
            mastitis_type = "NA"
        else:
            mastitis_type = ask_y_n_statement.ask_option("Mastitis type", ["Diffuse", "Sectoral", "Other"])
        tender = ask_y_n_statement.ask_option("Tenderness in breast ?",["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
        retract = ask_y_n_statement.ask_option("Nipple Retraction ?",["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
        discharge = ask_y_n_statement.ask_option("Nipple Discharge ?",
                                     ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
        if discharge == "Not Present":
            discharge_type = "NA"
        else:
            discharge_type = ask_y_n_statement.ask_option("Discharge Type?",
                                     ["Serous", "Milky", "Brown", "Bloody", "Other"])
        skin_change_location = ask_y_n_statement.ask_option("Skin Changes?",
                                     ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
        if skin_change_location == "Not Present":
            skin_change_type = "NA"
        else:
            skin_change_type = ask_y_n_statement.ask_option("Type of skin change?",
                                     ["Dimpling", "Ulceration", "Discolouration", "Eczema", "Edema", "Redness",
                                      "Peau d'orange", "Other"])
        ax_nodes = ask_y_n_statement.ask_option("Palpable axillary nodes",
                                     ["Right Breast", "Left Breast", "Both", "Not palpable", "Other"])
        if ax_nodes == "Not palpable":
            ax_nodes_number, ax_nodes_size, ax_nodes_fixity = ("NA",)*3
        else:
            ax_nodes_number = input("Number of nodes: ")
            ax_nodes_size = input("Size of nodes: ")
            ax_nodes_fixity =  ask_y_n_statement.ask_y_n("Fixity of axillary nodes", "Yes", "No")
        supra_nodes = ask_y_n_statement.ask_option("Palpable supraclavicular nodes",
                                                ["Right Breast", "Left Breast", "Both", "Not palpable", "Other"])
        if supra_nodes == "Not palpable":
            supra_nodes_number, supra_nodes_size, supra_nodes_fixity = ("NA",)*3
        else:
            supra_nodes_number = input("Number of nodes: ")
            supra_nodes_size = input("Size of nodes: ")
            supra_nodes_fixity = ask_y_n_statement.ask_y_n("Fixity of supraclavicular nodes", "Yes", "No")
        contra_breast = ask_y_n_statement.ask_option("Contralateral Breast", ["Normal", "Diffuse Mastitis", "Localised Mastitis", "Other"])
        arm_edema = ask_y_n_statement.ask_option("Edema of arm", ["Right", "Left", "Both", "Not Present", "Other"])
        arm_circ_right = input("Circumference of right arm (cm): ")
        arm_volume_right = input("Upper limb volume - right arm (cc): ")
        arm_elbow_right = input("Distance from the elbow - right arm (cm): ")
        arm_circ_left = input("Circumference of left arm (cm): ")
        arm_volume_left = input("Upper limb volume - left arm (cc): ")
        arm_elbow_left = input("Distance from the elbow - left arm (cm): ")

        data_list = [con_stat, con_form, prov_diag, lump_palp, lump_location_data, lump_size, lump_number, lump_consistency,
                     lump_fixity, mastitis_location_data, mastitis_type, tender, retract, discharge, discharge_type,
                     skin_change_location, skin_change_type, ax_nodes, ax_nodes_number, ax_nodes_size, ax_nodes_fixity,
                     supra_nodes, supra_nodes_number, supra_nodes_size, supra_nodes_fixity, contra_breast, arm_edema,
                     arm_circ_right, arm_volume_right, arm_elbow_right, arm_circ_left, arm_volume_left, arm_elbow_left]

        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def nipple_cytology (file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    module_name = "nipple_cytology"
    check = False
    while not check:
        cyto = ask_y_n_statement.ask_option("Nipple Cytology", ["Done", "Not Done"])
        if cyto == "Not Done":
            cyto_date, cyto_number, cyto_report = ("NA",)*3
        else:
            cyto_date = input("Date of nipple cytology: ")
            cyto_number = input("Nipple Cytology number: ")
            cyto_report = ask_y_n_statement.ask_option("Nipple Cytology report and interpretation", ["Normal", "Suspicious", "Diagnostic for Cancer", "Other"])
        data_list = [cyto, cyto_date, cyto_number, cyto_report]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def mammography (conn, cursor, file_number):
    import ask_y_n_statement
    import pccm_names
    import radio_tables
    import add_update_sql
    module_name = "mammography"
    check = False
    while not check:
        mammo_loc = ask_y_n_statement.ask_option("Mammography Diagnosis at", ["PCCM", "Outside", "Other"])
        mammo_details = ask_y_n_statement.ask_y_n("First Mammography?")
        if mammo_details:
            mammo_date = input("Date when mammography done: ")
            mammo_details = "First Mammography"
            mammo_number, mammo_rep_previous = ("NA",)*2
        else:
            mammo_date = input("Date of last mammography done: ")
            mammo_details = "More than one Mammography"
            mammo_number = input ("Number of mammographies undergone: ")
            mammo_rep_previous = input ("Report of previous mammography: ")
        mammo = ask_y_n_statement.ask_y_n("Mammography diagnosis done")
        if mammo:
            mammo = "Mammography diagnosis done"
            mammo_diag_date = input("Date of mammography diagnosis: ")
            mammo_diag_acc = input ("Accession number of mammography diagnosis: ")
            breast_density = ask_y_n_statement.ask_option("Density of breast", ["a. The breasts are almost entirely fatty",
                            "b. There are scattered areas of fibroglandular density", "c. The breasts are "
                            "heterogeneously dense, which may obscure small masses", "d. The breasts are extremely dense,"
                            "which lowers the sensitivity of mammography"])
            mammo_mass_location = ask_y_n_statement.ask_y_n("Is there any mass detected")
            if mammo_mass_location:
                table = "Mammography_Multiple_Mass"
                mass_number, mammo_mass_location, mammo_mass_location_quad, mammo_mass_depth, mammo_mass_dist, \
                mammo_mass_pect, mammo_mass_shape, mammo_mass_margin, mammo_mass_density = radio_tables.multiple_mass(table, conn,
                                                                                    cursor, file_number)
            else:
                mass_number = "No mass detected"
                mammo_mass_location, mammo_mass_location_quad, mammo_mass_depth, mammo_mass_dist, \
                mammo_mass_pect, mammo_mass_shape, mammo_mass_margin, mammo_mass_density = ("NA", )*8
            calc = ask_y_n_statement.ask_y_n("Is Calcification present?")
            if calc:
                calc_number, calc_location, location_quad, calc_depth, calc_dist, calc_pect, calc_name, calc_type, \
                calc_dist = radio_tables.cal_table(file_number, conn, cursor)
            else:
                calc_number = "No Calcification detected"
                calc_location, location_quad, calc_depth, calc_dist, calc_pect, calc_name, calc_type, \
                calc_dist = ("NA", )*8
            mammo_arch = ask_y_n_statement.ask_y_n("Is Architectural distortion present")
            if mammo_arch:
                arch_loc = ask_y_n_statement.ask_option("Location of Distortion", ["Right Breast", "Left Breast", "Both"])
                arch_quad = radio_tables.lesion_location(arch_loc)
                arch_depth = ask_y_n_statement.ask_option("Depth of Architectural Distortion",
                                                          ["Anterior", "Middle", "Posterior", "Other"])
                arch_dist = ask_y_n_statement.ask_option("Distance from nipple of Architectural Distortion",
                                                         ["<0.5 cm", ">0.5 cm", "Other"])
                pect_check = ask_y_n_statement.ask_y_n(
                    "Is distance from Pectoralis Major described for Architectural Distortion")
                if pect_check:
                   arch_pect = input("Distance from Pectoralis Major (cm): ")
                else:
                    arch_pect = "Distance from Pectoralis Major not described"
            else:
                arch_loc = "Not Present"
                arch_quad, arch_depth,  arch_dist,  arch_pect = ("NA", )*4
            asym = ask_y_n_statement.ask_y_n("Is asymmetry present")
            if asym:
                asym_loc = ask_y_n_statement.ask_option("Location of Asymmetry", ["Right Breast", "Left Breast", "Both"])
                asym_quad = radio_tables.lesion_location(asym_loc)
                asym_depth = ask_y_n_statement.ask_option("Depth of Asymmetry",
                                                          ["Anterior", "Middle", "Posterior", "Other"])
                asym_dist = ask_y_n_statement.ask_option("Distance from nipple of Asymmetry",
                                                         ["<0.5 cm", ">0.5 cm", "Other"])
                pect_check = ask_y_n_statement.ask_y_n(
                    "Is distance from Pectoralis Major described for Asymmetry")
                if pect_check:
                    asym_pect = input("Distance from Pectoralis Major (cm): ")
                else:
                    asym_pect = "Distance from Pectoralis Major not described"
                mammo_asymm = radio_tables.lesion_location(asym_loc,["Type of Asymmetry in Right Breast",
                            "Type of Asymmetry in Left Breast"], ["Asymmetry","Global asymmetry","Focal asymmetry",
                            "Developing asymmetry", "Other"])
            else:
                asym_quad, asym_depth, asym_dist, asym_pect, mammo_asymm = ("NA", )*5
                asym_loc = "Not Present"
            intra_lymph = ask_y_n_statement.ask_y_n("Are intra-mammary lymph nodes present?")
            if intra_lymph:
                mammo_intra = input("Description of intra-mammary lymph nodes: ")
            else:
                mammo_intra = "Intra-mammary lymph nodes not present"
            lesion = ask_y_n_statement.ask_y_n("Skin Lesion present?")
            if lesion:
                mammo_lesion = ask_y_n_statement.ask_option("Location of lesion", ["Right Breast", "Left Breast", "Both"])
            else:
                mammo_lesion = "NA"

            asso_feat = ["Skin Retraction", "Nipple Retraction", "Skin Thickening", "Trabecular Thickening",
                         "Axillary adenopathy", "Architectural Distortion", "Calcifications"]
            asso_feat_data = []
            for index in (asso_feat):
                print("Associated feature: " + index )
                print("Detailed description can be added by choosing 'Other'")
                var = ask_y_n_statement.ask_option(index, ["Present", "Absent", "Other"])
                asso_feat_data.append(var)
            asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7 = asso_feat_data
            mammo_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/diagnosis?")
            if mammo_birad:
                mammo_birad, mammo_diag = radio_tables.birads()
            else:
                mammo_birad, mammo_diag = ("NA",) * 2
        else:
            mammo = "Mammography diagnosis not done"
            mammo_diag_date, mammo_diag_acc, breast_density, mass_number, mammo_mass_location, mammo_mass_location_quad,\
            mammo_mass_depth, mammo_mass_dist, mammo_mass_pect, mammo_mass_shape, mammo_mass_margin, mammo_mass_density, \
            calc_number, calc_location, location_quad, calc_depth, calc_dist, calc_pect, calc_name, calc_type, calc_dist,\
            arch_loc, arch_quad, arch_depth, arch_dist, arch_pect, asym_quad, asym_depth, asym_dist, asym_pect, \
            mammo_asymm, mammo_intra, mammo_lesion, asso_feat_1,asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, \
            asso_feat_6, asso_feat_7, mammo_birad, mammo_diag = ("NA",) * 42
        data_list = [mammo_loc, mammo_date, mammo_details, mammo_number, mammo_rep_previous, mammo, mammo_diag_date,
                     mammo_diag_acc, breast_density, mass_number, mammo_mass_location, mammo_mass_location_quad,
                     mammo_mass_depth, mammo_mass_dist, mammo_mass_pect, mammo_mass_shape, mammo_mass_margin,
                     mammo_mass_density, calc_number, calc_location, location_quad, calc_depth, calc_dist, calc_pect,
                     calc_name, calc_type, calc_dist, arch_loc, arch_quad, arch_depth, arch_dist, arch_pect, asym_quad,
                     asym_depth, asym_dist, asym_pect, mammo_asymm, mammo_intra, mammo_lesion, asso_feat_1, asso_feat_2,
                     asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, mammo_birad, mammo_diag]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def tomosynthesis (file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    module_name = "tomosynthesis"
    check = False
    while not check:
        tomo = ask_y_n_statement.ask_y_n("3D digital Tomosynthesis done")
        if tomo:
            tomo = "3D digital Tomosynthesis done"
            tomo_date = input("Date of examination of Tomosynthesis: ")
            tomo_acc = input("Accession number of Tomosynthesis: ")
        else:
            tomo = "3D digital Tomosynthesis not done"
            tomo_date, tomo_acc,  = ("NA", )*2

        data_list = [tomo, tomo_date, tomo_acc, ]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def abvs (file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    import radio_tables
    module_name = "abvs"
    check = False
    while not check:
        abvs = ask_y_n_statement.ask_y_n("Automated Breast Volume Scanner (ABVS) done?")
        if abvs:
            abvs = "Automated Breast Volume Scanner done"
            abvs_date = input("Date of examination of ABVS: ")
            abvs_acc = input("Accession number of ABVS: ")
            abvs_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            if abvs_lesion in {"Right Breast", "Left Breast", "Both"}:
                abvs_lesion_data = radio_tables.lesion_location(abvs_lesion)
            else:
                abvs_lesion_data = "NA"
            abvs_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            abvs_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            abvs_pect = input("Distance from Pectoralis Major (cm): ")
            abvs_diagnosis = ask_y_n_statement.ask_option("ABVS Diagnosis", ["Normal", "Benign", "Suspicious",
                                                                                      "Diagnostic for Cancer"])
        else:
            abvs = "Automated Breast Volume Scanner done"
            abvs_date, abvs_acc, abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect, abvs_diagnosis \
                = ("NA", )*8

        data_list = [abvs, abvs_date, abvs_acc,abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect,
                     abvs_diagnosis]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def sonomammo (conn, cursor, file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    import radio_tables
    module_name = "sonomammo"
    check = False
    while not check:
        sonomammo = ask_y_n_statement.ask_y_n("Sono-Mammography done?")
        if sonomammo:
            sonomammo = "Sono-Mammography done"
            sonomammo_date = input("Date of examination of Sono-mammography: ")
            sonomammo_acc = input("Accession number of Sono-Mammography: ")
            sonomammo_tissue = ask_y_n_statement.ask_option("Tissue Composition",
                                                            ["a.Homogeneous background echotexture – fat",
                                                             "b. Homogeneous background echotexture – fibroglandular",
                                                             "c. Heterogeneous background echotexture", "Other"])
            mass_sonomammo = ask_y_n_statement.ask_y_n("Is there any mass detected")
            if mass_sonomammo:
                table = "SonnoMammography_Multiple_Mass"
                mass_number_sonomammo, mass_location, mass_quad, mass_clock, mass_depth, mass_distance, mass_pect, mass_shape_sonomammo, \
                mass_orientation_sonomammo, mass_margin_sonomammo, mass_echo_sonomammo, mass_posterior_sonomammo\
                    = radio_tables.multiple_mass(table, conn, cursor, file_number)
            else:
                mass_number_sonomammo = "No Mass Detected"
                mass_location, mass_quad, mass_clock, mass_depth, mass_distance, mass_pect, mass_shape_sonomammo, \
                mass_orientation_sonomammo, mass_margin_sonomammo, mass_echo_sonomammo, mass_posterior_sonomammo \
                    = ("NA",) *11
            sonomammo_calc = ask_y_n_statement.ask_option("Calcification",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            if sonomammo_calc == "Not present":
                sonomammo_calc_type = "NA"
            else:
                sonomammo_calc_type = ask_y_n_statement.ask_option("Calcification location", ["Calcifications in a mass",
                                     "Calcifications outside of a mass", "Intraductal calcifications"])
            sonomammo_arch = ask_y_n_statement.ask_option("Architectural distortion",
                                                          ["Right Breast", "Left Breast", "Both", "Not present"])
            sonomammo_duct = ask_y_n_statement.ask_option("Duct Changes",
                                                          ["Right Breast", "Left Breast", "Both", "Not present"])
            sonomammo_skin = ask_y_n_statement.ask_y_n("Skin Changes")
            if sonomammo_skin:
                sonomammo_skin = ask_y_n_statement.ask_option("Type of skin changes", ["Skin thickening",
                                                                                       "Skin retraction"])
            else:
                sonomammo_skin = "No skin changes"
            sonomammo_edema = ask_y_n_statement.ask_option("Edema", ["Right Breast", "Left Breast", "Both", "Not present"])
            sonomammo_vasc = ask_y_n_statement.ask_option("Vascularity", ["Absent", "Internal vascularity",
                            "Vessels in rim", "Other"])
            sonomammo_elast = ask_y_n_statement.ask_option("Elasticity assessment", ["Soft", "Intermediate", "Hard",
                             "Other"])
            sonomammo_lymph_intra = input("Description of intramammary lymph nodes: ")
            sonomammo_lymph_ax = ask_y_n_statement.ask_option("Axillary Lymph Nodes", ["Normal", "Abnormal"])
            if sonomammo_lymph_ax == "Abnormal":
                lymph_ax_cort = input("Cortical thickness: ")
                lymph_ax_hilum = ask_y_n_statement.ask_option("Axillary lymph node hilum", ["Lost", "Thin",
                                                                                            "Preserved", "Other"])
                lymph_ax_vasc = ask_y_n_statement.ask_option("Axillary lymph node vascularity", ["Ventral",
                                                                                                 "Peripheral", "Other"])
            else:
                lymph_ax_cort, lymph_ax_hilum, lymph_ax_vasc = ("NA", )*3
            sonomammo_sol_duct = ask_y_n_statement.ask_y_n("Is solitary dilated duct present?")
            if sonomammo_sol_duct:
                sol_duct_loc = ask_y_n_statement.ask_option("Solitary Dilated duct", ["Right Breast", "Left Breast", "Both"])
                sol_duct_diam = input("Diameter of solitary dilated duct (mm): ")
                sol_mass = ask_y_n_statement.ask_y_n("Is Intra-ductal solid mass present?",
                                                     "Intra-ductal Solid Mass Present", "Intra-ductal Solid Mass Absent")
            else:
                sol_duct_loc = "Not Present"
                sol_duct_diam, sol_mass = ("NA",)*2
            other = ask_y_n_statement.ask_y_n("Are there any other findings?")
            if other:
                print ("If more than one other finding, chose Other and enter findings separated by ; ")
                sonomammo_other = ask_y_n_statement.ask_option("Other Findings", ["Simple cyst", "Clustered microcysts",
                                "Complicated cyst", "Mass in or on skin", "Foreign body including implants",
                                "Vascular abnormalities", "AVMs (arteriovenous malformations/pseudoaneurysms)",
                                "Mondor disease", "Postsurgical ﬂuid collection", "Fat necrosis", "Other"])
            else:
                sonomammo_other = "NA"
            sono_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if sono_birad:
                sonomammo_birad, sonomammo_diag = radio_tables.birads()
            else:
                sonomammo_birad, sonomammo_diag = ("NA", )*2
        else:
            sonomammo = "Sono-Mammography not done"
            sonomammo_date, sonomammo_acc, sonomammo_tissue, mass_number_sonomammo, mass_location, mass_quad, \
            mass_clock, mass_depth, mass_distance, mass_pect, mass_shape_sonomammo, mass_orientation_sonomammo, \
            mass_margin_sonomammo, mass_echo_sonomammo, mass_posterior_sonomammo, sonomammo_calc, sonomammo_calc_type, \
            sonomammo_arch, sonomammo_duct, sonomammo_skin, sonomammo_edema, sonomammo_vasc, sonomammo_elast, \
            sonomammo_lymph_intra, sonomammo_lymph_ax, lymph_ax_cort, lymph_ax_hilum, lymph_ax_vasc,  sol_duct_loc, \
            sol_duct_diam, sol_mass,sonomammo_other, sonomammo_birad, sonomammo_diag = ("NA", )*32
        data_list = [sonomammo, sonomammo_date, sonomammo_acc, sonomammo_tissue, mass_number_sonomammo, mass_location,
                     mass_quad, mass_clock, mass_depth, mass_distance, mass_pect, mass_shape_sonomammo,
                     mass_orientation_sonomammo, mass_margin_sonomammo, mass_echo_sonomammo, mass_posterior_sonomammo,
                     sonomammo_calc, sonomammo_calc_type, sonomammo_arch, sonomammo_duct, sonomammo_skin, sonomammo_edema,
                     sonomammo_vasc, sonomammo_elast, sonomammo_lymph_intra, sonomammo_lymph_ax, lymph_ax_cort,
                     lymph_ax_hilum, lymph_ax_vasc, sol_duct_loc, sol_duct_diam, sol_mass,sonomammo_other,
                     sonomammo_birad, sonomammo_diag]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))





def mri_breast (conn, cursor, file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    import radio_tables
    module_name = "mri_breast"
    check = False
    while not check:
        mri_breast = ask_y_n_statement.ask_y_n("Has MRI-Breast been done?")
        if mri_breast:
            mri_breast = "MRI-Breast done"
            mri_breast_date = input("Date of examination of MRI: ")
            mri_breast_acc = input("Accession number of MR: ")
            fgt_mri = ask_y_n_statement.ask_option("Ammount of Fibroglandular Tissue", ["a. Almost entirely fat",
                      "b. Scattered fibroglandular tissue", "c. Heterogeneous fibroglandular tissue", "d. Extreme fibroglandular tissue", "Other"])
            bpe_level_mri = ask_y_n_statement.ask_option("Background parenchymal enhancement Level", ["Minimal", "Mild", "Moderate", "Marked", "Other"])
            bpe_symm_mri = ask_y_n_statement.ask_option("Background parenchymal enhancement Symmetry", ["Symmetric", "Asymmetric", "Other"])
            focus_mri = input("Details of Focus: ")
            mass_mri = ask_y_n_statement.ask_y_n("Are masses detected?")
            if mass_mri:
                mass_mri = "Mass Detected"
                table = "MRI_Multiple_Mass"
                mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal \
                    = radio_tables.multiple_mass(table, conn, cursor, file_number)
            else:
                mass_mri = "No Mass Detected"
                mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal = ("NA", )*6
            asso_feat = ["Nipple Retraction", "Nipple Invasion", "Skin Retraction", "Skin Thickening",
                        "Axillary adenopathy", "Pectoralis muscle invasion", "Chest wall invasion",
                         "Architectural Distortion"]
            asso_feat_data = []
            for index in (asso_feat):
                print("Associated feature: " + index)
                print("Detailed description can be added by choosing 'Other'")
                var = ask_y_n_statement.ask_option(index,
                                                   ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
                asso_feat_data.append(var)
            asso_feat_9 = ask_y_n_statement.ask_option("Associated Feature: Skin Invasion",
                                                       ["Direct invasion", "Inﬂammatory cancer", "Other"])
            asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, asso_feat_8\
                = asso_feat_data
            fat_lesions = ask_y_n_statement.ask_option("Fat Containing Lesions", ["Lymph nodes: Normal",
                    "Lymph nodes: Abnormal", "Fat necrosis", "Hamartoma", "Postoperative seroma", "hematoma with fat"])
            mri_breast_kinetics_initial = ask_y_n_statement.ask_option("Kinetic curve assessment Signal intensity "
                                        "(SI)/time curve description (Initial Phase)", ["Slow", "Medium", "Fast",
                                                                                        "Other"])
            mri_breast_kinetics_delayed = ask_y_n_statement.ask_option("Kinetic curve assessment Signal intensity "
                                        "(SI)/time curve description (Delayed Phase)", ["Persistent", "Plateau",
                                                                                        "Washout", "Other"])
            mri_breast_non_enhance = ask_y_n_statement.ask_option("Non-enhancing findings",
                                     ["Ductal precontrast high signal on T1W", "Cyst",
                                      "Postoperative collections (hematoma/seroma)",
                                      "Post-therapy skin thickening and trabecular thickening",
                                      "Non-enhancing mass", "Architectural distortion",
                                      "Signal void from foreign bodies, clips, etc.", "Other"])
            mri_breast_implant = input("Implant related findings: ")
            mri_breast_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                             ["Right Breast", "Left Breast", "Both", "Not present"])
            if mri_breast_lesion in {"Right Breast", "Left Breast", "Both"}:
                mri_breast_lesion_location = radio_tables.lesion_location(mri_breast_lesion)
                mri_breast_lesion_depth = input("Lesion depth: ")
            else:
                mri_breast_lesion_location, mri_breast_lesion_depth = ("NA",) * 2
            mri_breast_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            mri_breast_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            mri_breast_pect = input("Distance from Pectoralis Major (cm): ")
            mri_breast_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if mri_breast_birad:
                mri_breast_birad, mri_breast_birad_diag = radio_tables.birads()
            else:
                mri_breast_birad, mri_breast_birad_diag = ("NA",) * 2
        else:
            mri_breast = "MRI-Breast not done"
            mri_breast_date, mri_breast_acc, fgt_mri, bpe_level_mri, bpe_symm_mri, focus_mri, mass_mri, \
            mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal, asso_feat_1, asso_feat_2,\
            asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, asso_feat_8, asso_feat_9, fat_lesions, \
            mri_breast_lesion, mri_breast_lesion_location, mri_breast_lesion_depth, mri_breast_kinetics_initial, \
            mri_breast_kinetics_delayed, mri_breast_non_enhance, mri_breast_implant, mri_breast_size, mri_breast_dist, \
            mri_breast_pect, mri_breast_birad, mri_breast_birad_diag = ("NA", )*35
        data_list = [mri_breast, mri_breast_date, mri_breast_acc, fgt_mri, bpe_level_mri, bpe_symm_mri, focus_mri,
                     mass_mri, mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal,
                     asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7,
                     asso_feat_8, asso_feat_9, fat_lesions, mri_breast_kinetics_initial, mri_breast_kinetics_delayed,
                     mri_breast_non_enhance, mri_breast_implant, mri_breast_lesion, mri_breast_lesion_location,
                     mri_breast_lesion_depth, mri_breast_size, mri_breast_dist, mri_breast_pect,
                     mri_breast_birad, mri_breast_birad_diag]
        columns_list = pccm_names.name_clinical(module_name)
        check = add_update_sql.review_input(file_number,columns_list, data_list)
    return (tuple(data_list))

def add_data(conn, cursor, file_number):
    import add_update_sql
    from ask_y_n_statement import ask_y_n
    import pccm_names
    table = "Clinical_Exam"
    file_row(cursor, file_number)
    enter = ask_y_n("Enter Clinical Examination information")
    if enter:
        data = clinical_exam_initial(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("clinical_exam_initial"),
                                       file_number, data)
    enter = ask_y_n("Enter Nipple Cytology report?")
    if enter:
        data = nipple_cytology(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("nipple_cytology"), file_number,
                                       data)
    enter = ask_y_n("Enter Mammography Report?")
    if enter:
        data = mammography(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("mammography"), file_number, data)
    enter = ask_y_n("Enter 3D Tomosynthesis?")
    if enter:
        data = tomosynthesis(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("tomosynthesis"), file_number,
                                       data)
    enter = ask_y_n("Enter Automated Breast Volume Scanner")
    if enter:
        data = abvs(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("abvs"), file_number, data)
    enter = ask_y_n("Enter Sono-Mammography")
    if enter:
        data = sonomammo(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("sonomammo"), file_number, data)
    enter = ask_y_n("Enter MRI-Breast")
    if enter:
        data = mri_breast(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.name_clinical("mri_breast"), file_number, data)

def edit_data(conn, cursor, file_number):
    import add_update_sql
    import pccm_names as colname
    table = "Clinical_Exam"
    print("Initial Clinical Examination")
    col_list = colname.name_clinical("clinical_exam_initial")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = clinical_exam_initial(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Nipple Cytology")
    col_list = colname.name_clinical("nipple_cytology")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = nipple_cytology(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Mammography")
    col_list = colname.name_clinical("mammography")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = mammography(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("3D-Tomosynthesis")
    col_list = colname.name_clinical("tomosynthesis")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = tomosynthesis(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Automated Breast Volume Scan")
    col_list = colname.name_clinical("abvs")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = abvs(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Sono-Mammography")
    col_list = colname.name_clinical("sonomammo")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = sonomammo(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("MRI Breast")
    col_list = colname.name_clinical("mri_breast")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = mri_breast(conn, cursor, file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)

