import modules.pccm_names as names

def create_col_list (colnames):
    col_list = ["File_number"] + colnames
    return col_list

def table_module_dict (table):
    table_module = {
        "Patient_Information_History": ["bio_info", "phys_act", "habits", "nut_supplements", "family_details",
                                        "med_history",
                                        "cancer_history", "family_cancer", "det_by", "breast_symptoms"],
        "Biopsy_Report_Data": ["biopsy_report_info", "tumour_biopsy_data"],
        "Radiology": ["mammography", "abvs", "sonomammo", "mri_breast"],
        "Neo_Adjuvant_Therapy": ["Neo_Adjuvant_Therapy", "clip_information"],
        "Surgery_Report": ["surgery_information", "node_excision", "post_surgery"],
        "Surgery_Block_Report_Data": ["surgery_block_information_1", "surgery_block_information_2",
                                      "surgery_block_information_3",
                                      "path_stage"],
        "Adjuvant_ChemoTherapy": ['Adjuvant_ChemoTherapy'],
        "Radiotherapy": [],
        "HormoneTherapy_Survival": ["hormone", "metastasis"],
        "Follow_up_Data": []
    }
    module_list = table_module.get(table)
    return module_list

def table_module_research (table):
    table_module = {
        "Patient_Information_History": ["bio_info_without_personal_info", "phys_act", "habits", "nut_supplements", "family_details",
                                        "med_history","cancer_history", "family_cancer", "det_by", "breast_symptoms"],
        "Biopsy_Report_Data": ["biopsy_report_info", "tumour_biopsy_data"],
        "Radiology": ["mammography", "abvs", "sonomammo", "mri_breast"],
        "Neo_Adjuvant_Therapy": ["Neo_Adjuvant_Therapy", "clip_information"],
        "Surgery_Report": ["surgery_information", "node_excision", "post_surgery"],
        "Surgery_Block_Report_Data": ["surgery_block_information_1", "surgery_block_information_2",
                                      "surgery_block_information_3",
                                      "path_stage"],
        "Adjuvant_ChemoTherapy": ['Adjuvant_ChemoTherapy'],
        "Radiotherapy": [],
        "HormoneTherapy_Survival": ["hormone", "metastasis"],
        "Follow_up_Data": []
    }
    module_list = table_module.get(table)
    return module_list

def db_dict (table, module):
    db_tables = {"Patient_Information_History" : names.names_info(module),
                 "Biopsy_Report_Data" : names.names_biopsy_new(module),
                 "Radiology" : names.names_radio(module),
                 "Neo_Adjuvant_Therapy": names.names_nact(module),
                 "Surgery_Report" : names.names_surgery_information(module),
                 "Surgery_Block_Report_Data" : names.names_surgery(module),
                 "Adjuvant_ChemoTherapy": names.names_chemotherapy(module),
                 "Radiotherapy": names.names_radiation(),
                 "HormoneTherapy_Survival": names.names_longterm(module),
                 "Follow_up_Data": names.name_follow_up()}
    cols = db_tables.get(table)
    return cols
