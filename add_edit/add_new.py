import reports
from main.add_insert_block_data import AddBlockData


def add_new(conn, cursor, file_number, table, user_name, folders, file):
    block_data = AddBlockData(folders, file, user_name)
    if table == "patient_information_history":
        reports.gen_info_tables.add_gen_info(conn, cursor, file_number, user_name, folders)
    elif table == 'biopsy_path_report_data':
        block_data.add_path_report(table)
    elif table == "clinical_exam":
        reports.clinical_exam.add_data(conn, cursor, file_number, user_name)
    elif table == "radiology":
        reports.radiology.add_data(conn, cursor, file_number, user_name)
    elif table == "neo_adjuvant_therapy":
        reports.nact.add_data(conn, cursor, file_number, user_name)
    elif table == "surgery_report":
        reports.surgery_info.add_data(conn, cursor, file_number, user_name)
    elif table == 'surgery_path_report_data':
        block_data.add_path_report(table)
    elif table == "adjuvant_chemotherapy":
        reports.chemotherapy.add_data(conn, cursor, file_number, user_name)
    elif table == "radiotherapy":
        reports.radiotherapy.add_data(conn, cursor, file_number, user_name)
    elif table == "hormonetherapy_survival":
        reports.longterm_therapy.add_data(conn, cursor, file_number, user_name)
    elif table == "follow_up_data":
        reports.follow_up_month_year.add_data(conn, file_number, user_name)