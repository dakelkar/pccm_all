def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Clinical_Exam(File_number) VALUES ('" + file_number + "')")

def clinical_exam_initial (file_number):
    import ask_y_n_statement
    import add_update_sql
    import  pccm_names
    module_name = "clinical_exam_initial"
    check = False
    while not check:
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
            lump_location_data = "Lump" + lump_location
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

        data_list = [prov_diag, lump_palp, lump_location_data, lump_size, lump_number, lump_consistency, lump_fixity, \
               mastitis_location_data, mastitis_type, tender, retract, discharge, discharge_type, skin_change_location, \
               skin_change_type, ax_nodes, ax_nodes_number, ax_nodes_size, ax_nodes_fixity, supra_nodes, supra_nodes_number, \
               supra_nodes_size, supra_nodes_fixity, contra_breast, arm_edema, arm_circ_right, arm_volume_right, \
               arm_elbow_right, arm_circ_left, arm_volume_left, arm_elbow_left]

        columns_list = pccm_names.names_clinical(module_name)
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
        columns_list = pccm_names.names_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def mammography (file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
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
        else:
            mammo = "Mammography diagnosis not done"
            mammo_diag_date, mammo_diag_acc = "NA", "NA"
        breast_density = ask_y_n_statement.ask_option("Density of breast", ["A: fatty", "B: scattered fibroglandular", "C: heterogeneously dense", "D: dense"])
        mammo_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                             ["Right Breast", "Left Breast", "Both", "Not present"])
        mammo_lesion_data = []
        if mammo_lesion == "Right Breast" or mammo_lesion == "Both":
            category = "Lesion location on Right Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            mammo_lesion_rb = ask_y_n_statement.ask_option(category, options)
            mammo_lesion_rb_data = "RB-" + mammo_lesion_rb
            mammo_lesion_data.append(mammo_lesion_rb_data)
        if mammo_lesion == "Left Breast" or mammo_lesion == "Both":
            category = "Lesion location on Left Breast"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            mammo_lesion_lb = ask_y_n_statement.ask_option(category, options)
            mammo_lesion_lb_data = "LB-" + mammo_lesion_lb
            mammo_lesion_data.append(mammo_lesion_lb_data)
        mammo_lesion_data = "; ".join(mammo_lesion_data)
        if mammo_lesion == "Not present":
            mammo_lesion_data = "Lesion" + mammo_lesion
        mammo_shape = ask_y_n_statement.ask_option("Shape", ["Oval", "Round", "Irregular", "Other"])
        mammo_size = ask_y_n_statement.ask_option("Size of mass", ["<2 cm", "2-5 cm", ">5cm"])
        mammo_margin = ask_y_n_statement.ask_option("Margins", ["Circumscribed", "Obscured", "Indistinct", "Spiculated", "Other"])
        mammo_density = ask_y_n_statement.ask_option("Density", ["High Density", "Equal Density", "Low Density",
                                                                "Fat-containing", "Other"])
        mammo_calcification = ask_y_n_statement.ask_option("Calcification Type", ["Skin", "Vascular",
        "Coarse or 'Popcorn-like'", "Large Rod-like", "Round and punctate", "Lucent-Centered", "Eggshell or Rim",
        "Milk of Calcium", "Suture", "Dystrophic", "Amorphous", "Coarse Heterogeneous", "Fine Pleomorphic",
                                                "Fine Linear or Fine Linear Branching", "Other"])
        if mammo_calcification in {"Skin", "Vascular", "Coarse or 'Popcorn-like'", "Large Rod-like", "Round and punctate",
                                   "Eggshell or Rim","Dystrophic"}:
            mammo_calcification_type = "Typically Benign"
            print (mammo_calcification_type)
        elif mammo_calcification in {"Milk of Calcium", "Suture","Amorphous", "Coarse Heterogeneous", "Fine Pleomorphic",
                                                "Fine Linear or Fine Linear Branching"}:
            mammo_calcification_type = "Suspicious Morphology"
            print("Implication of calcification Type is "+ mammo_calcification_type)
        else:
            mammo_calcification_type = input ("Implication of calcification type "+ mammo_calcification)
        mammo_calcification_dist = ask_y_n_statement.ask_option("Calcification distribution", ["Diffuse", "Regional",
                                                                                        "Grouped", "Linear", "Segmental", "Other"])
        mammo_arch = ask_y_n_statement.ask_option("Architectural distortion of mass", ["Right", "Left", "Both", "Not present"])
        mammo_asymm = ask_y_n_statement.ask_option("Asymmetry of mass", ["Global", "Focal", "Developing", "Not present", "Other"])
        mammo_intra = ask_y_n_statement.ask_option("Intra mammary lymph nodes", ["Right", "Left", "Both", "Other"])
        mammo_lesion_skin = ask_y_n_statement.ask_option("Skin Lesion",["Right", "Left", "Both", "Other"] )
        mammo_dil = ask_y_n_statement.ask_option("Solitary Dilated duct",["Right", "Left", "Both", "Other"])
        asso_feat = ["Skin Retraction", "Nipple Retraction", "Skin Thickening", "Trabecular Thickening",
                     "Axillary lymphadenopathy", "Architectural Distortion", "Calcification"]
        asso_feat_data = []
        for index in (asso_feat):
            print ("Associated feature "+index+ " in rest of breast")
            var = ask_y_n_statement.ask_option(index, ["Right", "Left", "Both", "Other"])
            asso_feat_data.append(var)
        asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7 = asso_feat_data
        mammo_sec = input ("Secondary Lesion/Contralateral Lesion: ")
        mammo_dist = ask_y_n_statement.ask_option("Distance from Skin", ["<0.5 cm", ">0.5 cm"])
        mammmo_pect = input ("Distance from Pectoralis Major (cm): ")
        mammo_birads = ask_y_n_statement.ask_option("BI-RADS", ["0", "I", "II", "III", "IV", "IVA", "IVB","IVC" "V"])

        data_list = [mammo_loc, mammo_details, mammo_date, mammo_number, mammo_rep_previous, mammo, mammo_diag_date,
                     mammo_diag_acc, breast_density, mammo_lesion, mammo_lesion_data, mammo_shape, mammo_size,
                     mammo_margin, mammo_density, mammo_calcification, mammo_calcification_type,
                     mammo_calcification_dist, mammo_arch, mammo_asymm, mammo_intra, mammo_lesion_skin, mammo_dil,
                     asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7,
                     mammo_sec, mammo_dist, mammmo_pect,  mammo_birads]
        columns_list = pccm_names.names_clinical(module_name)
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
            tomo_acc = input("Accession number of Tomosynthesis")
            tomo_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            tomo_lesion_data = []
            if tomo_lesion == "Right Breast" or tomo_lesion == "Both":
                category = "Lesion location on Right Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                tomo_lesion_rb = ask_y_n_statement.ask_option(category, options)
                tomo_lesion_rb_data = "RB-" + tomo_lesion_rb
                tomo_lesion_data.append(tomo_lesion_rb_data)
            if tomo_lesion == "Left Breast" or tomo_lesion == "Both":
                category = "Lesion location on Left Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                tomo_lesion_lb = ask_y_n_statement.ask_option(category, options)
                tomo_lesion_lb_data = "LB-" + tomo_lesion_lb
                tomo_lesion_data.append(tomo_lesion_lb_data)
            if tomo_lesion == "Not present":
                tomo_lesion_data = "Lesion" + tomo_lesion
            else:
                tomo_lesion_data = "; ".join(tomo_lesion_data)
            tomo_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm"])
            tomo_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm"])
            tomo_pect = input("Distance from Pectoralis Major (cm): ")
            tomo_diagnosis = ask_y_n_statement.ask_option("Tomosynthesis Diagnosis", ["Normal", "Benign", "Suspicious",
                                                                                      "Diagnostic for Cancer"])
        else:
            tomo = "3D digital Tomosynthesis not done"
            tomo_date, tomo_acc, tomo_lesion, tomo_lesion_data, tomo_size, tomo_dist, tomo_pect, tomo_diagnosis = ("NA", )*8

        data_list = [tomo, tomo_date, tomo_acc, tomo_lesion_data, tomo_size, tomo_dist, tomo_pect, tomo_diagnosis]
        columns_list = pccm_names.names_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def abvs (file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    module_name = "abvs"
    check = False
    while not check:
        abvs = ask_y_n_statement.ask_y_n("Automated Breast Volume Scanner (ABVS) done?")
        if abvs:
            abvs = "Automated Breast Volume Scanner done"
            abvs_date = input("Date of examination of ABVS: ")
            abvs_acc = input("Accession number of ABVS")
            abvs_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            abvs_lesion_data = []
            if abvs_lesion == "Right Breast" or abvs_lesion == "Both":
                category = "Lesion location on Right Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                abvs_lesion_rb = ask_y_n_statement.ask_option(category, options)
                abvs_lesion_rb_data = "RB-" + abvs_lesion_rb
                abvs_lesion_data.append(abvs_lesion_rb_data)
            if abvs_lesion == "Left Breast" or abvs_lesion == "Both":
                category = "Lesion location on Left Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                abvs_lesion_lb = ask_y_n_statement.ask_option(category, options)
                abvs_lesion_lb_data = "LB-" + abvs_lesion_lb
                abvs_lesion_data.append(abvs_lesion_lb_data)
            if abvs_lesion == "Not present":
                abvs_lesion_data = "Lesion" + abvs_lesion
            else:
                abvs_lesion_data = "; ".join(abvs_lesion_data)
            abvs_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            abvs_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            abvs_pect = input("Distance from Pectoralis Major (cm): ")
            abvs_diagnosis = ask_y_n_statement.ask_option("ABVS Diagnosis", ["Normal", "Benign", "Suspicious",
                                                                                      "Diagnostic for Cancer"])
        else:
            abvs = "Automated Breast Volume Scanner done"
            abvs_date, abvs_acc, abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect, abvs_diagnosis = ("NA", )*8

        data_list = [abvs, abvs_date, abvs_acc,abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect, abvs_diagnosis]
        columns_list = pccm_names.names_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def sonomammo (file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    module_name = "sonomammo"
    check = False
    while not check:
        sonomammo = ask_y_n_statement.ask_y_n("Sono-Mammography done?")
        if sonomammo:
            sonomammo = "Sono-Mammography done"
            sonomammo_date = input("Date of examination of Sono-mammography: ")
            sonomammo_acc = input("Accession number of Sono-Mammography")
            sonomammo_lesion_number = input("Number of lesions: ")
            sonomammo_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            sonomammo_lesion_data = []
            if sonomammo_lesion == "Right Breast" or sonomammo_lesion == "Both":
                category = "Lesion location on Right Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                sonomammo_lesion_rb = ask_y_n_statement.ask_option(category, options)
                sonomammo_lesion_rb_data = "RB-" + sonomammo_lesion_rb
                sonomammo_lesion_data.append(sonomammo_lesion_rb_data)
            if sonomammo_lesion == "Left Breast" or sonomammo_lesion == "Both":
                category = "Lesion location on Left Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                sonomammo_lesion_lb = ask_y_n_statement.ask_option(category, options)
                sonomammo_lesion_lb_data = "LB-" + sonomammo_lesion_lb
                sonomammo_lesion_data.append(sonomammo_lesion_lb_data)
            if sonomammo_lesion == "Not present":
                sonomammo_lesion_data = "Lesion" + sonomammo_lesion
            else:
                sonomammo_lesion_data = "; ".join(sonomammo_lesion_data)
            sonomammo_shape = ask_y_n_statement.ask_option("Shape of lesion: ", ["Oval", "Round", "Irregular", "Other"])
            sonomammo_size =  ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            sonomammo_orientation = ask_y_n_statement.ask_option("Orientation of lesion", ["Parallel", "Non-parallel"])
            sonomammo_margins = ask_y_n_statement.ask_option("Margins of lesion", ["Circumscribed", "Not Circumscribed",
                                                                "Indistinct", "Angular", "Microlobulated", "Spiculated", "Other"])
            sonomammo_echo = ask_y_n_statement.ask_option("Echo pattern of lesion", ["Hypoechoic", "Hyperechoic",
                                                                    "Isoechoic", "Complex", "Heterogenous", "Other"])
            sonomammo_postacoustic  = ask_y_n_statement.ask_option("Post-Acoustic Features of lesion", ["No Post Features", "Enhancement", "Shadowing", "Combined pattern", "Other"])
            sonomammo_calc = ask_y_n_statement.ask_option("Calcification", ["In mass", "Outside", "Intraductal", "Other"])
            sonomammo_arch = ask_y_n_statement.ask_option("Architectural distortion of lesion",
                                                      ["Right", "Left", "Both", "Not present"])
            other_feat = ["Skin Changes", "Edema", "Vascularity", "Lymph nodes"]
            other_feat_data = []
            for index in (other_feat):
                var = ask_y_n_statement.ask_option(index, ["Right", "Left", "Both", "Other"])
                other_feat_data.append(var)
            sonomammo_skin, sonomammo_edema, sonomammo_vasc, sonomammo_lymph = other_feat_data
            sonomammo_dist_nipple = ask_y_n_statement.ask_option("Distance from Nipple", ["<0.5cm", ">0.5cm", "Other"])
            sonomammo_dist_skin = ask_y_n_statement.ask_option("Distance from Nipple", ["<0.5cm", ">0.5cm", "Other"])
            sonomammo_pect = input("Distance from Pectoralis Major (cm): ")
            sonomammo_diag = ask_y_n_statement.ask_option("Diagnosis of Sono-Mammography", ["Normal", "Duct actasia",
                                                                                "Intra ductal pailloma", "Papillomatosis"])
        else:
            sonomammo = "Sono-Mammography not done"
            sonomammo_date, sonomammo_acc, sonomammo_lesion_number, sonomammo_lesion, sonomammo_lesion_data, sonomammo_shape ,sonomammo_size ,\
            sonomammo_orientation,sonomammo_margins,sonomammo_echo,sonomammo_postacoustic,sonomammo_calc, sonomammo_arch,\
            sonomammo_skin, sonomammo_edema, sonomammo_vasc, sonomammo_lymph, sonomammo_dist_nipple, sonomammo_dist_skin,\
            sonomammo_pect ,sonomammo_diag = ("NA", )*21
        data_list = [sonomammo, sonomammo_date, sonomammo_acc, sonomammo_lesion_number, sonomammo_lesion, \
                    sonomammo_lesion_data, sonomammo_shape ,sonomammo_size,sonomammo_orientation, sonomammo_margins,\
                    sonomammo_echo, sonomammo_postacoustic,sonomammo_calc, sonomammo_arch,sonomammo_skin, \
                    sonomammo_edema, sonomammo_vasc, sonomammo_lymph, sonomammo_dist_nipple, sonomammo_dist_skin, \
                    sonomammo_pect ,sonomammo_diag]
        columns_list = pccm_names.names_clinical(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def mri_breast_axilla (file_number):
    import ask_y_n_statement
    import add_update_sql
    import pccm_names
    module_name = "mri_breast_axilla"
    check = False
    while not check:
        mri_breast = ask_y_n_statement.ask_y_n("MRI-Breast and Axilla done?")
        if mri_breast:
            mri_breast = "MRI-Breast and Axilla done"
            mri_breast_date = input("Date of examination of Sono-mammography: ")
            mri_breast_acc = input("Accession number of Sono-Mammography")
            mri_breast_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            mri_breast_lesion_data = []
            if mri_breast_lesion == "Right Breast" or mri_breast_lesion == "Both":
                category = "Lesion location on Right Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                mri_breast_lesion_rb = ask_y_n_statement.ask_option(category, options)
                mri_breast_lesion_rb_data = "RB-" + mri_breast_lesion_rb
                mri_breast_lesion_data.append(mri_breast_lesion_rb_data)
            if mri_breast_lesion == "Left Breast" or mri_breast_lesion == "Both":
                category = "Lesion location on Left Breast"
                options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
                mri_breast_lesion_lb = ask_y_n_statement.ask_option(category, options)
                mri_breast_lesion_lb_data = "LB-" + mri_breast_lesion_lb
                mri_breast_lesion_data.append(mri_breast_lesion_lb_data)
            if mri_breast_lesion == "Not present":
                mri_breast_lesion_data = "Lesion" + mri_breast_lesion
            else:
                mri_breast_lesion_data = "; ".join(mri_breast_lesion_data)
            mri_breast_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            mri_breast_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            mri_breast_pect = input("Distance from Pectoralis Major (cm): ")
            mri_breast_diagnosis = ask_y_n_statement.ask_option("MRI Breast and Axilla Diagnosis", ["Normal", "Benign", "Suspicious",
                                                                             "Diagnostic for Cancer"])
        else:
            mri_breast = "MRI-Breast and Axilla not done"
            mri_breast_date , mri_breast_acc, mri_breast_lesion, mri_breast_lesion_data, \
            mri_breast_size, mri_breast_dist, mri_breast_pect, mri_breast_diagnosis = ("NA", )*8
        data_list = [mri_breast, mri_breast_date , mri_breast_acc, mri_breast_lesion, mri_breast_lesion_data, \
            mri_breast_size, mri_breast_dist, mri_breast_pect, mri_breast_diagnosis]
        columns_list = pccm_names.names_clinical(module_name)
        check = add_update_sql.review_input(file_number,columns_list, data_list)
    return (tuple(data_list))

