from modules.ask_y_n_statement import ask_option, ask_y_n
from tables.radio_tables import lesion_location
import sql.add_update_sql as add_update_sql
from modules.pccm_names import names_surgery_information as names
from tables.surgery_tables import surg_var

def file_row(cursor, file_number):
    cursor.execute("INSERT INTO Surgery_Report(File_number) VALUES ('" + file_number + "')")

def clip_information(file_number):
    check = False
    while not check:
        clip = ask_y_n("Was Clip inserted for surgery?")
        if clip:
            clip_number = input("Number of clips inserted: ")
            clip_date = input("Date of clip insertion: ")
        else:
            clip_date, clip_number = ("NA", )*2
        nact = ask_y_n("Did the patient undergo neo-adjuvant therapy?")
        if nact:
            nact_cycle = input('After how many cycles was the clip inserted? ')
        else:
            nact_cycle = "NA"
        data_list = clip_number, clip_date, nact_cycle
        col_list = names("clip_information")
        check = add_update_sql.review_input(file_number, col_list, data_list)
    return data_list

def surgery_information(file_number):
    check = False
    while not check:
        date_surgery = input("Date of surgery: ")
        hosp_surgery = input ("Name of hospital: ")
        hosp_id = input("Patient ID at the hospital: ")
        hosp_ward = input("Name of hospital ward: ")
        date_admin = input("Date of admission: ")
        hosp_anesth = input("Name of Anaesthetist: ")
        hosp_surgeon = input("Name of the Surgeon/s: ")
        lesion = ask_option("Location of lesion", ["Right Breast", "Left Breast", "Both Breasts"])
        lesion_loc = lesion_location(lesion)
        surgery_type = ask_option("Type of Surgery", ["Simple Mastectomy", "Modified Radical Mastectomy",
                      "Skin Sparing Mastectomy", "Skin Reducing Mastectomy/Inferior Dermal Sling",
                      "Areolar Sparing Mastectomy", "Breast Conservation Surgery", "Nipple Sparing Mastectomy",
                      "Nipple Reconstruction"])
        if surgery_type == "Skin Sparing Mastectomy":
            type = ask_option("Type of Skin Sparing Mastectomy", ["Type 1", "Type 2", "Type 3", "Type 4"])
            surgery = surgery_type+": "+type
        elif surgery_type == "Breast Conservation Surgery":
            type = ask_option("Type of Breast Conservation Surgery", ["Wedge Excision", "Central Quadrant Wedge Excision",
                  "Wide Lumpectomy", "Quadrantectomy", "Large Volume Segmental Resection", "Multiple Tumour Excision"])
            surgery = surgery_type+": "+type
        else:
            surgery = surgery_type
        incisions = ask_option("Type of Incision", ["Racket", "Inframammary Fold Incision", "Wise Pattern",
                    "Transverse Oblique", "Transverse", "Circum-areolar", "Lateral Fold", "Axillary Fold", "Sub-mammary"])
        recon = ask_option("Type of reconstruction", ["Flap","Implant","Sling", "Non-sling","Flap+Implant","Not Done",
                                                      "Other"])
        if recon == "Implant":
            type = ask_option("Type of Implant", ["Fixed Volume","Dual"])
            recon = recon+": "+type
        mammo = ask_option("Type of Mammoplasty", ["Type 1 - Simple Mammoplasty", "Type 2 - Volume Displacement",
                            "Type 3 - Therapeutic", "Type 4 Volume Replacement", "Other"])
        if mammo == "Type 2 - Volume Displacement":
            mammo_type = ask_option("Type of flap used", ["Grisotti Flap", "Round Block", "Batwing Procedure"])
            mammo = mammo +": "+mammo_type
        elif mammo == "Type 3 - Therapeutic":
            mammo_plan = ask_option("Plan of mammoplasty", ["Wise pattern", "Vertical Scar"])
            mammo_done = ask_option("Pedicle type", ["Lower Pedicle", "Superior Pedicle", "Superio-medial Pedicle",
                                                     "Lateral Pedicle", "Dual Pedicle", "Superio-medial Pedicle",
                                                     "Lateral Pedicle", "Superior", "Other"])
            mammo = mammo+": "+mammo_plan+"; "+mammo_done
        elif mammo == "Type 4 Volume Replacement":
            mammo_volume = ask_option("Tyep of replacement used", ["Local Flaps", "LD flaps", "Mini LD", "Full LD",
                                                                   "Muscle Sparing", "TRAM"])
            mammo = mammo + ": " + mammo_volume
        mammo_guide = ask_option("Surgery guided by", ["Palpation", "USG guided", "Wire placement guided"])
        surgery_contra = ask_y_n("Surgery on contralateral side?")
        if surgery_contra:
            surgery_contra = input("Type of surgery: ")
        else:
            surgery_contra = "No contralateral surgery"
        surgery_notes = input("Surgery Notes: ")
        data_list = [date_surgery, hosp_surgery, hosp_id, hosp_ward, date_admin, hosp_anesth, hosp_surgeon, lesion_loc,
                     surgery, incisions, recon, mammo, mammo_guide, surgery_contra, surgery_notes]
        col_list = names("surgery_information")
        check = add_update_sql.review_input(file_number, col_list, data_list)
    return data_list

