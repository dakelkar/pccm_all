def add_new(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_y_n
    import add_update_sql
    import gen_info_tables
    import biopsy_report
    import surgery_block
    import block_report_data
    import clinical_exam
    import pccm_names

    if table in {"Patient_Information_History", "All"}:
        gen_info_tables.add_gen_info(conn, cursor, file_number)
    if table in {"Biopsy_Report_Data", "All"}:
        biopsy_report.add_data(conn, cursor, file_number)
    if table in {"Clinical_Exam", "All"}:
        clinical_exam.add_data(conn, cursor, file_number)
    if table in {"NeoAdjuvant_Chemotherapy", "All"}:
        print ("module to be added")
    if table in {"Surgery_Block_Report_Data", "All"}:
        surgery_block.add_data(conn,cursor,file_number)
    if table in {"Adjuvant_Chemotherapy", "All"}:
        print ("module to be added")
    if table in {"Block_Report_Data", "All"}:
        block_report_data.file_row(cursor, file_number)
        enter = ask_y_n("Enter Block Report information?")
        if enter:
            data = block_report_data.block_report_info (file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_block("block_report_info"),
                                           file_number, data)
        enter = ask_y_n("Enter Tumour Biopsy data?")
        if enter:
            data = block_report_data.tumour_biopsy_data(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_block("tumour_biopsy_data"),
                                           file_number, data)
        enter = ask_y_n("Enter Lymphnode Biopsy data?")
        if enter:
            data = block_report_data.lymphnode_biopsy(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_block("lymphnode_biopsy"), file_number,
                                           data)
        enter = ask_y_n("Enter Surgery Information?")
        if enter:
            data = block_report_data.surgery_info (file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_block("surgery_info"), file_number,
                                           data)
        enter = ask_y_n("Enter Surgery Block Report?")
        if enter:
            data = block_report_data.surgery_block (file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_block("surgery_block"), file_number,
                                           data)
        enter = ask_y_n("Enter Node Block Details?")
        if enter:
            data = block_report_data.node_block (file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_block("node_block"), file_number,
                                          data)
        enter = ask_y_n("Enter Pathological Stage?")
        if enter:
            data = block_report_data.path_stage(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_block("path_stage"), file_number,
                                          data)