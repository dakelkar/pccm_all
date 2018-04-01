def table_module(table):
    if table == "Patient_Information_History":
        mod_list = ["bio_info", "phys_act", "habits", "nut_supplements", "family_details", "med_history",
                    "cancer_history", "family_cancer", "det_by", "breast_symptoms"]
        names_list = "names_info"
    elif table == "Biopsy_Report_Data":
        mod_list = ["biopsy_report_info", "tumour_biopsy_data", "lymphnode_biopsy"]
        names_list = "names_biopsy"
    elif table == "Clinical_Exam":
        mod_list = ["clinical_exam_initial", "nipple_cytology", "other_test","mammography", "tomosynthesis", "abvs", "sonomammo",
                    "mri_breast"]
        names_list = "name_clinical"
    elif table == "Surgery_Block_Report_Data":
        mod_list = ["surgery_block_information_1","surgery_block_information_2", "surgery_block_information_3",
                    "path_stage"]
        names_list = "names_surgery"
    elif table == "NeoAdjuvant_Chemotherapy"
        mod_list = ["NACT_Drug_Regimen", "NACT_Toxicity"]
        names_list = "names_nact"
    else:
        mod_list, names_list = "File_number", "File_number"
    return [mod_list, names_list]
