import textwrap
import datetime

def ask_option(category, options):
    option_remove = ["Data not available", "Other"]
    for remove in option_remove:
        try:
            options.remove(remove)
        except:
            options
    options = options + ["Data not in Report", "Requires Follow-up", "Requires Specialist Input", 'Other']
    option_list = []
    val = []
    for index in range(0, len(options)):
        var = [(str(index + 1) + ". " + options[index])]
        val.append(str(index + 1))
        option_list.append(var)
    option_flat = [item for sublist in option_list for item in sublist]
    option_flat = " ".join(option_flat)
    check = False
    while not check:
        print("\n","Enter " + category, "\n")
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=option_flat)
        print(string, "\n")
        answer = input("Enter option number: ")
        check = answer in set(val)
    ans_int = int(answer) - 1
    option_ = options[ans_int]
    if option_ == "Other":
        option = input("Details: ")
    else:
        option = option_
    return option

def ask_y_n(question: object, yes_ans: object = True, no_ans: object = False) -> object:
    option_list = ["1. Yes", "2. No"]
    option_flat = " ".join(option_list)
    check = False
    while not check:
        print("\n",question)
        print("\n", option_flat, "\n")
        answer = input("Enter option number: ")
        check = answer in {"1", "2"}
    if answer == "1":
        option = yes_ans
    else:
        option = no_ans
    return option


def join_lists(all_data, sep):
    data_return = []
    for index in all_data:
        data_joint = sep.join(index)
        data_return.append(data_joint)
    return data_return

def ask_y_n_na(question, yes_ans = "Yes", no_ans = "No",
               na_ans = "Requires Follow-up"):
    option_flat = "1. Yes 2. No 3. " + na_ans
    check = False
    while not check:
        print("\n",question)
        print("\n", option_flat, "\n")
        answer = input("Enter option number: ")
        check = answer in {"1", "2", "3"}
    if answer == "1":
        option = yes_ans
    elif answer == "2":
        option = no_ans
    else:
        option = na_ans
    return option

def ask_option_y_n(question, yes_ans = "Yes", no_ans = "No",
               ans_3 = "Requires Follow up", ans_4 = "Requires Specialist Input"):
    option_list = ["1. Yes", "2. No", "3. Requires Follow up", "4. Requires Specialist Input"]
    option_flat = " ".join(option_list)
    check = False
    while not check:
        print("\n",question)
        print("\n", option_flat, "\n")
        answer = input("Enter option number: ")
        check = answer in {"1", "2", "3", "4"}
    if answer == "1":
        option = yes_ans
    elif answer == "2":
        option = no_ans
    elif answer == "3":
        option = ans_3
    else:
        option = ans_4
    return option

def check_date(date_string):
    checked_date = False
    while not checked_date:
        isValidDate = True
        error = '\nDate entered is not valid\nDate must be in dd/mm/yyyy format or NA\n'
        inputDate = input('\n' + date_string + '\n')
        if inputDate !='NA':
            try:
                day, month, year = inputDate.split('/')
                try:
                    datetime.datetime(int(year), int(month), int(day))
                except ValueError:
                    print(error)
                    isValidDate = False
            except ValueError:
                print (error)
                isValidDate = False
            if (isValidDate):
                checked_date = datetime.datetime.today() > datetime.datetime(int(year), int(month), int(day))
                if not checked_date:
                    print (error)
        else:
            checked_date= ask_y_n('Date is NA. Is that correct?')
    return inputDate

def edit_table(df, id_col, df_col):
    print(df)
    check = ask_y_n("Are entries correct?")
    if not check:
        to_correct = ask_y_n("Correct entire table?")
        if to_correct:
            return to_correct, df
        else:
            id_list = list(df[id_col])
            to_do = True
            while to_do:
                id = input("Enter " + id_col + "to change: ")
                index = id_list.index(id)
                print(df.loc[index, :])
                col_change = ask_option("Name of column to change", df_col)
                new_val = input("Enter correct value for " + col_change + ' for ' + id)
                df.loc[index, col_change] = new_val
                print(df)
                to_do = ask_y_n("Make more changes to " + id_col + ' ' + id + '?')
            to_correct = False
            return to_correct, df


def ask_list(category, options):
    option_list = []
    val = []
    i=1
    for option in options:
        var = [(str(i) + ". " + option)]
        val.append(str(i))
        option_list.append(var)
        i = i+1
    option_flat = [item for sublist in option_list for item in sublist]
    option_flat = " ".join(option_flat)
    check = False
    while not check:
        print("\n", "Enter " + category, "\n")
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=option_flat)
        print(string, "\n")
        answer = input("Enter option number: ")
        check = answer in set(val)
    ans_int = int(answer) - 1
    option = options[ans_int]
    return option