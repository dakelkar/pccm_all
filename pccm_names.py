def names_info(module_name):
    if module_name == "nut_supplements":
        col_list = ["Nutritional_supplements_y_n", "Type_Nutritional_supplements", "Quantity_Nutritional_supplements", \
              "Duration_Nutritional_supplements"]
    elif module_name == "phys_act":
        col_list = ["Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"]
    elif module_name == "med_history":
        col_list = ["Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History",
                    "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History"]
    elif module_name == "cancer_history":
        col_list = ["Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer", \
                        "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer",
                        "Treatment_Duration_Previous_Cancer"]
    elif module_name == "family_details":
        col_list = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                    "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period",
                    "Period_Type", "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child",
                    "Age_first_pregnancy", "Age_last_child", "Age_last_pregnancy", "Two_births_in_year",
                    "Breast_feeding", "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding",
                    "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"]
    elif module_name == "breast_symptoms":
        col_list = ["RB_symptoms", "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration",
                    "RB_Other_Symptoms","RB_Other_Symptoms_duration", "LB_Other_Symptoms", "LB_Other_Symptoms_duration",
                    "Metastasis_Symptoms"]
    elif module_name == "habits":
        col_list = ["Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week",
                    "Duration_alcohol", "Comments_alcohol", "Tobacco_y_n", "Exposure_Mode", "Type_Passive",
                    "Type_tobacco", "Tobacco_consumption_age_yrs", "Tobacco_Frequency","Quantity_tobacco_per_week",
                    "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"]
    elif module_name == "det_by":
        col_list = ["Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date"]
    elif module_name == "family_cancer":
        col_list = ["FamilyCancer_history_y_n", "Type_DegreeRelation_TypeRelation_Age_FamilyCancer"]
    elif module_name == "bio_info":
        col_list = ["MR_number", "Name", "Consent", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address",
                        "Current_Address", "Phone", "Email_ID", "Gender", "Age_yrs", "Date_of_Birth", "Place_Birth",
                        "Height_cm", "Weight_kg", "BMI"]
    else:
        col_list = ["File_number"]
    return col_list

def names_clinical(module_name):
    if module_name == "clinical_exam_initial":
        col_list = ['Provisional_Diagnosis_Clinical_Examination_CE', 'Lump_Palpable_CE', 'Lump_Location_CE', 'Lump_Size_CE', 'Lump_Number_CE', \
                  'Lump_Consistency_CE', 'Lump_Fixity_CE', 'Mastitis_CE', 'Mastitis_type_CE', 'Tenderness_CE', \
                  'Nipple_Retraction_CE', 'Nipple_Discharge_CE', 'Nipple_Discharge_Type_CE', 'Skin_changes_CE', \
                  'Skin_change_type_CE', 'Palpable_axillary_nodes_CE', 'Palpable_axillary_nodes_number_CE', \
                  'Palpable_axillary_nodes_size_CE', 'Palpable_axillary_nodes_fixity_CE', \
                  'Palpable_supraclavicular_nodes_CE', 'Palpable_supraclavicular_nodes_number_CE', \
                  'Palpable_supraclavicular_nodes_size_CE', 'Palpable_supraclavicular_nodes_fixity_CE', \
                  'Contralateral_Breast_CE', 'Edema_arm_CE', 'RightArm_Circumference_cm_CE', \
                  'RightArm_UpperLimbVolume_cc_CE', 'RightArm_ElbowDistance_cm_CE', 'LeftArm_Circumference_cm_CE', \
                  'LeftArm_UpperLimbVolume_cc_CE', 'LeftArm_ElbowDistance_cm_CE']
    elif module_name =="nipple_cytology":
        col_list = ["Nipple_Cytology", "Date_Nipple_Cytology", "Number_Nipple_Cytology", "Report_Nipple_Cytology"]
    elif module_name == "mammography":
        col_list = ['DiagnosisLocation_Mammography', 'First_Mammography', 'LatestDate_Mammography', 'Number_Mammography', \
                  'PreviousDate_Mammography', 'Diagnosis_Mammography', 'Date_Diagnosis_Mammography', 'AccessionNumber_Mammography', \
                  'BreastDensity_Mammography','Lesion_Mammography', 'LesionLocation_Mammography', 'Shape_Mammography', 'Size_Mammography', \
                  'Margin_Mammography', 'Density_Mammography', 'Calcification_Mammography', \
                  'Calcification_Implication_Mammography', 'Calcification_Distribution_Mammography', \
                  'Architecture_Mammography', 'Asymmetry_Mammography', 'IntraMammaryLN_Mammography', \
                  'SkinLesion_Mammography', 'DilatedDuct_Mammography', 'Features_SkinRetraction_Mammography', \
                  'Features_NippleRetraction_Mammography', 'Features_SkinThickening_Mammography', \
                  'Features_TrabecularThickening_Mammography', 'Features_AxillaryLymphadenopathy_Mammography', \
                  'Features_ArchitecturalDistortion_Mammography', "Features_Calcification_Mammography",\
                  'SecondaryLesion_ContralateralBreast_Mammography','DistancefromSkin_Mammography',
                    'DistanceFromPectMaj_Mammography', 'BIRADS_Mammography']
    elif module_name == "tomosynthesis":
        col_list = ["Tomosynthesis_3D", "Date_Tomosynthesis", "Accession_Tomosynthesis", "Lesion_Tomosynthesis",
                        "Lesion_Location_Tomosynthesis", "Size_Tomosynthesis", "Distance_Tomosynthesis",
                        "Distance_PectMajor_Tomosynthesis", "Diagnosis_Tomosynthesis"]
    elif module_name == "abvs":
        col_list = ["Automated_Breast_Volume_Scanner_ABVS", "Date_ABVS", "Accession_ABVS", "Lesion_ABVS", \
              "Lesion_Location_ABVS", "Size_ABVS", "Distance_ABVS", "Distance_PectMajor_ABVS", \
              "Diagnosis_ABVS"]
    elif module_name == "sonomammo":
        col_list = ['SonoMammography', 'Date_SonoMammography', 'AccessionNumber_SonoMammography', \
                       'Number_SonoMammography', 'Lesion_SonoMammography', 'Lesion_Location_SonoMammography', \
                       'Shape_SonoMammography', 'Size_SonoMammography', 'Orientation_SonoMammography', \
                       'Margins_SonoMammography', 'Echo_SonoMammography', 'Postacoustic_SonoMammography', \
                       'Calcification_SonoMammography', 'ArchitecturalDistoration_SonoMammography', \
                       'SkinChanges_SonoMammography', 'Edema_SonoMammography', 'Vascularity_SonoMammography', \
                       'LymphNodes_SonoMammography', 'DistanceNipple_SonoMammography', 'DistanceSkin_SonoMammography', \
                       'Distance_PectMajor_SonoMammography', 'Diagnosis_SonoMammography']
    elif module_name == "mri_breast_axilla":
        col_list = ['MRI_Breast_Axilla', 'Date_MRI_Breast_Axilla', 'AccessionNumber_MRI_Breast_Axilla',
                        'Lesion_MRI_Breast_Axilla', 'LesionLocation_MRI_Breast_Axilla', 'Size_MRI_Breast_Axilla',
                        'DistancefromSkin_MRI_Breast_Axilla', 'DistanceFromPectMaj_MRI_Breast_Axilla',
                        'Diagnosis_MRI_Breast_Axilla']
    else:
        col_list = ["File_number"]
    return col_list

