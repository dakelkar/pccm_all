import sqlite3
from add_update_sql import add_columns
from datetime import date
import os.path

folder = "DB"
db_name = "PCCM_BreastCancerDB6_" + str(date.today()) + '.db'
path = os.path.join(folder, db_name)

if os.path.isfile(path):
    print (path + " file already exists")
else:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    table_name1 = "Patient_Information_History"
    columns1 = "File_number, MR_number, Name, Consent, Aadhaar_Card, FirstVisit_Date, Permanent_Address, Current_Address, Phone, Email_ID, " \
       "Gender, Age_yrs, Date_of_Birth, Place_Birth, Height_cm, Weight_kg, BMI"
    cursor.execute(f'CREATE TABLE {table_name1} ({columns1})')

    phys_act = "Physical_Activity_y_n", "Type_Physical_Activity", "Frequency_Physical_Activity"
    add_columns(cursor, table_name1, phys_act)

    habits = "Diet", "Alcohol_y_n", "Alcohol_Consumption_age_yrs", "Quantity_alcohol_per_week", "Duration_alcohol", \
             "Comments_alcohol", "Tobacco_y_n", "Type_tobacco", "Tobacco_consumption_age_yrs", \
             "Quantity_tobacco_per_week", "Duration_tobacco", "Comments_tobacco", "Other_Deleterious_Habits"
    add_columns(cursor, table_name1, habits)

    nut_supp = "Nutritional_supplements_y_n", "Type_Nutritional_supplements", "Quantity_Nutritional_supplements", \
			            "Duration_Nutritional_supplements",
    add_columns(cursor, table_name1, nut_supp)

    family_details = "Marital_Status", "Siblings", "Sisters", "Brothers", "Children", "Daughters", "Sons"
    add_columns(cursor, table_name1, family_details)

    repro_details = "Menarche_yrs", "Menopause_Status", "Age_at_Menopause_yrs", "Date_last_menstrual_period", "Period_Type", \
                    "Number_pregnancies", "Pregnancy_to_term", "Number_abortions", "Age_first_child", "Age_first_pregnancy", \
                    "Age_last_child", "Age_last_pregnancy", "Two_births_in_year", "Breast_feeding", \
                    "Child_Breast_feeding", "Duration_Breast_feeding", "Breast_Usage_Breast_feeding", \
                    "Type_birth_control_used", "Details_birth_control", "Duration_birth_control"
    add_columns(cursor, table_name1, repro_details)

    other_tables_y_n =  "Any_Other_Medical_History_y_n", "Type_Any_Other_Medical_History", \
                       "Diagnosis_Date_Any_Other_Medical_History", "Treatment_Any_Other_Medical_History",\
                       "Previous_Cancer_History_y_n", "Type_Previous_Cancer", "Year_Diagnosed_Previous_Cancer", \
                       "Treatment_Previous_Cancer", "Treatment_Type_Previous_Cancer",\
                       "Treatment_Duration_Previous_Cancer","FamilyCancer_history_y_n", \
                       "Type_DegreeRelation_TypeRelation_Age_FamilyCancer"
    add_columns(cursor, table_name1, other_tables_y_n)

    symptoms = "Current_Breast_Cancer_Detected_By", "Current_Breast_Cancer_Detected_Date", "RB_symptoms", \
               "RB_symptoms_duration", "LB_symptoms", "LB_symptoms_duration", "RB_Other_Symptoms", \
			  "RB_Other_Symptoms_duration", "LB_Other_Symptoms", "LB_Other_Symptoms_duration", "Metatasis_Symptoms"
    add_columns(cursor, table_name1, symptoms)
    table_name9 = "Clinical_Exam"
    columns9 = "File_number"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name9, nf=columns9))

    clinical_exam = 'Provisional_Diagnosis_Clinical_Examination_CE', 'Lump_Palpable_CE', 'Lump_Location_CE', \
                    'Lump_Size_CE', 'Lump_Number_CE', 'Lump_Consistency_CE', 'Lump_Fixity_CE', 'Mastitis_CE', \
                    'Mastitis_type_CE', 'Tenderness_CE', 'Nipple_Retraction_CE', 'Nipple_Discharge_CE', \
                    'Nipple_Discharge_Type_CE', 'Skin_changes_CE', 'Skin_change_type_CE', \
                    'Palpable_axillary_nodes_CE', 'Palpable_axillary_nodes_number_CE', \
                    'Palpable_axillary_nodes_size_CE', 'Palpable_axillary_nodes_fixity_CE', \
                    'Palpable_supraclavicular_nodes_CE', 'Palpable_supraclavicular_nodes_number_CE', \
                    'Palpable_supraclavicular_nodes_size_CE', 'Palpable_supraclavicular_nodes_fixity_CE', \
                    'Contralateral_Breast_CE', 'Edema_arm_CE', 'RightArm_Circumference_cm_CE', \
                    'RightArm_UpperLimbVolume_cc_CE', 'RightArm_ElbowDistance_cm_CE', 'LeftArm_Circumference_cm_CE',\
                    'LeftArm_UpperLimbVolume_cc_CE', 'LeftArm_ElbowDistance_cm_CE'
    add_columns(cursor, table_name9, clinical_exam)

    nipple_cytology =  "Nipple_Cytology", "Date_Nipple_Cytology", "Number_Nipple_Cytology", "Report_Nipple_Cytology"
    add_columns(cursor, table_name9, nipple_cytology)

    mammography = 'DiagnosisLocation_Mammography', 'First_Mammography', 'LatestDate_Mammography', 'Number_Mammography',\
              'PreviousDate_Mammography', 'Diagnosis_Mammography', 'Date_Diagnosis_Mammography', \
              'AccessionNumber_Mammography', 'BreastDensity_Mammography','Lesion_Mammography', \
              'LesionLocation_Mammography', 'Shape_Mammography', 'Size_Mammography', 'Margin_Mammography', \
              'Density_Mammography', 'Calcification_Mammography', 'Calcification_Implication_Mammography', \
              'Calcification_Distribution_Mammography', 'Architecture_Mammography', 'Asymmetry_Mammography', \
              'IntraMammaryLN_Mammography', 'SkinLesion_Mammography', 'DilatedDuct_Mammography', \
              'Features_SkinRetraction_Mammography', 'Features_NippleRetraction_Mammography', \
              'Features_SkinThickening_Mammography', 'Features_TrabecularThickening_Mammography', \
              'Features_AxillaryLymphadenopathy_Mammography', 'Features_ArchitecturalDistortion_Mammography', \
              "Features_Calcification_Mammography", 'SecondaryLesion_ContralateralBreast_Mammography', \
              'DistancefromSkin_Mammography', 'DistanceFromPectMaj_Mammography', 'BIRADS_Mammography'

    add_columns(cursor, table_name9, mammography)

    tomosynthesis = "Tomosynthesis_3D", "Date_Tomosynthesis", "Accession_Tomosynthesis", "Lesion_Tomosynthesis",\
                    "Lesion_Location_Tomosynthesis", "Size_Tomosynthesis", "Distance_Tomosynthesis", \
                    "Distance_PectMajor_Tomosynthesis", "Diagnosis_Tomosynthesis"

    add_columns(cursor, table_name9, tomosynthesis)

    abvs = "Automated_Breast_Volume_Scanner_ABVS", "Date_ABVS", "Accession_ABVS", "Lesion_ABVS","Lesion_Location_ABVS","Size_ABVS", \
              "Distance_ABVS", "Distance_PectMajor_ABVS", "Diagnosis_ABVS"
    add_columns(cursor, table_name9, abvs)

    sonomammo = 'SonoMammography', 'Date_SonoMammography', 'AccessionNumber_SonoMammography', \
              'Number_SonoMammography', 'Lesion_SonoMammography', 'Lesion_Location_SonoMammography', \
              'Shape_SonoMammography', 'Size_SonoMammography', 'Orientation_SonoMammography', \
              'Margins_SonoMammography', 'Echo_SonoMammography', 'Postacoustic_SonoMammography', \
              'Calcification_SonoMammography', 'ArchitecturalDistoration_SonoMammography', \
              'SkinChanges_SonoMammography', 'Edema_SonoMammography', 'Vascularity_SonoMammography', \
              'LymphNodes_SonoMammography', 'DistanceNipple_SonoMammography', 'DistanceSkin_SonoMammography', \
              'Distance_PectMajor_SonoMammography', 'Diagnosis_SonoMammography'
    add_columns(cursor, table_name9, sonomammo)

    mri_axilla = 'MRI_Breast_Axilla', 'Date_MRI_Breast_Axilla', 'AccessionNumber_MRI_Breast_Axilla', \
                 'Lesion_MRI_Breast_Axilla', 'LesionLocation_MRI_Breast_Axilla', 'Size_MRI_Breast_Axilla', \
                 'DistancefromSkin_MRI_Breast_Axilla', 'DistanceFromPectMaj_MRI_Breast_Axilla', \
                 'Diagnosis_MRI_Breast_Axilla'

    add_columns(cursor, table_name9, mri_axilla)

    table_name10 = "Block_Report_Data"
    columns10 = "File_number"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name10, nf=columns10))

    block_report_info = "Block_SR_Number", "Biopsy_Block_ID", "No_of_blocks", "Date_of_Biopsy", "Lab_ID", "Biopsy_Type"
    add_columns(cursor, table_name10, block_report_info)

    tumour_biopsy = "Tumour_biopsy_diagnosis", "Tumour_biopsy_diagnosis_grade", "Tumour_biopsy_ER", \
                    "Tumour_biopsy_ER_Percent", "Tumour_biopsy_PR", "Tumour_biopsy_PR_Percent", "Tumour_biopsy_HER2", \
                    "Tumour_biopsy_HER2_Grade", "Tumour_biopsy_FISH", "Tumour_biopsy_Ki67_Percent"
    add_columns(cursor, table_name10, tumour_biopsy)

    lymphnode_biopsy = "Lymph_Node_biopsy_FNAC", "Lymph_Node_biopsy_location", "Lymph_Node_biopsy_diagnosis"
    add_columns(cursor, table_name10, lymphnode_biopsy)

    surgery_info = "Surgical_Block_ID", "Surgery_Block_Location", "Surgery_No_of_blocks", "Block_Source", "Tumor_block_ref", "Nodes_block_ref", \
              "Ad_Normal_block_ref", "Reduction_tissue_block_ref", "Date_of_Surgery", "Name_Surgeon", "Hospital_ID", \
              "Lesion_Side", "Type_surgery", "Response_surgery"
    add_columns(cursor, table_name10, surgery_info)

    surgery_block = "Tumour_size_Surgery_Block_Report", "Grade_Surgery_Block_Report", "Diagnosis_Surgery_Block_Report", \
              "DCIS_Percent_Surgery_Block_Report", "DCIS_Invasion_Surgery_Block_Report", \
              "Perineural_Invasion_Surgery_Block_Report", "Necrosis_Surgery_Block_Report", \
              "Lymphovascular_Invasion_Surgery_Block_Report", "Margins_Surgery_Block_Report", "Surgery_Block_Report"
    add_columns(cursor, table_name10, surgery_block)

    node_block = "Sentinel_Node_Block_Report", "Sentinel_Node_Number_Removed", "Sentinel_Node_Number_Positive",\
                 "Sentinel_Node_Block_Report_Number", "Axillary_Node_Block_Report", "Axillary_Node_Number_Removed", \
                 "Axillary_Node_Number_Positive", "Axillary_Node_Block_Report_Number", "Apical_Node_Block_Report", \
                 "Apical_Node_Number_Removed", "Apical_Node_Number_Positive", "Apical_Node_Block_Report_Number", \
                 "Perinodal_Spread_Node_Block_Report", "Supraclavicular_Involved_Node_Block_Report"
    add_columns(cursor, table_name10, node_block)

    staging = "Pathological_Staging_pT", "Pathological_Staging_pN", "Pathological_Staging_M", \
              "Pathological_Staging_P_Stage", "Clinical_Staging"
    add_columns(cursor, table_name10, staging)

# additional tables
    table_name2 = "General_Medical_History"
    columns2 = "File_number, Condition, Diagnosis_date, Treatment"

    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name2, nf=columns2))
    table_name3 = "Family_Cancer_History"
    columns3 = 'File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs'
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name3, nf=columns3))
    table_name4 = "Previous_Cancer_History"
    columns4 = "File_number, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, Duration_Surgery, Radiation," \
               "Type_Radiation,Duration_Radiation,Chemotherapy,Type_Chemotherapy,Duration_Chemotherapy,Hormone," \
               "Type_Hormone,Duration_Hormone,Alternative,Type_Alternative,Duration_Alternative,HomeRemedy," \
               "Type_HomeRemedy,Duration_HomeRemedy"

    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name4, nf=columns4))
    table_name5 = "Nutritional_Supplements"
    columns5 = "File_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
               "Duration_nutritional_supplements"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name5, nf=columns5))
    table_name7 = "Physical_Activity"
    columns7 = "File_number, Type_activity, Frequency_activity"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name7, nf=columns7))
    table_name8 = "Breast_Feeding"
    columns8 = "File_number, Child_number, Feeding_duration, Breast_usage_feeding"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name8, nf=columns8))
    conn.commit()
    print (path + (" file created"))
    conn.close()
