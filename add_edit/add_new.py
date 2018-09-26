import reports


def add_new(conn, cursor, file_number, table, user_name, folders):
    if table == "Patient_Information_History":
        reports.gen_info_tables.add_gen_info(conn, cursor, file_number, user_name, folders)
    elif table == "Biopsy_Report_Data":
        biopsy = reports.BiopsyData(conn, cursor, file_number, user_name)
        biopsy.add_data()
    elif table == "Clinical_Exam":
        reports.clinical_exam.add_data(conn, cursor, file_number, user_name)
    elif table == "Radiology":
        reports.radiology.add_data(conn, cursor, file_number, user_name)
    elif table == "Neo_Adjuvant_Therapy":
        reports.nact.add_data(conn, cursor, file_number, user_name)
    elif table == "Surgery_Report":
        reports.surgery_info.add_data(conn, cursor, file_number, user_name)
    elif table == "Surgery_Block_Report_Data":
        reports.surgery_block.add_data(conn,cursor,file_number, user_name)
    elif table == "Adjuvant_ChemoTherapy":
        reports.chemotherapy.add_data(conn, cursor, file_number, user_name)
    elif table == "Radiotherapy":
        reports.radiotherapy.add_data(conn, cursor, file_number, user_name)
    elif table == "HormoneTherapy_Survival":
        reports.longterm_therapy.add_data(conn, cursor, file_number, user_name)
    elif table == "Follow_up_Data":
        reports.follow_up_month_year.add_data(conn, file_number, user_name)