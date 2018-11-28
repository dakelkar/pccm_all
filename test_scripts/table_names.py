table_name = ["Patient_Information_History", "General_Medical_History", "Family_Cancer_History",
              "Previous_Cancer_History", "Nutritional_Supplements", "Physical_Activity", "Breast_Feeding",
              "Clinical_Exam", "Block_Report_Data", "SonnoMammography_Multiple_Mass", "Mammography_Multiple_Mass",
              "SonnoMammography_Multiple_Mass",  "MRI_Multiple_Mass", "Calcification_Mammography" ]
def table_module (index):
    import pccm_names
    module_name1 = ["File_number", "bio_info", "phys_act", "habits", "nut_supplements", "family_details", "med_history",
                        "cancer_history", "family_cancer", "det_by", "breast_symptoms"]
    module_name2 = ["general_table"]
    columns3 = ["family_cancer"]
    columns4 = ["previous_cancer"]
    columns5 = ["nut_sup"]
    columns6 = ["phys_act"]
    columns8 = ["breast_feed"]
    module_name9 = ["File_number", "clinical_exam_initial", "nipple_cytology", "mammography", "tomosynthesis", "abvs",
                    "sonomammo", "mri_breast"]
    module_names10 = ["File_number", 'block_report_info', 'tumour_biopsy_data', 'lymphnode_biopsy', 'surgery_info',
                      'surgery_block', 'node_block', 'path_stage']
    columns11 = ["SonnoMammography_Multiple_Mass"]
    columns12 = ['Mammography_Multiple_Mass']
    columns13 = ["MRI_Multiple_Mass"]
    columns14 = ["Calcification_Mammography"]
    modules = [module_name1, module_name2, columns3, columns4, columns5, columns6, columns8, module_names10,
               module_name9, columns11, columns12, columns13, columns14]
    module =  (modules[index])

    colnames = []
    for i in modules:
        col_list = pccm_names.colnames(modules[i])
        colnames.append(col_list)
    names = ", ".join(colnames)
    return names


