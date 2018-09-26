import reports


def edit_record(conn, cursor, file_number, table, user_name, folders):
    if table == "Patient_Information_History":
        reports.gen_info_tables.edit_data(conn, cursor, file_number, user_name, folders)
    elif table == "Biopsy_Report_Data":
        biopsy = reports.BiopsyData(conn, cursor, file_number, user_name)
        biopsy.edit_data()
    elif table == "Clinical_Exam":
        reports.clinical_exam.edit_data(conn, cursor, file_number, user_name)
    elif table == "Radiology":
        reports.radiology.edit_data(conn, cursor, file_number, user_name)
    elif table == "Neo_Adjuvant_Therapy":
        reports.nact.edit_data(conn, cursor, file_number, user_name)
    elif table == "Surgery_Report":
        reports.surgery_info.edit_data(conn, cursor, file_number, user_name)
    elif table == "Surgery_Block_Report_Data":
        reports.surgery_block.edit_data(conn, cursor, file_number, user_name)
    elif table == "Adjuvant_ChemoTherapy":
        reports.chemotherapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "Radiotherapy":
        reports.radiotherapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "HormoneTherapy_Survival":
        reports.longterm_therapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "Follow_up_Data":
        reports.follow_up_month_year.edit_data(conn, cursor, file_number, user_name)
