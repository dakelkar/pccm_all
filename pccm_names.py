def names_info(module_name):
    if module_name == "nut_supplements":
        col_list = ["Nutritional_supplements_y_n", "Type_Nutritional_supplements", "Quantity_Nutritional_supplements",
                    "Duration_Nutritional_supplements"]
    elif module_name == "phys_act":
        col_list = ["Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"]
    elif module_name == "med_history":
        col_list = ["Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History",
                    "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History"]
    elif module_name == "cancer_history":
        col_list = ["Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer",
                    "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer", "Treatment_Duration_Previous_Cancer"]
    elif module_name == "family_details":
        col_list = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                    "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period",
                    "Period_Type", "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child",
                    "Age_first_pregnancy", "Age_last_child", "Age_last_pregnancy", "Two_births_in_year",
                    "Breast_feeding", "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding",
                    "Fertility_treatment_y_n", "Type_fertility_treatment", "Details_fertility_treatment",
                    "Cycles_fertility_treatment", "Success_fertility_treatment","Type_birth_control_used",
                    "Details_birth_control", "Duration_birth_control"]
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
        col_list = ["MR_number", "Name", "Aadhaar_Card", "FirstVisit_Date", "Permanent_Address",
                    "Current_Address", "Phone", "Email_ID", "Gender", "Age_yrs", "Date_of_Birth", "Place_Birth",
                    "Height_cm", "Weight_kg", "BMI"]
    else:
        col_list = ["File_number"]
    return col_list

