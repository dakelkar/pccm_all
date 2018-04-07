def surg_var(var):
    if var == "post_surgery_comp":
        var_list = ["Seroma", "Aspiration", "Drainage", "Flap Necrosis", "Debridemend", "Hematoma",
                         "Surgical Site Infection", "Delayed Wound Healing", "Lymphoedema"]
    elif var == "recurrence_sites":
        var_list = ["Loco-regional", "Breast", "Axilla", "Distant"]
    else:
        var_list = "No such variable"
    return var_list
