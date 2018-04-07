import reports

def edit_record(conn, cursor, file_number, table):
    if table =="Patient_Information_History":
        reports.gen_info_tables.edit_data(conn, cursor, file_number)
    elif table =="Biopsy_Report_Data":
        reports.biopsy_report.edit_data(conn, cursor, file_number)
    elif table =="Clinical_Exam":
        reports.clinical_exam.edit_data(conn, cursor, file_number)
    elif table == "Radiology":
        reports.radiology.edit_data(conn, cursor, file_number)
    elif table =="NeoAdjuvant_Chemotherapy":
        reports.nact.edit_data(conn, cursor, file_number)
    elif table =="Surgery_Report":
        reports.surgery_info.edit_data(conn, cursor, file_number)
    elif table =="Surgery_Block_Report_Data":
        reports.surgery_block.edit_data(conn,cursor,file_number)
    elif table =="Chemotherapy":
        reports.chemotherapy.edit_data(conn, cursor, file_number)
    elif table == "Radiotherapy":
        reports.radiotherapy.edit_data(conn, cursor, file_number)
    elif table == "HormoneTherapy_Recurrence_Survival":
        reports.longterm_therapy.edit_data(conn, cursor, file_number)
    elif table == "Follow_up_Data":
        reports.follow_up_month_year.edit_data(conn, cursor, file_number)