def names_clinical(module_name):
    if module_name == "clinical_exam_initial":
        col_list = ["Consent_Status","Consent_form_status",'Provisional_Diagnosis_Clinical_Examination_CE',
                    'Lump_Palpable_CE', 'Lump_Location_CE', 'Lump_Size_CE', 'Lump_Number_CE',
                    'Lump_Consistency_CE', 'Lump_Fixity_CE', 'Mastitis_CE', 'Mastitis_type_CE', 'Tenderness_CE',
                    'Nipple_Retraction_CE', 'Nipple_Discharge_CE', 'Nipple_Discharge_Type_CE', 'Skin_changes_CE',
                    'Skin_change_type_CE', 'Palpable_axillary_nodes_CE', 'Palpable_axillary_nodes_number_CE',
                    'Palpable_axillary_nodes_size_CE', 'Palpable_axillary_nodes_fixity_CE',
                    'Palpable_supraclavicular_nodes_CE', 'Palpable_supraclavicular_nodes_number_CE',
                    'Palpable_supraclavicular_nodes_size_CE', 'Palpable_supraclavicular_nodes_fixity_CE',
                    'Contralateral_Breast_CE', 'Edema_arm_CE', 'RightArm_Circumference_cm_CE',
                    'RightArm_UpperLimbVolume_cc_CE', 'RightArm_ElbowDistance_cm_CE', 'LeftArm_Circumference_cm_CE',
                    'LeftArm_UpperLimbVolume_cc_CE', 'LeftArm_ElbowDistance_cm_CE']
    elif module_name =="nipple_cytology":
        col_list = ["Nipple_Cytology", "Date_Nipple_Cytology", "Number_Nipple_Cytology", "Report_Nipple_Cytology"]
    elif module_name == "mammography":
        col_list = ['Location_Mammography', 'First_Mammography', 'LatestDate_Mammography','Number_Mammography',
                    'PreviousDate_Mammography', 'Diagnosis_Mammography', 'Date_Diagnosis_Mammography',
                    'AccessionNumber_Mammography', 'BreastDensity_Mammography', 'Mass_Number_Mammography',
                    'Mass_Location_Mammography', 'Mass_Location_Quadrant', 'Mass_Shape_Mammography',
                    'Mass_Margin_Mammography', 'Mass_Density_Mammography', 'Calcification_Number_Mammography',
                    'Calcification_Location_Mammography', 'Calcification_Location_Quardrant_Mammography',
                    'Calcification_Description_Mammography','Calcification_Type_Mammography',
                    'Calcification_Distribution_Mammography','Architecture_Mammography',
                    'ArchitecturalDistoration_Location_Mammography','ArchitecturalDistoration_Quadrant_Mammography',
                    'Asymmetry_Location_Mammography', 'Asymmetry_Quadrant_Mammography', 'Asymmetry_Type_Mammography',
                    'IntraMammaryLN_Mammography', 'SkinLesion_Mammography', 'DilatedDuct_Mammography',
                    'Asso_features_Skin_retraction_Mammography', 'Asso_features_Nipple_retraction_Mammography',
                    'Asso_features_Skin_thickening_Mammography', 'Asso_features_Trabecular_thickening_Mammography',
                    'Asso_features_Axillary_adenopathy_Mammography', 'Asso_features_Architectural_distortion_Mammography',
                    'Asso_features_Calcifications_Mammography', 'Lesion_Depth_Mammography','Lesion_LateralLocation_Mammography',
                    'Lesion_QuadrantLocation_Mammography', 'Lesion_DistancefromNipple_Mammography',
                    'Lesion_DistanceFromPectMaj_Mammography', 'Category_BI_RADS_Mammography', 'Detail_BI_RADS_Mammography']
    elif module_name == "tomosynthesis":
        col_list = ["Tomosynthesis_3D", "Date_Tomosynthesis", "Accession_Tomosynthesis", "Lesion_Tomosynthesis",
                        "Lesion_Location_Tomosynthesis", "Size_Tomosynthesis", "Distance_Tomosynthesis",
                        "Distance_PectMajor_Tomosynthesis", "Diagnosis_Tomosynthesis"]
    elif module_name == "abvs":
        col_list = ["Automated_Breast_Volume_Scanner_ABVS", "Date_ABVS", "Accession_ABVS", "Lesion_ABVS",
                    "Lesion_Location_ABVS", "Size_ABVS", "Distance_ABVS", "Distance_PectMajor_ABVS",
                    "Diagnosis_ABVS"]
    elif module_name == "sonomammo":
        col_list = ['SonoMammography', 'Date_SonoMammography', 'AccessionNumber_SonoMammography',
                    'Tissue_Type_Sonomammography', 'Mass_Sonomamography',  'Mass_Number_Sonomamography',
                    'Mass_Location_Sonomamography', 'Mass_Location_Quadrant_Sonomamography',
                    'Mass_Location_Clock_Sonomamography',   'Mass_Shape_Sonomamography',
                    'Mass_Orientation_Sonomamography', 'Mass_Margin_Sonomamography', 'Mass_Echo_Sonomamography',
                    'Mass_Posterior_Sonomamography','Calicification_Sonomamography','Calicification_Type_Sonomamography',
                    'Architectural_Distortion_Sonomamography','Duct_Changes_Sonomamography','Skin_Changes_Sonomamography',
                    'Edema_Sonomamography','Vascularity_Sonomamography', 'Elasticity_Sonomamography',
                    'Node_Intramammary_Sonomamography','Node_Axillary_Sonomamography', 'Node_Axillary_Cortex_Sonomamography',
                    'Node_Axillary_Hilum_Sonomamography','Node_Axillary_Vascularity_Sonomamography',
                    'Other_Features_Sonomamography', 'DistancefromNipple_SonoMammography',
                    'DistancefromSkin_SonoMammography', 'DistanceFromPectMaj_SonoMammography',
                    'Category_BI_RADS_SonoMammography', 'Detail_BI_RADS_SonoMammography']
    elif module_name == "mri_breast":
        col_list = ['MRI_Breast', 'Date_MRI_Breast', 'AccessionNumber_MRI_Breast', 'Fibroglandular_Tissue_MRI_Breast',
                    'Background_Paranchymal_Enhancement_Level_MRI_Breast',
                    'Background_Paranchymal_Enhancement_Symmetry_MRI_Breast','Focus_MRI_Breast', 'Mass_MRI_Breast',
                    'Number_Mass_MRI_Breast', 'Mass_Location_MRI_Breast', 'Mass_Location_Quadrant_MRI_Breast',
                    'Mass_Shape_MRI_Breast', 'Mass_Margin_MRI_Breast', 'Mass_Internal_Enhancement_Char_MRI_Breast',
                    'Asso_features_Nipple_retraction_MRI_Breast', 'Asso_features_Nipple_invasion_MRI_Breast',
                    'Asso_features_Skin_retraction_MRI_Breast', 'Asso_features_Skin_thickening_MRI_Breast',
                    'Asso_features_Axillary_adenopathy_MRI_Breast', 'Asso_features_PectoralisMuscle_Invasion_MRI_Breast',
                    'Asso_features_ChestWall_Invasion_MRI_Breast', 'Asso_features_Architectural_distortion_MRI_Breast',
                    'Asso_features_Skin_Invasion_MRI_Breast', 'Fat_Lesion_MRI_Breast','Kinetics_Initial_MRI_Breast',
                    'Kinetics_Delayed_MRI_Breast', 'Non_Enhanced_Features_MRI_Breast', 'Implant_MRI_Breast',
                    'Lesion_MRI_Breast', 'Lesion_Location_MRI_Breast','Lesion_Depth_MRI_Breast', 'Lesion_Size_MRI_Breast',
                    'DistancefromSkin_MRI_Breast', 'DistanceFromPectMaj_MRI_Breast', 'Category_BI_RADS_MRI_Breast',
                    'Detail_BI_RADS_MRI_Breast']
    else:
        col_list = ["File_number"]
    return col_list

