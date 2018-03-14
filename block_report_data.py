def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Block_Report_Data(File_number) VALUES ('" + file_number + "')")

def block_report_info (file_number):
    from add_update_sql import review_input
    from ask_y_n_statement import ask_option, ask_y_n
    import  pccm_names
    module_name = "block_report_info"
    check = False
    while not check:
        con_stat = ask_y_n("Has consent been taken from patient?", "Consent Taken", "No Consent")
        if con_stat == "Consent Taken":
            con_form = ask_y_n("Is consent form with signature present in file ?",
                                                 "Consent form with signature present in folder",
                                                 "Completed consent form not present in folder")
        else:
            con_form = "NA"
        block_sr = input("Block Serial Number: ")
        block_id = input ("Biopsy Block ID: ")
        block_number = input("Number of blocks: ")
        block_date = input("Date of Biopsy: ")
        lab_id = input("Lab ID: ")
        category = "Biopsy Type"
        options = ["Direct", "USG Guided", "VAB", "True-cut", "Steriotactic", "Other"]
        biopsy_type= ask_option(category, options)
        data_list = [con_stat,con_form,block_sr, block_id, block_number, block_date, lab_id,biopsy_type]
        columns_list = pccm_names.names_block(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def tumour_biopsy_data(file_number):
    from ask_y_n_statement import ask_option
    from add_update_sql import review_input
    import pccm_names
    module_name = "tumour_biopsy_data"
    check = False
    while not check:
        category = "Tumour biopsy diagnosis"
        options = ['Benign', "Ductal carcinoma in situ(DCIS) with microinvasion",
                   "Ductal carcinoma in situ(DCIS) without microinvasion", "Lobular Carcinoma in Situ (LCS)",
                   "Invasive Ductal Carcinoma (IDC)", "Invasive Lobular Carcinoma (ILC)", "Granulamatous Mastitis",
                   "Papillary Carcinoma", "Phylloid Carcinoma", "Invasive Mammary Carcinoma",
                   "Invasive Breast Carcinoma", "Other"]
        tumour_diagnosis = ask_option(category, options)
        tumour_grade = ask_option("Tumour Biopsy Diagnosis", ["Grade 1", "Grade 2", "Grade 3", "Other"])
        tumour_er= ask_option("ER Status", ["Positive", "Negative"])
        if (tumour_er == "Positive"):
            tumour_er_percent = input ("ER Percent: ")
        else:
            tumour_er_percent = "NA"
        tumour_pr = ask_option("PR Status", ["Positive", "Negative"])
        if (tumour_pr == "Positive"):
            tumour_pr_percent = input ("PR Percent: ")
        else:
            tumour_pr_percent = "NA"
        tumour_her2 = ask_option("HER2 Status", ["Positive", "Equivocal", "Negative"])
        if tumour_her2 == "Negative":
            tumour_her2_grade, tumour_fish = ("NA", )*2
        else:
            tumour_her2_grade = input ("HER2 Grade: ")
            tumour_fish = ask_option("FISH", ["Positive", "Negative"])
        tumour_ki67 = input("Ki67 Percent: ")
        data_list = [tumour_diagnosis, tumour_grade, tumour_er ,tumour_er_percent ,tumour_pr, tumour_pr_percent,
                     tumour_her2, tumour_her2_grade, tumour_fish, tumour_ki67]
        columns_list = pccm_names.names_block(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def lymphnode_biopsy(file_number):
    from ask_y_n_statement import ask_option
    from add_update_sql import review_input
    import pccm_names
    module_name = "lymphnode_biopsy"
    check = False
    while not check:
        fnac = ask_option("Lymph Node biopsy FNAC", ["Done", "Not Done"])
        if fnac == "Done":
            fnac_location = ask_option("Lymph Node biopsy location",  ["Right", "Left", "Both"])
            fnac_diagnosis = ask_option("Lymph Node biopsy diagnosis", ["Normal", "Benign", "Malignant", "Other"])
        else:
            fnac_location, fnac_diagnosis = ("NA", )*2
        data_list = [fnac, fnac_location, fnac_diagnosis]
        columns_list = pccm_names.names_block(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def surgery_info (file_number):
    from ask_y_n_statement import ask_option, ask_y_n
    from add_update_sql import review_input
    import pccm_names
    module_name = "surgery_info"
    check = False
    while not check:
        surg_block_id = input("Surgical Block ID: ")
        surg_location = input ("Location of surgery block id "+ surg_block_id)
        surg_no_block = input("Number of Blocks: ")
        surg_block_source = input ("Surgery Block Source: ")
        surg_tumour_block = input ("Tumour Block Reference: ")
        surg_node_block = input ("Nodes Block Reference: ")
        surg_normal_block = input ("Adjacent Normal Block Reference: ")
        surg_red_block = input ("Reduction Tissue Block Reference: ")
        surg_date = input ("Date of Surgery: ")
        surg_name = input ("Name of surgeon: ")
        surg_hosp_id = input ("Hospital ID: ")
        lesion_side = ()
        lesion_side_rb_y_n = ask_y_n ("Lesion Side RB")
        if lesion_side_rb_y_n:
            category = "Lesion Side RB"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            lesion_side_rb = ask_option(category, options)
            lesion_side_rb_data = "RB-"+lesion_side_rb
        lesion_side_lb_y_n = ask_y_n("Lesion Side LB")
        if lesion_side_lb_y_n:
            category = "Lesion Side LB"
            options = ["UOQ", "UIQ", "C", "UCQ", "LCQ", "LOQ", "LIQ"]
            lesion_side_lb = ask_option(category, options)
            lesion_side_lb_data = "LB-" + lesion_side_lb
        if lesion_side_rb_y_n and lesion_side_lb_y_n:
            lesion_side = lesion_side_rb_data + "; " + lesion_side_lb_data
        elif lesion_side_rb_y_n:
            lesion_side = lesion_side_rb_data
        elif lesion_side_lb_y_n:
            lesion_side = lesion_side_lb_data
        print("Lesion side "+ lesion_side)
        surg_type = ask_option ("Type Surgery", ["Reconstruction", "Breast Conservation Surgery (BCS)", "Therapeutic Mammoplasty",
                   "Reduction Mammoplasty", "Wide Local Excision", "Other"])
        if surg_type == "Reconstruction":
            surg_type = ask_option("Type Reconstruction", ["Mastectomy/Modified Radical Mastectomy", "Implant"])
        surg_response = ask_option("Response to Surgery", ["Complete_Remission/No Residual Tumor", "Progressing", "Partial", "Static", "Other"])
        data_list = [surg_block_id, surg_location, surg_no_block, surg_block_source, surg_tumour_block, surg_node_block,
                     surg_normal_block, surg_red_block, surg_date, surg_name, surg_hosp_id, lesion_side, surg_type,
                     surg_response]
        columns_list = pccm_names.names_block(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def surgery_block (file_number):
    from ask_y_n_statement import ask_option, ask_y_n
    from add_update_sql import review_input
    import  pccm_names
    module_name = "surgery_block"
    check = False
    while not check:
        print ("Surgery Block Report")
        tumour_size = input ("Tumour size: ")
        tumour_grade = ask_option("Tumour Grade", ["I", "II", "III", "Other"])
        surg_diag = ask_option("Surgery Diagnosis", ["Ductal carcinoma in situ(DCIS)", "Invasive Ductal Carcinoma", "Other"])
        if (surg_diag == "Ductal carcinoma in situ(DCIS)"):
            dcis_percent = input ("Percent DCIS: ")
            dcis_invasion = ask_option("DCIS Invasion", ['Microinvasion', 'Macroinvasion'])
        else:
            dcis_percent, dcis_invasion = ("NA", )*2
        per_inv = ask_y_n("Perineural Invasion", "Perineural Invasion Present", "Perineural Invasion Absent")
        necrosis = ask_y_n("Necrosis", "Necrosis Present", "Necrosis Absent")
        lymph_invasion = ask_y_n("Lymphovascular invasion", "Lymphovascular invasion Present",
                                 "Lymphovascular invasion Absent")
        margin = ask_option("Margins", ["Involved", "Free"])
        print ("Surgery Block Report")
        report = ask_option("Pathological Complete Remission",["Yes", "No", "Other"])
        data_list = [tumour_size,tumour_grade,surg_diag,dcis_percent,dcis_invasion,per_inv,necrosis,
                     lymph_invasion,margin, report]
        columns_list = pccm_names.names_block(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def node_block (file_number):
    from ask_y_n_statement import ask_option, ask_y_n
    from add_update_sql import review_input
    import pccm_names
    module_name = "node_block"
    check = False
    while not check:
        sent_data = node_details("Sentinel")
        sentinel, sent_number_rem, sent_number_pos, sent_number = sent_data
        print ("Sentinel Node "+ sent_number)
        ax_data = node_details("Axillary")
        ax, ax_number_rem, ax_number_pos, ax_number = ax_data
        print("Axillary Node " + ax_number)
        ap_data = node_details("Apical")
        ap, ap_number_rem, ap_number_pos, ap_number = ap_data
        print("Apical Node " + ap_number)
        per_spread = ask_y_n("Perinodal Spread", "Perinodal Spread", "No Perinodal Spread")
        supra_inv = ask_y_n("Supraclavicular Node Involvment", "Supraclavicular Node Involved", "No Supraclavicular Node Involvment")
        data_list = [sentinel, sent_number_rem, sent_number_pos, sent_number, ax, ax_number_rem,
                     ax_number_pos, ax_number, ap, ap_number_rem, ap_number_pos, ap_number, per_spread, supra_inv]
        columns_list = pccm_names.names_block(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))


def node_details (node_name):
    node_name + " Node"
    number_removed = input("Number of "+node_name+" Nodes removed: ")
    number_positive = input("Number of "+node_name+" Nodes positive: ")
    if int(number_positive)>0:
        node = "Positive"
    else:
        node = "Negative"
    number = "("+number_positive + "/" + number_removed+")"
    data = [node, number_removed, number_positive, number]
    return data

def path_stage(file_number):
    from add_update_sql import review_input
    from ask_y_n_statement import ask_option, ask_y_n
    import pccm_names
    module_name = "path_stage"
    check = False
    while not check:
        category = "pT"
        options = ["is", "0", "1", "2", "3", "4", "Other"]
        pT = ask_option(category, options)
        category = "pN"
        options = ["0", "1", "2", "3", "4", "Other"]
        pN = ask_option(category, options)
        category = ("M")
        options = ["0", "x", "1", "Present", "Other"]
        M = ask_option(category, options)
        path_stage = "pT" + pT + "N" + pN + "M" + M
        print ("Pathological Stage: "+ path_stage)
        check = ask_y_n("Is pathological stage correct")
        if not check:
            path_stage = input("Please enter correct pathological stage: ")
        if M == "1":
            clinical_stage = "IV"
        elif M == "0":
            if pN == "3":
                clinical_stage = "IIIC"
            elif pN == "2":
                if pT == "4":
                    clinical_stage = "IIIB"
                else:
                    clinical_stage = "IIIA"
            elif pN == "1mi":
                clinical_stage = "IB"
            elif pN == "1":
                if (pT=="0" or pT == "1"):
                    clinical_stage = "IIA"
                elif pT=="2":
                    clinical_stage = "IIB"
                elif pT == "3":
                    clinical_stage = "IIIA"
                elif pT =="4":
                    clinical_stage = "IIIC"
                else:
                    clinical_stage = input("Clinical Staging: ")
            elif pN =="0":
                if pT =="is":
                    clinical_stage = "0"
                elif pT == "1":
                    clinical_stage = "IA"
                elif pT =="2":
                    clinical_stage = "IIA"
                elif pT == "3":
                    clinical_stage = "IIB"
                elif pT == "4":
                    clinical_stage = "IIIB"
                else:
                    clinical_stage = input("Clinical Staging: ")
        else:
            clinical_stage = input("Clinical Staging: ")
        print ("Clinical stage "+ clinical_stage)
        print ("Based on TNM status", path_stage, "and Anatomic stage/prognostic groups table at"
                                                  "https://emedicine.medscape.com/article/2007112-overview")
        check = ask_y_n("Is clinical stage correct")
        if not check:
            clinical_stage = input("Please enter correct clinical stage: ")
        data_list = [pT, pN, M, path_stage, clinical_stage]
        columns_list = pccm_names.names_block(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))
