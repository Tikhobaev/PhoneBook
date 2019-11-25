import re
import datetime
from numpy import NaN


def add_record(pb):
    print("*********** Please enter new record in format 'Name;Surname;DD.MM.YYYY;XXXXXXXXXXX' ***********")
    fields = get_fields()  # obtain input and parse it into an array of fields
    correct(fields)
    if check(fields) == -1:  # if error with name/surname/tel_number occurred
        return               # or if date is incorrect then return
    if check_if_exist(pb, fields) == -1:  # if record with this name and surname is already exist an
        return                            # user don't want to change it
    pb.loc[pb.shape[0]] = [fields[0], fields[1], fields[2], fields[3]]  # recording
    pb.to_csv("pb.csv")
    print("\n~~~~~~~~ New record was added successfully ~~~~~~~~\n")


def correct(fields):
    fields[0] = correct_name_surname(fields[0])
    fields[1] = correct_name_surname(fields[1])
    fields[2] = correct_date(fields[2])
    fields[3] = correct_telephone(fields[3])


def correct_name_surname(field):
    name = re.match(r'^[\s\w]*$', field)  # only spaces and letters
    if name:
        field = name.group(0)
        field = field.capitalize()
    else:
        print("~~~~~~~~ Only letters, numbers and spaces are allowed in name/surname field ~~~~~~~~")
        field = ''
    return field


def correct_date(field):
    data = re.match(r'^\d{2}[-.]\d{2}[-.]\d{4}$', field)
    if data:
        field = re.sub('-', r'\.', data.group(0))
        try:
            datetime.datetime.strptime(field, '%d.%m.%Y')
        except ValueError:
            field = '-'  # means that date is incorrect
    else:
        field = ''
    return field


def correct_telephone(field):
    tel_number = re.search(r'^(8|\+7)[0-9]{10}$', field)
    if tel_number:
        field = re.sub(r'\+7', '8', tel_number.group(0))
    else:
        field = ''
    return field


def get_fields():
    new_record = input()
    fields = new_record.split(";")
    while len(fields) != 4:
        print("~~~~~~~~ Wrong number of fields in record, must be 4 fields\nPlease try again: ~~~~~~~~")
        new_record = input()
        fields = new_record.split(";")
    return fields


def check(fields):
    if len(fields[0]) == 0 or len(fields[1]) == 0 or len(fields[3]) == 0:
        print("*~~~~~~~~ Name, Surname and phone fields must be filled, try again: ~~~~~~~~")
        return -1

    if fields[2] == '-':
        print("*~~~~~~~~ Incorrect data, try again ~~~~~~~~")
        return -1
    elif len(fields[2]) == 0:
        fields[2] = NaN
        return 0


def check_if_exist(pb, fields):
    try:
        if not pb[(pb["Name"] == fields[0]) & (pb["Surname"] == fields[1])].empty:
            print("~~~~~~~~~~~~~~ The record with this name and surname already exist ~~~~~~~~~~~~~~~")
            print("******** Do you want to change fields name and surname in this record? (1 - yes, 2 - no) ********")
            try:
                change_input = int(input())
            except (ValueError, TypeError):
                print("~~~~~~~~~~~~~~~~~~~ Incorrect input ~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~ You will be returned to the main menu ~~~~~~~~")
                return -1
            if change_input == 1:
                return change_record(pb, fields)
            else:
                return -1
    except:
        print("*** Error ***")
        return -1


def change_record(pb, fields):
    print("*********** Enter new name: ************")
    name = input()
    print("********** Enter new surname: **********")
    surname = input()
    name = correct_name_surname(name)
    surname = correct_name_surname(surname)
    if len(name) == 0 or len(surname) == 0:
        print(r"~~~~~~~~ Name\surname field cannot be empty ~~~~~~~~")
        return -1
    index = pb[(pb["Name"] == fields[0]) & (pb["Surname"] == fields[1])].index.values
    pb.at[index[0], "Name"] = name
    pb.at[index[0], "Surname"] = surname
    pb.to_csv("pb.csv")
    print("\nRecord has been changed successfully\n")
    return -1
