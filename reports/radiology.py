from modules.ask_y_n_statement import ask_y_n
from modules.pccm_names import names_radio as names
import modules.ask_y_n_statement as ask_y_n_statement
import sql.add_update_sql as add_update_sql
import additional_tables.radio_tables as radio_tables
from datetime import datetime


def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Radiology(File_number) VALUES ('" + file_number + "')")


def mammography(file_number = 'test'):
    module_name = "mammography"
    check = False
    while not check:
        mammo = ask_y_n_statement.ask_y_n("Are mammography results available for this patient?")
        if not mammo:
            check_mammo = ask_y_n("Is the diagnostic radiological report present?")
            if check_mammo:
                mammo = "Mammography not done for diagnosis"
            else:
                mammo = "Requires Follow-up"
            tomo, mammo_date, mammo_place, mammo_indication, mammo_breast, mass_number, mammo_mass_location, \
            mammo_mass_shape, mammo_mass_margin, mammo_mass_nipple_cm, mammo_mass_size, mammo_mass_size_unit, calc_number, \
            calc_location, calc_type, mammo_birad, mammo_impression, skin_lesion = (mammo,) * 18
        else:
            tomo = ask_y_n_statement.ask_y_n("Have 3D Tomography images also been acquired?")
            if tomo:
                tomo = "Yes"
                print("Please include 3d-Tomo observations in Mammography results")
            else:
                tomo = "No"
            mammo = "Mammography done"
            mammo_date = input("Date of mammography: ")
            mammo_place = ask_y_n("Was exam peformed at PCCM?", yes_ans="PCCM", no_ans="Outside")
            if mammo_place == "Outside":
                mammo_place = input("Please input Radiologist name and place (Name; Place): ")
            mammo_indication = input ("Indication for mammography: ")
            mammo_breast = ask_y_n_statement.ask_option("Details described for", ["Right Breast", "Left Breast", "Bilateral"])
            mammo_mass_location = ask_y_n_statement.ask_y_n("Is there any mass/lesion detected")
            if mammo_mass_location:
                table = "Mammography_Mass"
                mass_number, mammo_mass_location, mammo_mass_shape, mammo_mass_margin, mammo_mass_nipple_cm, \
                mammo_mass_size, mammo_mass_size_unit = radio_tables.multiple_mass(table, mammo_breast)
            else:
                mass_number, mammo_mass_location, mammo_mass_shape, mammo_mass_margin, mammo_mass_nipple_cm, \
                mammo_mass_size, mammo_mass_size_unit= ("No mass detected", )*7
            calc = ask_y_n_statement.ask_y_n("Is Calcification present?")
            if calc:
                calc_number, calc_location, calc_type = radio_tables.cal_table(file_number, mammo_breast)
            else:
                calc_number, calc_location, calc_type = ("No Calcification detected", )*3
            mammo_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/diagnosis?")
            if mammo_birad:
                mammo_birad = radio_tables.birads()
            else:
                mammo_birad = "BI-RAD not assigned in report"
            skin_lesion = input("Please input description of skin lesion if present: ")
            mammo_impression = input("Input Impression(if available): ")
        data_list = [mammo, mammo_date, mammo_place, mammo_indication,mammo_breast, mass_number, mammo_mass_location,
                     mammo_mass_shape, mammo_mass_margin, mammo_mass_nipple_cm, mammo_mass_size, mammo_mass_size_unit, calc_number,
                     calc_location, calc_type, skin_lesion,mammo_birad, mammo_impression, tomo]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return tuple(data_list)


