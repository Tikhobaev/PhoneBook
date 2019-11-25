from Add.add import correct_name_surname,correct_date, correct_telephone
import re
import datetime


def search_record(pb, mode=0):
    print("********* Enter the fields by which the record will be searched *********")
    command = 0
    fields = ["Name", "Surname", "Date", "Phone number"]
    result = pb
    while command != 5:
        print("\nSearch by:")
        print("\t1. Name")
        print("\t2. Surname")
        print("\t3. Date of birth in format 'DD.MM' ")
        print("\t4. Telephone")
        print("\t5. Stop")
        try:
            command = int(input())
        except:
            print("Incorrect input")
            command = 0
            continue
        if command < 1 or command > 5:
            print("Incorrect input")
            continue
        if command == 5:
            break
        print("Enter field ", fields[command-1])
        field = input()
        if command == 4:  # cast to int the telephone number
            try:
                field = int(field)
            except:
                print("Incorrect telephone number")
                return
        field = correct_field(field, command)
        if field == ":":  # indicates a mistake
            return
        try:
            if command == 3:
                result = pb[pb[fields[command - 1]].str.startswith(field)]
            else:
                result = pb[pb[fields[command-1]] == field]
        except:
            print("***Error***")
        if result is None or result.empty:
            print("Phonebook doesn't contain the record with these parameters")
            break
        print(result)
        if mode == 1:
            return result
    return result


def correct_field(field, command):
    if command == 1 or command == 2:
        field = correct_name_surname(field)
        if len(field) == 0:
            print(r"~~~~~~~~ Incorrect name\surname ~~~~~~~~")
            return ":"
    elif command == 3:
        field = re.match(r'^\d{2}[-.]\d{2}', field)
        if field:
            field = re.sub('-', r'\.', field.group(0))
            __field = field + ".2020"
            try:
                datetime.datetime.strptime(__field, '%d.%m.%Y')
            except ValueError:
                field = '-'  # means that date is incorrect
                print(r"~~~~~~~~ Incorrect data ~~~~~~~~")
                return ":"
    elif command == 4:
        field = correct_telephone(str(field))
        if len(field) == 0:
            print(r"~~~~~~~~ Incorrect number ~~~~~~~~")
            return ":"
    return field