def names_block(module_name):
    if module_name == "block_report_info":
        col_list = ["Block_SR_Number", "Biopsy_Block_ID", "No_of_blocks", "Date_of_Biopsy", "Lab_ID", "Biopsy_Type"]
    elif module_name == "tumour_biopsy_data":
        col_list = ["Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade", "Tumour_biopsy_ER",
                    "Tumour_biopsy_ER_Percent", "Tumour_biopsy_PR", "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2",
                    "Tumour_biopsy_HER2_Grade", "Tumour_biopsy_FISH", "Tumour_biopsy_Ki67_Percent"]
    elif module_name == "lymphnode_biopsy":
        col_list = ["Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location", "Lymph_Node_biopsy_diagnosis"]
    elif module_name == "surgery_info":
        col_list = ["Surgical_Block_ID", "Surgery_Block_Location", "Surgery_No_of_blocks", "Block_Source",
                    "Tumor_block_ref", "Nodes_block_ref", "Ad_Normal_block_ref", "Reduction_tissue_block_ref",
                    "Date_of_Surgery", "Name_Surgeon", "Hospital_ID", "Lesion_Side", "Type_surgery", "Response_surgery"]
    elif module_name == "surgery_block":
        col_list = ["Tumour_size_Surgery_Block_Report", "Grade_Surgery_Block_Report", "Diagnosis_Surgery_Block_Report",
                    "DCIS_Percent_Surgery_Block_Report", "DCIS_Invasion_Surgery_Block_Report",
                    "Perineural_Invasion_Surgery_Block_Report", "Necrosis_Surgery_Block_Report",
                    "Lymphovascular_Invasion_Surgery_Block_Report", "Margins_Surgery_Block_Report",
                    "Surgery_Block_Report"]
    elif module_name == "node_block":
        col_list = ["Sentinel_Node_Block_Report", "Sentinel_Node_Number_Removed", "Sentinel_Node_Number_Positive",
                    "Sentinel_Node_Block_Report_Number", "Axillary_Node_Block_Report", "Axillary_Node_Number_Removed",
                    "Axillary_Node_Number_Positive", "Axillary_Node_Block_Report_Number", "Apical_Node_Block_Report",
                    "Apical_Node_Number_Removed", "Apical_Node_Number_Positive", "Apical_Node_Block_Report_Number",
                    "Perinodal_Spread_Node_Block_Report", "Supraclavicular_Involved_Node_Block_Report"]
    elif module_name == "path_stage":
        col_list = ["Pathological_Staging_pT", "Pathological_Staging_pN", "Pathological_Staging_M",
                    "Pathological_Staging_P_Stage", "Clinical_Staging"]
    else:
        col_list = "File_number"
    return col_list