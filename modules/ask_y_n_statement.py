import textwrap

def ask_symptom(symp_state):
    symp_y_n = input("Symptom of " + symp_state + "? (y/n) ")
    if str.lower(symp_y_n) == "y":
        symp_breast_right = input("Right Breast y/n: ")
        if str.lower(symp_breast_right) == "y":
            symp_breast_right = symp_state
            symp_duration_right = input("Duration of symptoms in right breast: ")
        else:
            symp_breast_right = None
            symp_duration_right = None
        symp_breast_left = input("Left Breast y/n: ")
        if str.lower(symp_breast_left) == "y":
            symp_breast_left = symp_state
            symp_duration_left = input("Duration of symptoms in left breast: ")
        else:
            symp_breast_left = None
            symp_duration_left = None
    else:
        symp_breast_right = None
        symp_duration_right = None
        symp_breast_left = None
        symp_duration_left = None
    RB = [symp_breast_right, symp_duration_right]
    LB = [symp_breast_left, symp_duration_left]
    data = [RB, LB]
    return data


def get_symptom(symp_state):
    all_data = []
    for index in range(0, len(symp_state)):
        var = ask_symptom(symp_state[index])
        all_data.append(var)
    return all_data


def get_rb_lb(all_data, pos):
    data_list = []
    data_index = len(all_data)
    for index in range(0, data_index):
        var = all_data[index][pos]
        data_list.append(var)
    return (data_list)


def ask_option(category, options):
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
        print("Enter " + category)
        wrapper = textwrap.TextWrapper(width=100)
        string = wrapper.fill(text=option_flat)
        print(string)
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
        print(question)
        print(option_flat)
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
