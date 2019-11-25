from Add.add import correct_name_surname
from datetime import date, datetime


def show_age(pb):
    print("********* To receive the age follow the instructions *********")
    print("******************* Please, enter the name *******************")
    name = input()
    print("******************* Please, enter the surname *******************")
    surname = input()
    result = find_name_surname(pb, name, surname)
    if result is None:
        return
    try:
        date_of_birth = datetime.strptime(result["Date"][0], '%d.%m.%Y')
        days_in_year = 365.2425
        age = int((datetime.now() - date_of_birth).days / days_in_year)
        print(name, surname, ": age -", age)
    except:
        print("***Error***")
        return


def find_name_surname(pb, name, surname):
    name = correct_name_surname(name)
    surname = correct_name_surname(surname)
    if len(name) == 0 or len(surname) == 0:
        print("*~~~~~~~~ Incorrect name or surname ~~~~~~~~")
        return
    try:
        result = pb[(pb["Name"] == name) & (pb["Surname"] == surname)]
    except:
        print("***Error***")
        return
    if result is None or result.empty:
        print("~~~~~~~~ Phonebook doesn't contain the record with these parameters ~~~~~~~~")
        return
    return result
