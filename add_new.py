def add_new(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_y_n
    import add_update_sql
    import block_report_data
    import gen_info_tables
    import clinical_exam
    import pccm_names
    from print_gen_info import print_info
    if table in {"Patient_Information_History", "All"}:
        gen_info_tables.file_row(cursor, file_number)
        enter = ask_y_n("Enter Patient Biographical Information")
        if enter:
            data = gen_info_tables.bio_info(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("bio_info"), file_number, data)
        enter = ask_y_n("Enter Patient habits")
        if enter:
            data = gen_info_tables.phys_act(conn, cursor, file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("phys_act"), file_number, data)
            data = gen_info_tables.habits(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("habits"), file_number, data)
            data = gen_info_tables.nut_supplements(conn, cursor, file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("nut_supplements"), file_number, data)
        enter = ask_y_n("Enter Patient family and reproductive details?")
        if enter:
            data = gen_info_tables.family_details(conn, cursor, file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("family_details"), file_number, data)
        enter = ask_y_n("Enter Patient and family medical history?")
        if enter:
            data = gen_info_tables.med_history(conn, cursor, file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("med_history"), file_number,
                                           data)
            data = gen_info_tables.cancer_history(conn, cursor, file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("cancer_history"), file_number,
                                           data)
            data = gen_info_tables.family_cancer(conn, cursor, file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("family_cancer"), file_number,
                                           data)
        enter = ask_y_n("Enter Patient Symptoms?")
        if enter:
            data = gen_info_tables.det_by(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("det_by"), file_number, data)
            data = gen_info_tables.breast_symptoms(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_info("breast_symptoms"), file_number,
                                           data)
        print_info(cursor, file_number)
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
    if table in {"Clinical_Exam", "All"}:
        clinical_exam.file_row(cursor, file_number)
        enter = ask_y_n("Enter Clinical Examination information")
        if enter:
            data = clinical_exam.clinical_exam_initial(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_clinical("clinical_exam_initial"),
                                           file_number, data)
        enter = ask_y_n("Enter Nipple Cytology report?")
        if enter:
            data = clinical_exam.nipple_cytology(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_clinical("nipple_cytology"),
                                           file_number, data)
        enter = ask_y_n("Enter Mammography Report?")
        if enter:
            data = clinical_exam.mammography(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_clinical("mammography"),
                                           file_number, data)
        enter = ask_y_n("Enter 3D Tomosynthesis?")
        if enter:
            data = clinical_exam.tomosynthesis(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_clinical("tomosynthesis"),
                                           file_number, data)
        enter = ask_y_n("Enter Automated Breast Volume Scanner")
        if enter:
            data = clinical_exam.abvs(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_clinical("abvs"),
                                           file_number, data)
        enter = ask_y_n("Enter Sono-Mammography")
        if enter:
            data = clinical_exam.sonomammo(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_clinical("sonomammo"),
                                           file_number, data)
        enter = ask_y_n("Enter MRI-Breast and Axilla")
        if enter:
            data = clinical_exam.mri_breast_axilla(file_number)
            add_update_sql.update_multiple(conn, cursor, table, pccm_names.names_clinical("mri_breast_axilla"),
                                           file_number, data)