def abvs(file_number):
    module_name = "abvs"
    check = False
    while not check:
        abvs = ask_y_n_statement.ask_y_n("Automated Breast Volume Scanner (ABVS) done?")
        if abvs:
            abvs = "Automated Breast Volume Scanner done"
            abvs_date = input("Date of examination of ABVS: ")
            abvs_acc = input("Accession number of ABVS: ")
            abvs_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                       ["Right Breast", "Left Breast", "Both", "Not present"])
            if abvs_lesion in {"Right Breast", "Left Breast", "Both"}:
                abvs_lesion_data = radio_tables.lesion_location(abvs_lesion)
            else:
                abvs_lesion_data = "NA"
            abvs_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            abvs_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            abvs_pect = input("Distance from Pectoralis Major (cm): ")
            abvs_diagnosis = ask_y_n_statement.ask_option("ABVS Diagnosis",
                                                          ["Normal", "Benign", "Suspicious", "Diagnostic for Cancer"])
        else:
            abvs = "Automated Breast Volume Scanner not done"
            abvs_date, abvs_acc, abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect, \
            abvs_diagnosis = ("NA",) * 8

        data_list = [abvs, abvs_date, abvs_acc, abvs_lesion, abvs_lesion_data, abvs_size, abvs_dist, abvs_pect,
                     abvs_diagnosis]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return tuple(data_list)


def sonomammo(file_number = 'test', user_name = "dk"):
    module_name = "sonomammo"
    check = False
    while not check:
        sonomammo = ask_y_n_statement.ask_y_n("Are sonomammography results available for this patient?")
        if sonomammo:
            sonomammo = "Sono-Mammography done"
            sonomammo_date = input("Date of examination of Sono-mammography: ")
            sonomammo_place = input("")
            sonomammo_breast = ask_y_n_statement.ask_option("Details described for", ["Right Breast", "Left Breast", "Bilateral"])
            mass_sonomammo = ask_y_n_statement.ask_y_n("Is there any mass detected")
            if mass_sonomammo:
                mass_sonomammo = 'Mass/Lesion Detected'
                table = "SonnoMammography_Mass"
                mass_number, sonomammo_mass_location, sonomammo_mass_location_clock, sonomammo_masss_shape, \
                sonomammo_mass_margin, sonomammo_mass_echo, sonomammo_mass_size, sonomammo_mass_size_unit\
                    = radio_tables.multiple_mass(table, sonomammo_breast)
            else:
                mass_sonomammo, mass_number, sonomammo_mass_location, sonomammo_mass_location_clock, \
                sonomammo_masss_shape, sonomammo_mass_margin, sonomammo_mass_echo, sonomammo_mass_size, sonomammo_mass_size_unit = \
                    ("No Mass Detected",) * 9
            sonomammo_calc = ask_y_n_statement.ask_option("Calcification",
                                                          ["Right Breast", "Left Breast", "Bilateral", "Not present", "Other"])
            if sonomammo_calc != "Not present":
                sonomammo_calc_type = ask_y_n_statement.ask_option("Calcification location",
                                                                   ["Calcifications in a mass",
                                                                    "Calcifications outside of a mass",
                                                                    "Intraductal calcifications"])
            else:
                sonomammo_calc_type = "NA"
            sonomammo_vasc = ask_y_n_statement.ask_option("Vascularity",
                                                          ["Absent", "Internal vascularity", "Vessels in rim", "Other"])
            sono_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if sono_birad:
                sonomammo_birad = radio_tables.birads()
            else:
                sonomammo_birad = "NA"
            sonomammo_impression = input("Input Impression(if available): ")
        else:
            check_mammo = ask_y_n("Is the diagnostic radiological report present?")
            if check_mammo:
                sonomammo = "Sonomammography not done for diagnosis"
            else:
                sonomammo = "Requires Follow-up"
            sonomammo_date, sonomammo_breast, mass_sonomammo, mass_number, sonomammo_mass_location, \
            sonomammo_masss_shape, sonomammo_mass_margin, sonomammo_mass_echo, sonomammo_mass_location_clock, \
            sonomammo_mass_size, sonomammo_mass_size_unit, sonomammo_calc, sonomammo_calc_type, \
            sonomammo_vasc,sonomammo_birad, sonomammo_impression \
                = (sonomammo,) * 16
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [sonomammo, sonomammo_date, sonomammo_breast, mass_sonomammo, mass_number, sonomammo_mass_location,
                     sonomammo_mass_location_clock, sonomammo_masss_shape, sonomammo_mass_margin, sonomammo_mass_echo,
                     sonomammo_mass_size, sonomammo_mass_size_unit, sonomammo_calc, sonomammo_calc_type, sonomammo_vasc,
                     sonomammo_birad,sonomammo_impression, user_name, last_update]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return tuple(data_list)


