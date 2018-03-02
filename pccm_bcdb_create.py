import sqlite3
from add_update_sql import add_columns
from datetime import date
import os.path
import pccm_names
folder = "DB"
db_name = "PCCM_BreastCancerDB_" + str(date.today()) + '.db'
path = os.path.join(folder, db_name)

if os.path.isfile(path):
    print (path + " file already exists")
else:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    table_name1 = "Patient_Information_History"
    columns1 = "File_number"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name1, nf=columns1))
    module_names = ["bio_info", "phys_act", "habits", "nut_supplements", "family_details", "med_history",
                    "cancer_history", "family_cancer", "det_by", "breast_symptoms"]
    for index in module_names:
        col_name = pccm_names.names_info(index)
        add_columns(cursor, table_name1, col_name)

    table_name9 = "Clinical_Exam"
    columns9 = "File_number"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name9, nf=columns9))
    module_names = ["clinical_exam_initial", "nipple_cytology", "mammography", "tomosynthesis", "abvs", "sonomammo",
                    "mri_breast_axilla"]
    for index in module_names:
        col_name = pccm_names.names_clinical(index)
        add_columns(cursor, table_name9, col_name)

    table_name10 = "Block_Report_Data"
    columns10 = "File_number"
    cursor.execute('CREATE TABLE {tn} ({nf})' \
                   .format(tn=table_name10, nf=columns10))
    module_names = ['block_report_info', 'tumour_biopsy_data', 'lymphnode_biopsy', 'surgery_info', 'surgery_block',
                    'node_block', 'path_stage']
    for index in module_names:
        col_name = pccm_names.names_block(index)
        add_columns(cursor, table_name10, col_name)

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