def names_block(module_name):
    if module_name == "block_report_info":
        col_list = ["Consent_Status_BR","Consent_form_status_BR", "Block_SR_Number", "Biopsy_Block_ID", "No_of_blocks",
                    "Date_of_Biopsy", "Lab_ID", "Biopsy_Type"]
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

def info_print(module_name):
    if module_name == "nut_supplements":
        col_list = ["Nutritional supplements", "Type of Nutritional supplements", "Quantity  of Nutritional supplements",
                    "Duration of use"]
    elif module_name == "phys_act":
        col_list = ["Physical Activity", "Type of Physical Activity", "Frequency of Physical Activity"]
    elif module_name == "med_history":
        col_list = ["Other Medical History", "Type of Medical History", "Date of Diagnosis", "Treatment"]
    elif module_name == "cancer_history":
        col_list = ["Previous Cancer History", "Type of Previous Cancer", "Year of Diagnosis", "Treatment taken",
                    "Details of Treatment taken", "Duration of Treatment"]
    elif module_name == "family_details":
        col_list = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                    "Age at Menarche (yrs)", "Menopausal Status", "Age at Menopause (yrs)", "Date of last menstrual period",
                    "Period Type", "Number of pregnancies", "Pregnancy carried to term (includes abortion after 6 months)", "Number of abortions", "Age of first child",
                    "Age at first pregnancy", "Age of last child", "Age at last pregnancy", "Twice births in year",
                    "Breast feeding", "Child Breast feeding", "Duration of Breast feeding", "Breast Usage for Breast feeding",
                    "Fertility treatment", "Type of fertility treatment", "Details of fertility treatment",
                    "Cycles of fertility treatment", "Successful fertility treatment","Type of birth control used",
                    "Details of birth control used", "Duration of birth control"]
    elif module_name == "breast_symptoms":
        col_list = ["Right Breast symptoms", "Duration of symptoms in Right Breast", "Left Breast symptoms",
                    "Duration of symptoms in Left Breast", "Other Symptoms in Right Breast",
                    "Duration of other symptoms in Right Breast", "Other Symptoms in Left Breast",
                    "Duration of other symptoms in Left Breast", "Metastasis Symptoms"]
    elif module_name == "habits":
        col_list = ["Diet", "Alcohol Consumption", "Alcohol Consumption since age (yrs)", "Quantity of alcohol consumed per week",
                    "Duration of alcohol consumption", "Additional comments", "Tobacco", "Mode of Exposure to Tobacco", "Type of Passive Tobacco Exposure",
                    "Type of tobacco consumed/exposed to", "Tobacco consumption since age (yrs)", "Frequency of Tobacco consumption","Quantity of tobacco consumed per week",
                    "Duration tobacco of tobacco consumption", "Additional Comments", "Other Deleterious Habits"]
    elif module_name == "det_by":
        col_list = ["Current Breast Cancer Detected By", "Date of Current Breast Cancer Detection"]
    elif module_name == "family_cancer":
        col_list = ["Family Cancer History", "Type of Cancer | Degree of Relation | Type of Relation | Age at diagnosis"]
    elif module_name == "bio_info":
        col_list = ["Medical Record Number", "Name", "Aadhaar Card Number", "Date of First Visit", "Permanent Address",
                    "Current Address", "Phone Number", "Email ID", "Gender", "Age (yrs)", "Date of Birth",
                    "Place of Birth", "Height (cm)", "Weight (kg)", "BMI"]
    else:
        col_list = "Module not found"
    return col_list