def mri_breast(file_number = 'test', user_name = 'dk'):
    module_name = "mri_breast"
    check = False
    while not check:
        mri_breast = ask_y_n_statement.ask_y_n("Has MRI-Breast been done?")
        if mri_breast:
            mri_breast = "MRI-Breast done"
            mri_breast_date = input("Date of examination of MRI: ")
            mri_breast_acc = input("Accession number of MRI (Include location): ")
            mri_breast_described = ask_y_n_statement.ask_option("Details described for",
                                                                ["Right Breast", "Left Breast", "Bilateral"])
            fgt_mri = ask_y_n_statement.ask_option("Ammount of Fibroglandular Tissue",
                                                   ["a. Almost entirely fat", "b. Scattered fibroglandular tissue",
                                                    "d. Extreme fibroglandular tissue", "Other"])
            bpe_level_mri = ask_y_n_statement.ask_option("Background parenchymal enhancement Level",
                                                         ["Minimal", "Mild", "Moderate", "Marked", "Other"])
            bpe_symm_mri = ask_y_n_statement.ask_option("Background parenchymal enhancement Symmetry",
                                                        ["Symmetric", "Asymmetric", "Other"])
            focus_mri = input("Details of Focus: ")
            mass_mri = ask_y_n_statement.ask_y_n("Are masses detected?")
            if mass_mri:
                mass_mri = "Mass Detected"
                table = "MRI_Mass"
                mri_mass_number, mass_location, mass_shape, mass_margin, mass_internal = \
                    radio_tables.multiple_mass(table, mri_breast_described)
            else:
                mass_mri = "No Mass Detected"
                mri_mass_number, mass_location, mass_quad, mass_shape, mass_margin, mass_internal = ("NA",) * 6
            asso_feat = ["Nipple Retraction", "Nipple Invasion", "Skin Retraction", "Skin Thickening",
                         "Axillary adenopathy", "Pectoralis muscle invasion", "Chest wall invasion",
                         "Architectural Distortion"]
            asso_feat_data = []
            for index in (asso_feat):
                print("Associated feature: " + index)
                print("Detailed description can be added by choosing 'Other'")
                var = ask_y_n_statement.ask_option(index,
                                                   ["Right Breast", "Left Breast", "Both", "Not Present", "Other"])
                asso_feat_data.append(var)
            asso_feat_9 = ask_y_n_statement.ask_option("Associated Feature: Skin Invasion",
                                                       ["Direct invasion", "Inﬂammatory cancer", "Other"])
            asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, \
            asso_feat_8 = asso_feat_data
            fat_lesions = ask_y_n_statement.ask_option("Fat Containing Lesions",
                                                       ["Lymph nodes: Normal", "Lymph nodes: Abnormal", "Fat necrosis",
                                                        "Hamartoma", "Postoperative seroma", "hematoma with fat"])
            mri_breast_kinetics_initial = ask_y_n_statement.ask_option("Kinetic curve assessment Signal intensity "
                                                                       "(SI)/time curve description (Initial Phase)",
                                                                       ["Slow", "Medium", "Fast", "Other"])
            mri_breast_kinetics_delayed = ask_y_n_statement.ask_option("Kinetic curve assessment Signal intensity "
                                                                       "(SI)/time curve description (Delayed Phase)",
                                                                       ["Persistent", "Plateau", "Washout", "Other"])
            mri_breast_non_enhance = ask_y_n_statement.ask_option("Non-enhancing findings",
                                                                  ["Ductal precontrast high signal on T1W", "Cyst",
                                                                   "Postoperative collections (hematoma/seroma)",
                                                                   "Post-therapy skin thickening and trabecular "
                                                                   "thickening","Signal void from foreign bodies, "
                                                                                "clips, etc.", "Other"])
            mri_breast_implant = input("Implant related findings: ")
            mri_breast_lesion = ask_y_n_statement.ask_option("Location of lesion",
                                                             ["Right Breast", "Left Breast", "Both", "Not present"])
            if mri_breast_lesion in {"Right Breast", "Left Breast", "Both"}:
                mri_breast_lesion_location = radio_tables.lesion_location(mri_breast_lesion)
                mri_breast_lesion_depth = input("Lesion depth: ")
            else:
                mri_breast_lesion_location, mri_breast_lesion_depth = ("NA",) * 2
            mri_breast_size = ask_y_n_statement.ask_option("Size of lesion", ["<2 cm", "2-5 cm", ">5 cm", "Other"])
            mri_breast_dist = ask_y_n_statement.ask_option("Distance from Skin (cm)", ["<0.5 cm", ">0.5 cm", "Other"])
            mri_breast_pect = input("Distance from Pectoralis Major (cm): ")
            mri_breast_birad = ask_y_n_statement.ask_y_n("Does the report include a BI-RAD assessment/Diagnosis?")
            if mri_breast_birad:
                mri_breast_birad = radio_tables.birads()
            else:
                mri_breast_birad  = "No BI-RAD Category given in report"
        else:
            mri_breast = "MRI-Breast not done"
            mri_breast_date, mri_breast_acc, fgt_mri, bpe_level_mri, bpe_symm_mri, focus_mri, mass_mri, mri_mass_number, \
            mass_location, mass_quad, mass_shape, mass_margin, mass_internal, asso_feat_1, asso_feat_2, asso_feat_3, \
            asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7, asso_feat_8, asso_feat_9, fat_lesions, \
            mri_breast_lesion, mri_breast_lesion_location, mri_breast_lesion_depth, mri_breast_kinetics_initial, \
            mri_breast_kinetics_delayed, mri_breast_non_enhance, mri_breast_implant, mri_breast_size, mri_breast_dist, \
            mri_breast_pect, mri_breast_birad, mri_breast_described = (mri_breast,) * 35
        last_update = datetime.now().strftime("%Y-%b-%d %H:%M")
        data_list = [mri_breast, mri_breast_date, mri_breast_acc, mri_breast_described, fgt_mri, bpe_level_mri, bpe_symm_mri, focus_mri,
                     mass_mri, mri_mass_number, mass_location, mass_shape, mass_margin, mass_internal,
                     asso_feat_1, asso_feat_2, asso_feat_3, asso_feat_4, asso_feat_5, asso_feat_6, asso_feat_7,
                     asso_feat_8, asso_feat_9, fat_lesions, mri_breast_kinetics_initial, mri_breast_kinetics_delayed,
                     mri_breast_non_enhance, mri_breast_implant, mri_breast_lesion, mri_breast_lesion_location,
                     mri_breast_lesion_depth, mri_breast_size, mri_breast_dist, mri_breast_pect, mri_breast_birad,
                     user_name, last_update]
        columns_list = names(module_name)
        check = add_update_sql.review_input(file_number, columns_list, data_list)
    return tuple(data_list)


def add_data(conn, cursor, file_number, user_name):
    table = "Radiology"
    enter = ask_y_n("Enter Mammography Report?")
    if enter:
        data = mammography(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("mammography"), file_number, data)
    enter = ask_y_n("Enter Automated Breast Volume Scanner")
    if enter:
        data = abvs(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("abvs"), file_number, data)
    enter = ask_y_n("Enter Sono-Mammography")
    if enter:
        data = sonomammo(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, names("sonomammo"), file_number, data)
    enter = ask_y_n("Enter MRI-Breast")
    if enter:
        data = mri_breast(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, names("mri_breast"), file_number, data)


def edit_data(conn, cursor, file_number, user_name):
    table = "Radiology"
    print("Mammography")
    col_list = names("mammography")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = mammography(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Automated Breast Volume Scan")
    col_list = names("abvs")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = abvs(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Sono-Mammography")
    col_list = names("sonomammo")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = sonomammo(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("MRI Breast")
    col_list = names("mri_breast")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = mri_breast(file_number, user_name)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
