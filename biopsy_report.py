def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Biopsy_Report_Data(File_number) VALUES ('" + file_number + "')")

def biopsy_report_info(file_number):
    from add_update_sql import review_input
    import ask_y_n_statement
    import pccm_names
    module_name = "biopsy_report_info"
    check = False
    while not check:
        con_stat = ask_y_n_statement.ask_y_n("Has consent been taken from patient?", "Consent Taken", "No Consent")
        if con_stat == "Consent Taken":
            con_form = ask_y_n_statement.ask_y_n("Is consent form with signature present in file ?",
                               "Consent form with signature present in folder",
                               "Completed consent form not present in folder")
        else:
            con_form = "NA"
        block_sr = input("Biopsy Block Serial Number: ")
        location = False
        while location == False:
            print ("Biopsy Block Location: ")
            block_cab = input ("Cabinet No: " )
            block_drawer = input ("Drawer Number: ")
            block_col = input ("Column Number: ")
            block_pos = ask_y_n_statement.ask_option("Is Block in", ["Front", "Back"])
            block_location = block_cab+"-"+block_drawer+"-"+block_col+"-"+block_pos
            print ("Block location is "+ block_location)
            location = ask_y_n_statement.ask_y_n("Is this correct?")
        block_current = input ("What is the current location of block? ")
        biopsy_pccm = ask_y_n_statement.ask_y_n("Is the biopsy report in PCCM custody? ", "In PCCM Custody", "Not in PCCM custody")
        block_id = input("Biopsy Block ID: ")
        block_number = input("Number of blocks: ")
        block_date = input("Date of Biopsy: ")
        lab_id = input("Biopsy Lab ID: ")
        biopsy_type = ask_y_n_statement.ask_option("Biopsy Type", ["Direct", "USG Guided", "VAB", "True-cut", "Steriotactic", "Other"])
        data_list = [con_stat, con_form, block_sr, block_location, block_current, biopsy_pccm, block_id,  block_number, block_date, lab_id, biopsy_type]
        columns_list = pccm_names.names_biopsy(module_name)
        check = review_input(file_number, columns_list, data_list)
    return (tuple(data_list))

def tumour_biopsy_data(file_number):
    from ask_y_n_statement import ask_option,ask_y_n
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
        lymph_emboli = ask_y_n("Are Lymphovascular emboli seen?", "Lymphovascular Emboli Seen", "No Lymphovascular Emboli Seen")
        dcis_biopsy = ask_y_n("Does the biopsy show DCIS", "DCIS seen", "DCIS not seen")
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
        data_list = [tumour_diagnosis, tumour_grade, lymph_emboli, dcis_biopsy, tumour_er ,tumour_er_percent ,tumour_pr, tumour_pr_percent,
                     tumour_her2, tumour_her2_grade, tumour_fish, tumour_ki67]
        columns_list = pccm_names.names_biopsy(module_name)
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

def add_data(conn, cursor, file_number):
    from ask_y_n_statement import ask_y_n
    import add_update_sql
    import pccm_names
    file_row(cursor, file_number)
    table = "Biopsy_Report_Data"
    enter = ask_y_n("Enter Biopsy Block Report information?")
    if enter:
        data = biopsy_report_info(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_biopsy("biopsy_report_info"), file_number,
                                       data)
    enter = ask_y_n("Enter Tumour Biopsy data?")
    if enter:
        data = tumour_biopsy_data(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_biopsy("tumour_biopsy_data"), file_number,
                                       data)
    enter = ask_y_n("Enter Lymphnode Biopsy data?")
    if enter:
        data = lymphnode_biopsy(file_number)
        add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_biopsy("lymphnode_biopsy"), file_number,
                                       data)

def edit_data(conn, cursor, file_number):
    import add_update_sql
    import pccm_names as colname
    table = "Biopsy_Report_Data"
    print("Block Report information")
    col_list = colname.names_biopsy("biopsy_report_info")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = biopsy_report_info(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Tumour Biopsy data")
    col_list = colname.names_biopsy("tumour_biopsy_data")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = tumour_biopsy_data(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Lymphnode Biopsy data")
    col_list = colname.names_biopsy("lymphnode_biopsy")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = lymphnode_biopsy(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)