def info_print_all (module_name):
    if module_name == "Print_edit":
        nut_supp = ["Nutritional supplements", "Type of Nutritional supplements", "Quantity  of Nutritional supplements",
                    "Duration of use"]
        phys_act = ["Physical Activity", "Type of Physical Activity", "Frequency of Physical Activity"]
        med_history = ["Other Medical History", "Type of Medical History", "Date of Diagnosis", "Treatment"]
        cancer_history = ["Previous Cancer History", "Type of Previous Cancer", "Year of Diagnosis", "Treatment taken",
                    "Details of Treatment taken", "Duration of Treatment"]
        family_details = ["Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons",
                    "Age at Menarche (yrs)", "Menopausal Status", "Age at Menopause (yrs)", "Date of last menstrual period",
                    "Period Type", "Number of pregnancies", "Pregnancy carried to term (includes abortion after 6 months)", "Number of abortions", "Age of first child",
                    "Age at first pregnancy", "Age of last child", "Age at last pregnancy", "Twice births in year",
                    "Breast feeding", "Child Breast feeding", "Duration of Breast feeding", "Breast Usage for Breast feeding",
                    "Fertility treatment", "Type of fertility treatment", "Details of fertility treatment",
                    "Cycles of fertility treatment", "Successful fertility treatment","Type of birth control used",
                    "Details of birth control used", "Duration of birth control"]
        breast_symptoms = ["Right Breast symptoms", "Duration of symptoms in Right Breast", "Left Breast symptoms",
                    "Duration of symptoms in Left Breast", "Other Symptoms in Right Breast",
                    "Duration of other symptoms in Right Breast", "Other Symptoms in Left Breast",
                    "Duration of other symptoms in Left Breast", "Metastasis Symptoms"]
        habits = ["Diet", "Alcohol Consumption", "Alcohol Consumption since age (yrs)", "Quantity of alcohol consumed per week",
                    "Duration of alcohol consumption", "Additional comments", "Tobacco", "Mode of Exposure to Tobacco", "Type of Passive Tobacco Exposure",
                    "Type of tobacco consumed/exposed to", "Tobacco consumption since age (yrs)", "Frequency of Tobacco consumption","Quantity of tobacco consumed per week",
                    "Duration tobacco of tobacco consumption", "Additional Comments", "Other Deleterious Habits"]
        det_by = ["Current Breast Cancer Detected By", "Date of Current Breast Cancer Detection"]
        family_cancer = ["Family Cancer History", "Type of Cancer | Degree of Relation | Type of Relation | Age at diagnosis"]
        bio_info = ["Medical Record Number", "Name", "Aadhaar Card Number", "Date of First Visit", "Permanent Address",
                    "Current Address", "Phone Number", "Email ID", "Gender", "Age (yrs)", "Date of Birth",
                    "Place of Birth", "Height (cm)", "Weight (kg)", "BMI"]
        col_list =  bio_info + nut_supp + phys_act + habits + family_details + med_history +cancer_history + \
                    family_cancer + det_by + breast_symptoms
    else:
        col_list = "Module not found"
    return col_list
def mammo_tables(table_name):
    if table_name == "SonnoMammography_Multiple_Mass":
        col_list = ["File_number", "Mass_ID", 'Mass_Location', 'Mass_Location_Quadrant','Mass_Location_Clock',
                    'Mass_Shape','Mass_Orientation','Mass_Margin', 'Mass_Echo', 'Mass_Posterior']
    elif table_name == "Mammography_Multiple_Mass":
        col_list = ["File_number", "Mass_ID", 'Mass_Location', 'Mass_Location_Quadrant', 'Mass_Shape', 'Mass_Margin',
                    'Mass_Density']
    elif table_name == "Calcification_Mammography":
        col_list = ["File_number", "Calcification_ID", 'Calcification_Location', 'Calcification_Location_Quadrant',
                    'Calcification', 'Calcification_Type', 'Calcification_Distribution']
    elif table_name == "MRI_Multiple_Mass":
        col_list = ["File_number", "Mass_ID", 'Mass_Location', 'Mass_Location_Quadrant', 'Mass_Shape', 'Mass_Margin',
                    'Mass_Internal_Enhancement_Char']
    else:
        col_list = "File_number"
    return col_list