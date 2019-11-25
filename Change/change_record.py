from Search.search_record import search_record
from Add.add import correct_name_surname
from Add.add import correct_date
from Add.add import correct_telephone


def change_record(pb):
    copy_pb = pb
    print("   *********** You are going to change a record *************")
    print("********* Firstly, it is necessary to find the record *********\n")
    result = search_record(pb, 1)
    if result is None:
        return copy_pb
    if result.empty:
        return copy_pb
    print("********* Enter id of the record you are going to change *********")
    try:
        record_id = int(input())
    except:
        print("Error: Incorrect id")
        return copy_pb
    try:
        pb.iloc[record_id]
    except:
        print("Error: Incorrect id")
        return copy_pb
    print("What do you want to change?")
    print("\t1. Name")
    print("\t2. Surname")
    print("\t3. Date of birth")
    print("\t4. Telephone")
    print("\t5. All record")
    print("\t6. Exit")
    try:
        command = int(input())
    except:
        print("Error: Incorrect command")
        return copy_pb
    if command < 1 or command > 6:
        print("Error: Incorrect command")
        return copy_pb
    if command == 6:
        return copy_pb
    if command == 1:
        change_name(pb, record_id, "Name")
    elif command == 2:
        change_name(pb, record_id, "Surname")
    elif command == 3:
        change_data(pb, record_id)
    elif command == 4:
        change_tel(pb, record_id)
    else:
        change_all_record(pb, record_id)
    pb.to_csv("pb.csv")
    return pb


def change_name(pb, record_id, field):
    print("Enter new ", field)
    new_value = input()
    new_value = correct_name_surname(new_value)
    if len(new_value) == 0:
        print("Error: incorrect value of field")
        return
    pb.at[record_id, field] = new_value
    return


def change_data(pb, record_id):
    print("Enter new date of birth")
    new_value = input()
    new_value = correct_date(new_value)
    if new_value == '-':
        print("Error: incorrect value of field")
        return
    pb.at[record_id, "Date"] = new_value


def change_tel(pb, record_id):
    print("Enter new phone number")
    new_value = input()
    new_value = correct_telephone(new_value)
    if len(new_value) == 0:
        print("Error: incorrect value of field")
        return
    pb.at[record_id, "Phone number"] = new_value


def change_all_record(pb, record_id):
    change_name(pb, record_id, "Name")
    change_name(pb, record_id, "Surname")
    change_data(pb, record_id)
    change_tel(pb, record_id)
