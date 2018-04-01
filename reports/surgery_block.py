def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Surgery_Block_Report_Data(File_number) VALUES ('" + file_number + "')")

def surgery_block_information_1(file_number):
    from sql.add_update_sql import review_input
    from modules.ask_y_n_statement import ask_option, ask_y_n
    import modules.pccm_names as pccm_names
    from tables.radio_tables import lesion_location
    module_name = "surgery_block_information_1"
    check = False
    while not check:
        con_stat = ask_y_n("Has consent been taken from patient?", "Consent Taken", "No Consent")
        if con_stat == "Consent Taken":
            con_form = ask_y_n("Is consent form with signature present in file ?",
                               "Consent form with signature present in folder",
                               "Completed consent form not present in folder")
        else:
            con_form = "NA"
        block_sr = input("Surgery Block Serial Number: ")
        print ("Surgery Block Location")
        location = False
        while location == False:
            print ("Biopsy Block Location: ")
            block_cab = input ("Cabinet No: " )
            block_drawer = input ("Drawer Number: ")
            block_col = input ("Column Number: ")
            block_pos = ask_option("Is Block in", ["Front", "Back"])
            block_location = block_cab+"-"+block_drawer+"-"+block_col+"-"+block_pos
            print ("Block location is "+ block_location)
            location = ask_y_n("Is this correct?")
        block_current = input ("What is the current location of block? ")
        surg_block_id = input("Surgical Block ID: ")
        surg_location = input("Location of surgery block id " + surg_block_id + ": ")
        surg_no_block = input("Number of Blocks: ")
        surg_block_source = input("Pathology Lab (source of block): ")
        surg_tumour_block = input("Tumour Block Reference: ")
        surg_node_block = input("Nodes Block Reference: ")
        surg_normal_block = input("Adjacent Normal Block Reference: ")
        surg_red_block = input("Reduction Tissue Block Reference: ")
        surg_date = input("Date of Surgery: ")
        surg_name = input("Name of surgeon: ")
        surg_hosp_id = input("Hospital ID: ")
        lesion_side = ask_option("Lesion on", ["Right Breast", "Left Breast", "Both"])
        lesion_side_data = lesion_location(lesion_side)
        nact = ask_y_n("Did the patient undergo NACT?", "NACT done", "No NACT")
        surg_type = ask_option("Type Surgery",
                               ["Reconstruction", "Breast Conservation Surgery (BCS)", "Therapeutic Mammoplasty",
                                "Reduction Mammoplasty", "Wide Local Excision", "Other"])
        if surg_type == "Reconstruction":
            surg_type = ask_option("Type Reconstruction", ["Mastectomy/Modified Radical Mastectomy",
                                                                             "Implant"])
        data_list = [con_stat, con_form, block_sr, block_location, block_current, surg_block_id, surg_location,
                     surg_no_block, surg_block_source, surg_tumour_block, surg_node_block, surg_normal_block,
                     surg_red_block, surg_date, surg_name, surg_hosp_id, lesion_side_data, nact, surg_type]
        columns_list = pccm_names.names_surgery(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def surgery_block_information_2 (file_number):
    from modules.ask_y_n_statement import ask_option, ask_y_n
    from sql.add_update_sql import review_input
    import modules.pccm_names as pccm_names
    module_name = "surgery_block_information_2"
    check = False
    while not check:
        tumour_size = input("Tumour size: ")
        tumour_grade = ask_option("Tumour Grade", ["I", "II", "III", "Other"])
        surg_diag = ask_option("Surgery Diagnosis",
                               ["Ductal carcinoma in situ(DCIS)", "Invasive Ductal Carcinoma", "Other"])
        if (surg_diag == "Ductal carcinoma in situ(DCIS)"):
            dcis_percent = input("Percent DCIS: ")
            dcis_invasion = ask_option("DCIS Invasion", ['Microinvasion', 'Macroinvasion'])
        else:
            dcis_percent, dcis_invasion = ("NA",) * 2
        per_inv = ask_y_n("Perineural Invasion", "Perineural Invasion Present", "Perineural Invasion Absent")
        necrosis = ask_y_n("Necrosis", "Necrosis Present", "Necrosis Absent")
        lymph_invasion = ask_y_n("Lymphovascular invasion", "Lymphovascular invasion Present",
                                 "Lymphovascular invasion Absent")
        margin = ask_option("Margins", ["Involved", "Free"])
        print("Surgery Block Report")
        report = ask_option("Pathological Complete Remission", ["Yes", "No", "Other"])
        data_list = [tumour_size, tumour_grade, surg_diag, dcis_percent, dcis_invasion, per_inv, necrosis,
                     lymph_invasion, margin, report]
        columns_list = pccm_names.names_surgery(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def surgery_block_information_3 (file_number):
    from modules.ask_y_n_statement import ask_y_n
    from sql.add_update_sql import review_input
    import modules.pccm_names as pccm_names
    module_name = "surgery_block_information_3"
    check = False
    while not check:
        sent_data = node_details("Sentinel")
        sentinel, sent_number_rem, sent_number_pos, sent_number = sent_data
        ax_data = node_details("Axillary")
        ax, ax_number_rem, ax_number_pos, ax_number = ax_data
        print("Axillary Node LNR: " + ax_number)
        ap_data = node_details("Apical")
        ap, ap_number_rem, ap_number_pos, ap_number = ap_data
        per_spread = ask_y_n("Perinodal Spread", "Perinodal Spread", "No Perinodal Spread")
        supra_inv = ask_y_n("Supraclavicular Node Involvment", "Supraclavicular Node Involved", "No Supraclavicular Node Involvment")
        data_list = [sentinel, sent_number_rem, sent_number_pos, ax, ax_number_rem,
                     ax_number_pos, ax_number, ap, ap_number_rem, ap_number_pos, per_spread, supra_inv]
        columns_list = pccm_names.names_surgery(module_name)
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
    from modules.ask_y_n_statement import ask_option, ask_y_n
    from sql.add_update_sql import review_input
    import modules.pccm_names as pccm_names
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
        columns_list = pccm_names.names_surgery(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def add_data(conn, cursor, file_number):
    from modules.ask_y_n_statement import ask_y_n
    import sql.add_update_sql as add_update_sql
    import modules.pccm_names as pccm_names
    table = "Surgery_Block_Report_Data"
    file_row(cursor, file_number)
    enter = ask_y_n("Enter Surgery Block information?")
    if enter:
        data = surgery_block_information_1(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("surgery_block_information_1"), file_number, data)
    enter = ask_y_n("Enter Surgery Block information (Tumour Details) ?")
    if enter:
        data = surgery_block_information_2(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("surgery_block_information_2"), file_number, data)
    enter = ask_y_n("Enter Surgery Block information (Node Details)?")
    if enter:
        data = surgery_block_information_3(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("surgery_block_information_3"), file_number, data)
    enter = ask_y_n("Enter Pathological Stage?")
    if enter:
        data = path_stage(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_surgery("path_stage"), file_number, data)

