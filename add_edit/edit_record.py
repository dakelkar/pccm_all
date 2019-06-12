import reports
from main.add_insert_block_data import AddBlockData


def edit_record(conn, cursor, file_number, table, user_name, folders, file):
    block_data = AddBlockData(folders, file, user_name)
    if table == "patient_information_history":
        reports.gen_info_tables.edit_data(conn, cursor, file_number, user_name, folders)
    elif table == 'biopsy_path_report_data':
        block_data.add_path_report(table)
    elif table == "clinical_exam":
        reports.clinical_exam.edit_data(conn, cursor, file_number, user_name)
    elif table == "radiology":
        reports.radiology.edit_data(conn, cursor, file_number, user_name)
    elif table == "neo_adjuvant_therapy":
        reports.nact.edit_data(conn, cursor, file_number, user_name)
    elif table == "surgery_report":
        reports.surgery_info.edit_data(conn, cursor, file_number, user_name)
    elif table == "adjuvant_chemotherapy":
        reports.chemotherapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "radiotherapy":
        reports.radiotherapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "hormonetherapy_survival":
        reports.longterm_therapy.edit_data(conn, cursor, file_number, user_name)
    elif table == "follow_up_data":
        reports.follow_up_month_year.edit_data(conn, cursor, file_number, user_name)
