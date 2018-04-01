def edit_record(conn, cursor, file_number, table):
    import sql.add_update_sql as add_update_sql
    import reports.gen_info_tables as gen_info_tables
    import reports.biopsy_report as biopsy_report
    import reports.surgery_block as surgery_block
    import reports.block_report_data as block_report_data
    import reports.clinical_exam as clinical_exam
    import modules.pccm_names as colname

    if table in {"Patient_Information_History", "All"}:
        gen_info_tables.edit_data(conn, cursor, file_number)
    if table in {"Biopsy_Report_Data", "All"}:
        biopsy_report.edit_data(conn, cursor, file_number)
    if table in {"Clinical_Exam", "All"}:
        clinical_exam.edit_data(conn, cursor, file_number)
    if table in {"NeoAdjuvant_Chemotherapy", "All"}:
        print ("module to be added")
    if table in {"Surgery_Block_Report_Data", "All"}:
        surgery_block.add_data(conn,cursor,file_number)
    if table in {"Adjuvant_Chemotherapy", "All"}:
        print ("module to be added")

    if table == "Block_Report_Data":
        print("Block Report information")
        col_list = colname.names_block("block_report_info")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = block_report_data.block_report_info(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Tumour Biopsy data")
        col_list = colname.names_block("tumour_biopsy_data")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = block_report_data.tumour_biopsy_data(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Lymphnode Biopsy data")
        col_list = colname.names_block("lymphnode_biopsy")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = block_report_data.lymphnode_biopsy(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Surgery Information")
        col_list = colname.names_block("surgery_info")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = block_report_data.surgery_info(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Surgery Block Report")
        col_list = colname.names_block("surgery_block")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = block_report_data.surgery_block(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Node Block Details")
        col_list = colname.names_block("node_block")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = block_report_data.node_block(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Pathological Stage")
        col_list = colname.names_block("path_stage")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = block_report_data.path_stage(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)

