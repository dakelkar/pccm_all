def edit_record(conn, cursor, file_number, table):
    from ask_y_n_statement import ask_y_n
    import add_update_sql
    import gen_info_tables
    import block_report_data
    import clinical_exam
    import pccm_names as colname
    if table == "Patient_Information_History":
        print("Patient Biographical Information")
        col_list = colname.names_info("bio_info")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = gen_info_tables.bio_info(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        col_list = colname.names_info("phys_act") + colname.names_info("habits") + \
                   colname.names_info("nut_supplements")
        print("Patient habits")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data_phys = gen_info_tables.phys_act(conn, cursor, file_number)
            data_hab = gen_info_tables.habits(file_number)
            data_nut = gen_info_tables.nut_supplements(conn, cursor, file_number, table)
            data = data_phys + data_hab + data_nut
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Patient family and reproductive details")
        col_list = colname.names_info("family_details")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = gen_info_tables.family_details(conn, cursor, file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Patient and family medical history")
        col_list = colname.names_info("med_history") + colname.names_info("cancer_history") + \
                   colname.names_info("family_cancer")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data_med = gen_info_tables.med_history(conn, cursor, file_number)
            data_can = gen_info_tables.cancer_history(conn, cursor, file_number)
            data_fam = gen_info_tables.family_cancer(conn, cursor, file_number)
            data = data_med + data_can + data_fam
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Patient Symptoms")
        col_list = colname.names_info("det_by") + colname.names_info("breast_symptoms")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data_det = gen_info_tables.det_by(file_number)
            data_symp = gen_info_tables.breast_symptoms(file_number)
            data = data_det + data_symp
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    if table == "Block_Report_Data" or table == "All":
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
    if table == "Clinical_Exam" or table == "All":
        print("Initial Clinical Examination")
        col_list = colname.names_clinical("clinical_exam_initial")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = clinical_exam.clinical_exam_initial(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Nipple Cytology")
        col_list = colname.names_clinical("nipple_cytology")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = clinical_exam.nipple_cytology(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Mammography")
        col_list = colname.names_clinical("mammography")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = clinical_exam.mammography(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("3D-Tomosynthesis")
        col_list = colname.names_clinical("tomosynthesis")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = clinical_exam.tomosynthesis(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Automated Breast Volume Scan")
        col_list = colname.names_clinical("abvs")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = clinical_exam.abvs(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("Sono-Mammography")
        col_list = colname.names_clinical("sonomammo")
        enter = ask_y_n("Edit data for Sono-Mammography")
        if enter:
            data = clinical_exam.sonomammo(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
        print("MRI Breast and Axilla")
        col_list = colname.names_clinical("mri_breast_axilla")
        enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
        if enter:
            data = clinical_exam.mri_breast_axilla(file_number)
            add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
