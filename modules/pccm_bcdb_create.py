import sqlite3
from sql.add_update_sql import add_columns, table_check
from datetime import date
import os
import modules.pccm_names as pccm_names


folder = "d:/OneDrive/repos/pccm_db/main/DB"
db_name = "PCCM_BreastCancerDB_Test_" + str(date.today()) + '.db'

path = os.path.join(folder, db_name)

conn = sqlite3.connect(path)
cursor = conn.cursor()
file_number = "File_number"
table = "Patient_Information_History"
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})'\
                   .format(tn=table, nf=file_number))
    module_names = ["bio_info", "phys_act", "habits", "nut_supplements", "family_details", "med_history",
                    "cancer_history", "family_cancer", "det_by", "breast_symptoms"]
    for index in module_names:
        col_name = pccm_names.names_info(index)
        add_columns(cursor, table, col_name)

table = "Biopsy_Report_Data"
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    module_names = ["biopsy_report_info", "tumour_biopsy_data"]
    for index in module_names:
        col_name = pccm_names.names_biopsy_new(index)
        add_columns(cursor, table, col_name)

table = "Surgery_Block_Report_Data"
if table_check(cursor, table) == 0:
    cursor.execute('CREATE TABLE {tn}({nf})' .format(tn=table, nf=file_number))
    module_names = ["surgery_block_information_1","surgery_block_information_2", "surgery_block_information_3",
                    "path_stage"]
    for index in module_names:
        col_name = pccm_names.names_surgery(index)
        add_columns(cursor, table, col_name)

table = "Radiology"
if table_check(cursor, table) == 0:
    module_names = ["mammography", "abvs", "sonomammo",
                    "mri_breast"]
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    for index in module_names:
        col_name = pccm_names.names_radio(index)
        add_columns(cursor, table, col_name)

table = "Surgery_Report"
if table_check(cursor, table) == 0:
    module_names = ["surgery_information", "node_excision","post_surgery"]
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    for index in module_names:
        col_name = pccm_names.names_surgery_information(index)
        add_columns(cursor, table, col_name)

table = "General_Medical_History"
if table_check(cursor, table) == 0:
    columns2 = "File_number, Condition, Diagnosis_date, Treatment"
    cursor.execute('CREATE TABLE {tn}({nf})' \
                   .format(tn=table, nf=columns2))

table = "Family_Cancer_History"
if table_check(cursor, table) == 0:
    columns3 = 'File_number, Type_Cancer, Relation_to_Patient, Type_Relation, Age_at_detection_yrs'
    cursor.execute('CREATE TABLE {tn}({nf})' \
                   .format(tn=table, nf=columns3))

table = "Previous_Cancer_History"
if table_check(cursor, table) == 0:
    columns4 = "File_number, Type_Cancer, Year_diagnosis, Surgery, Type_Surgery, Duration_Surgery, Radiation," \
               "Type_Radiation,Duration_Radiation,Chemotherapy,Type_Chemotherapy,Duration_Chemotherapy,Hormone," \
               "Type_Hormone,Duration_Hormone,Alternative,Type_Alternative,Duration_Alternative,HomeRemedy," \
               "Type_HomeRemedy,Duration_HomeRemedy"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns4))

table = "Nutritional_Supplements"
if table_check(cursor, table) == 0:
    columns5 = "File_number, Type_nutritional_supplements, Quantity_nutritional_supplements_per_day, " \
               "Duration_nutritional_supplements"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns5))

table = "Physical_Activity"
if table_check(cursor, table) == 0:
    columns7 = "File_number, Type_activity, Frequency_activity"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns7))

table = "Breast_Feeding"
if table_check(cursor, table) == 0:
    columns8 = "File_number, Child_number, Feeding_duration, Breast_usage_feeding"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=columns8))

table = "NACT_Tox_table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_nact(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))

table = "NACT_Drug_Table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_nact(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))

table = "Neo_Adjuvant_Therapy"
if table_check(cursor, table) == 0:
    module_names = ["Neo_Adjuvant_Therapy", "clip_information"]
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=file_number))
    for index in module_names:
        col_name = pccm_names.names_nact(index)
        add_columns(cursor, table, col_name)

table = "Adjuvant_ChemoTherapy"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_chemotherapy(table))
    cols_file = "File_number, " + column
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))


table = "Chemo_Tox_table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_chemotherapy(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))

table = "Chemo_Drug_Table"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_chemotherapy(table))
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))

table = "Radiotherapy"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.names_radiation())
    cols_file = "File_number, "+column
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))

table = "Follow_up_Data"
if table_check(cursor, table) == 0:
    column = ", ".join(pccm_names.name_follow_up())
    cols_file = "File_number, " + column
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=cols_file))

table = "HormoneTherapy_Survival"
if table_check(cursor, table) == 0:
    column = "File_number"
    cursor.execute('CREATE TABLE {tn}({nf})'.format(tn=table, nf=column))
    module_names = ["hormone", "metastasis"]
    for index in module_names:
        col_name = pccm_names.names_longterm(index)
        add_columns(cursor, table, col_name)

conn.commit()
print(path + " file created")
conn.close()
