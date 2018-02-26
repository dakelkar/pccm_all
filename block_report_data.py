def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Block_Report_Data(File_number) VALUES ('" + file_number + "')")

def block_report_info (conn, cursor, file_number, table):
    from add_update_sql import update_multiple
    from ask_y_n_statement import ask_option, ask_y_n
    block_sr = input("Block Serial Number: ")
    block_id = input ("Biopsy Block ID: ")
    block_number = input("No of blocks: ")
    block_date = input("Date of Biopsy: ")
    lab_id = input("Lab ID: ")
    category = "Biopsy Type"
    options = ["Direct", "USG Guided", "VAB", "True-cut", "Steriotactic", "Other"]
    biopsy_type= ask_option(category, options)
    columns = "Block_SR_Number", "Biopsy_Block_ID", "No_of_blocks", "Date_of_Biopsy", "Lab_ID", "Biopsy_Type"
    data = block_sr, block_id, block_number, block_date, lab_id,biopsy_type
    update_multiple(conn, cursor, table, columns, file_number, data)

def tumour_biopsy_data(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    from add_update_sql import update_multiple
    category = "Tumour biopsy diagnosis"
    options = ['Benign', "Ductal carcinoma in situ(DCIS) with microinvasion",
               "Ductal carcinoma in situ(DCIS) without microinvasion", "Lobular Carcinoma in Situ (LCS)",
               "Invasive Ductal Carcinoma (IDC)", "Invasive Lobular Carcinoma (ILC)", "Granulamatous Mastitis",
               "Papillary Carcinoma", "Phylloid Carcinoma", "Invasive Mammary Carcinoma", "Invasive Breast Carcinoma",
               "Other"]
    tumour_diagnosis = ask_option(category, options)
    category = "Tumour Biopsy Diagnosis"
    options = ["Grade 1", "Grade 2", "Grade 3", "Other"]
    tumour_grade = ask_option(category, options)
    category = "ER Status"
    options = ["Positive", "Negative"]
    tumour_er= ask_option(category, options)
    if (tumour_er == "Positive"):
        tumour_er_percent = input ("ER Percent: ")
    else:
        tumour_er_percent = "NA"
    category = "PR Status"
    options = ["Positive", "Negative"]
    tumour_pr = ask_option(category, options)
    if (tumour_pr == "Positive"):
        tumour_pr_percent = input ("PR Percent: ")
    else:
        tumour_pr_percent = "NA"
    category = "HER2 Status"
    options = ["Positive", "Equivocal", "Negative"]
    tumour_her2 = ask_option(category, options)
    if tumour_her2 == "Negative":
        tumour_her2_grade, tumour_fish = ("NA", )*2
    else:
        tumour_her2_grade = input ("HER2 Grade: ")
        category = "FISH"
        options = ["Positive", "Negative"]
        tumour_fish = ask_option(category, options)
    tumour_ki67 = input("Ki67 Percent: ")
    data = tumour_diagnosis, tumour_grade, tumour_er ,tumour_er_percent ,tumour_pr, tumour_pr_percent, tumour_her2, tumour_her2_grade,\
           tumour_fish, tumour_ki67
    columns = "Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade", "Tumour_biopsy_ER", "Tumour_biopsy_ER_Percent",\
              "Tumour_biopsy_PR", "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2", "Tumour_biopsy_HER2_Grade", \
              "Tumour_biopsy_FISH", "Tumour_biopsy_Ki67_Percent"
    update_multiple(conn, cursor, table, columns, file_number, data)

def lymphnode_biopsy(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    from add_update_sql import update_multiple
    category = "Lymph Node biopsy FNAC" 
    options = ["Done", "Not Done"]
    fnac = ask_option(category, options)
    if fnac == "Done":
        category = "Lymph Node biopsy location"
        options = ["Right", "Left", "Both"]
        fnac_location = ask_option(category, options)
        category = "Lymph Node biopsy diagnosis"
        options = ["Normal", "Benign", "Malignant", "Other"]
        fnac_diagnosis = ask_option(category, options)
    else:
        fnac_location, fnac_diagnosis = ("NA", )*2
    data = fnac, fnac_location, fnac_diagnosis
    columns = "Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location", "Lymph_Node_biopsy_diagnosis"
    update_multiple(conn, cursor, table, columns, file_number, data)

def surgery_info (conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    from add_update_sql import update_multiple
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
    #can add review statement here.
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
    category = "Type Surgery"
    options = ["Reconstruction", "Breast Conservation Surgery (BCS)", "Therapeutic Mammoplasty", "Reduction Mammoplasty", "Wide Local Excision", "Other"]
    surg_type = ask_option (category, options)
    if surg_type == "Reconstruction":
        category = "Type Reconstruction"
        options = ["Mastectomy/Modified Radical Mastectomy", "Implant"]
        surg_type = ask_option(category, options)
    category = "Response to Surgery"
    options = ["Complete_Remission/No Residual Tumor", "Progressing", "Partial", "Static", "Other"]
    surg_response = ask_option(category, options)
    data = surg_block_id, surg_no_block, surg_block_source, surg_tumour_block, surg_node_block, surg_normal_block, \
           surg_red_block, surg_date, surg_name, surg_hosp_id, lesion_side, surg_type, surg_response
    surgery_info = "Surgical_Block_ID", "Surgery_Block_Location", "Surgery_No_of_blocks", "Block_Source", "Tumor_block_ref", "Nodes_block_ref", \
              "Ad_Normal_block_ref", "Reduction_tissue_block_ref", "Date_of_Surgery", "Name_Surgeon", "Hospital_ID", \
              "Lesion_Side", "Type_surgery", "Response_surgery"
    update_multiple(conn, cursor, table, surgery_info , file_number, data)

def surgery_block (conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option, ask_y_n
    from add_update_sql import update_multiple
    print ("Surgery Block Report")
    tumour_size = input ("Tumour size: ")
    category = "Tumour Grade"
    options = ["I", "II", "III", "Other"]
    tumour_grade = ask_option(category, options)
    category = "Surgery Diagnosis"
    options = ["Ductal carcinoma in situ(DCIS)", "Invasive Ductal Carcinoma", "Other"]
    surg_diag = ask_option(category, options)
    if (surg_diag == "Ductal carcinoma in situ(DCIS)"):
        dcis_percent = input ("Percent DCIS: ")
        category = "DCIS Invasion"
        options = ['Microinvasion', 'Macroinvasion']
        dcis_invasion = ask_option(category, options)
    else:
        dcis_percent, dcis_invasion = ("NA", )*2
    per_inv = ask_y_n("Perineural Invasion", "Perineural Invasion Present", "Perineural Invasion Absent")
    necrosis = ask_y_n("Necrosis", "Necrosis Present", "Necrosis Absent")
    lymph_invasion = ask_y_n("Lymphovascular invasion", "Lymphovascular invasion Present", "Lymphovascular invasion Absent")
    category = "Margins"
    options = ["Involved", "Free"]
    margin = ask_option(category, options)
    print ("Surgery Block Report")
    category = "Pathological Complete Remission"
    options = ["Yes", "No", "Other"]
    report = ask_option(category, options)
    data = tumour_size,tumour_grade,surg_diag,dcis_percent,dcis_invasion,per_inv,necrosis,lymph_invasion,margin, report
    columns = "Tumour_size_Surgery_Block_Report", "Grade_Surgery_Block_Report", "Diagnosis_Surgery_Block_Report", \
              "DCIS_Percent_Surgery_Block_Report", "DCIS_Invasion_Surgery_Block_Report", \
              "Perineural_Invasion_Surgery_Block_Report", "Necrosis_Surgery_Block_Report", \
              "Lymphovascular_Invasion_Surgery_Block_Report", "Margins_Surgery_Block_Report", "Surgery_Block_Report"
    update_multiple(conn, cursor, table, columns, file_number, data)

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

def node_block (conn, cursor, file_number, table):
    from ask_y_n_statement import ask_option
    from add_update_sql import update_multiple
    sent_data = node_details("Sentinel")
    sentinel, sent_number_rem, sent_number_pos, sent_number = sent_data
    print ("Sentinel Node "+ sent_number)
    ax_data = node_details("Axillary")
    ax, ax_number_rem, ax_number_pos, ax_number = ax_data
    print("Axillary Node " + ax_number)
    ap_data = node_details("Apical")
    ap, ap_number_rem, ap_number_pos, ap_number = ap_data
    print("Apical Node " + ap_number)
    category =  "Perinodal Spread"
    options = ["Yes", "No"]
    per_spread = ask_option(category, options)
    category = "Supraclavicular Node Involvment"
    options = ["Yes", "No"]
    supra_inv = ask_option(category, options)
    data = sentinel, sent_number_rem, sent_number_pos, sent_number, ax, ax_number_rem, ax_number_pos, ax_number, ap, \
           ap_number_rem, ap_number_pos, ap_number, per_spread, supra_inv
    columns = "Sentinel_Node_Block_Report", "Sentinel_Node_Number_Removed", "Sentinel_Node_Number_Positive", \
              "Sentinel_Node_Block_Report_Number", "Axillary_Node_Block_Report", "Axillary_Node_Number_Removed", \
              "Axillary_Node_Number_Positive", "Axillary_Node_Block_Report_Number", "Apical_Node_Block_Report", \
              "Apical_Node_Number_Removed", "Apical_Node_Number_Positive", "Apical_Node_Block_Report_Number", \
              "Perinodal_Spread_Node_Block_Report", "Supraclavicular_Involved_Node_Block_Report"
    update_multiple(conn, cursor, table, columns, file_number, data)
def path_stage(conn, cursor, file_number, table):
    from add_update_sql import update_multiple
    from ask_y_n_statement import ask_option, ask_y_n
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
    check = ask_y_n("Is patholgicial stage correct")
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
    print ("Based on TNM status", path_stage, "and data at https://emedicine.medscape.com/article/2007112-overview")
    check = ask_y_n("Is clinical stage correct")
    if not check:
        clinical_stage = input("Please enter correct clinical stage: ")
    data = pT, pN, M, path_stage, clinical_stage
    columns = "Pathological_Staging_pT", "Pathological_Staging_pN", "Pathological_Staging_M", \
              "Pathological_Staging_P_Stage", "Clinical_Staging"
    update_multiple(conn, cursor, table, columns, file_number, data)