def post_surgery(file_number):
    check = False
    while not check:
        chemo = ask_y_n("Is chemotherapy planned?", "Chemotherapy planned", "No Chemotherapy")
        radio = ask_y_n("Is radiotherapy planned?", "Radiotherapy planned", "No Radiotherapy")
        other = ask_y_n("Are there any other post-surgery plans")
        if other:
            other = input("Please specify other post-surgery plans: ")
        else:
            other = "No other post surgery plans"
        drain = input("Drain removal date: ")
        total_drain = input("Total drain days: ")
        post_comp = ask_y_n("Did post-surgery complications occur?")
        if post_comp:
            post_surgery_comp = []
            day_add = True
            while day_add:
                comp = surg_var("post_surgery_comp")
                day = "Day "+input("Days post surgery: ")
                post_surgery_day = []
                for i in comp:
                    data = ask_y_n("On "+str(day)+ " did post surgery complication "+i+" occur?")
                    if data:
                        post_surgery_day.append(i)
                post_surgery_day = day+": "+("; ".join(post_surgery_day))
                if post_surgery_day == []:
                    post_surgery_day = "NA"
                post_surgery_comp.append(post_surgery_day)
                day_add = ask_y_n("Add another day for post surgery complications? ")
            post_comp = "|".join(post_surgery_comp)
        else:
            post_comp = "NA"
        recur = ask_y_n("Did recurrence occur post surgery?")
        if recur:
            recur_all = []
            late_add = True
            recur = surg_var("recurrence_sites")
            while late_add:
                day = "Day " + input("Days post surgery: ")
                recur_day = []
                for i in recur:
                    data = ask_y_n("On " + str(day) + " did "+i+" recurrence occur?")
                    if data:
                        recur_day.append(i)
                recur_day = day + ": "+ ("; ".join(recur_day))
                if recur_day == []:
                    recur_day = "NA"
                recur_all.append(recur_day)
                late_add = ask_y_n("Add another day for post surgery complications? ")
            recur = "|".join(recur_all)
        else:
            recur = "NA"
        opd = input("Please input OPD notes (if any): ")
        data_list = [chemo, radio, other,drain, total_drain,post_comp,recur, opd]
        col_list = names("post_surgery")
        check = add_update_sql.review_input(file_number, col_list, data_list)
    return data_list

def add_data(conn, cursor, file_number):
    table = "Surgery_Report"
    file_row(cursor, file_number)
    enter = ask_y_n("Enter Clip information?")
    if enter:
        data = clip_information(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("clip_information"), file_number, data)
    enter = ask_y_n("Enter Surgery Information?")
    if enter:
        data = surgery_information(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("surgery_information"), file_number, data)
    enter = ask_y_n("Enter Details of Post-Surgery complications ?")
    if enter:
        data = post_surgery(file_number)
        add_update_sql.update_multiple(conn, cursor, table, names("post_surgery"), file_number, data)

def edit_data(conn, cursor, file_number):
    table = "Surgery_Report"
    print("Clip information")
    col_list = names("clip_information")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = clip_information(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Surgery Information")
    col_list = names("surgery_information")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = surgery_information(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
    print("Post-Surgery complications")
    col_list = names("post_surgery")
    enter = add_update_sql.review_data(conn, cursor, table, file_number, col_list)
    if enter:
        data = post_surgery(file_number)
        add_update_sql.update_multiple(conn, cursor, table, col_list, file_number, data)
