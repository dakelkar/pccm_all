import datetime

def check_date(date_string):
    inputDate = input(date_string)
    day, month, year = inputDate.split('/')
    isValidDate = True
    checked_date = False
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    if (isValidDate):
        checked_date= datetime.datetime.today() > input_date
    return checked_date

