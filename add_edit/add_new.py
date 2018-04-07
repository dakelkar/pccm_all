import reports


def add_new(conn, cursor, file_number, table):
    if table =="Patient_Information_History":
        reports.gen_info_tables.add_gen_info(conn, cursor, file_number)
    elif table =="Biopsy_Report_Data":
        reports.biopsy_report.add_data(conn, cursor, file_number)
    elif table =="Clinical_Exam":
        reports.clinical_exam.add_data(conn, cursor, file_number)
    elif table == "Radiology":
        reports.radiology.add_data(conn, cursor, file_number)
    elif table =="NeoAdjuvant_Chemotherapy":
        reports.nact.add_data(conn, cursor, file_number)
    elif table =="Surgery_Report":
        reports.surgery_info.add_data(conn, cursor, file_number)
    elif table =="Surgery_Block_Report_Data":
        reports.surgery_block.add_data(conn,cursor,file_number)
    elif table =="Chemotherapy":
        reports.chemotherapy.add_data(conn, cursor, file_number)
    elif table == "Radiotherapy":
        reports.radiotherapy.add_data(conn, cursor, file_number)
    elif table == "HormoneTherapy_Recurrence_Survival":
        reports.longterm_therapy.add_data(conn, cursor, file_number)
    elif table == "Follow_up_Data":
        reports.follow_up_month_year.add_data(conn, file_number)