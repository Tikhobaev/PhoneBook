from Search.search_record import search_record
from Age.show_age import find_name_surname

def delete_record(pb):
    copy_pb = pb
    print("*********** You are going to delete a record *************")
    print("*********** Please, select the deleting mode *************")
    print("\t1. Deletion with search by name and surname")
    print("\t2. Deletion with search by any field")
    command = input()
    if command == "1":
        pb = delete_by_name_surname(pb)
        if pb is None:
            return copy_pb
        pb.to_csv("pb.csv")
        print("****************************************")
        print("The record has been removed successfully\n")
        return pb
    elif command == "2":
        print("********* Firstly, it is necessary to find the record *********\n")
        result = search_record(pb, 1)
        if result is None:
            return copy_pb
        if result.empty:
            return copy_pb
        print("********* Enter id of the record you are going to delete *********")
        try:
            record_id = int(input())
        except:
            print("\nError: Incorrect id\n")
            return copy_pb
        pb = pb.drop(record_id, axis=0)
        pb.to_csv("pb.csv")
        print("****************************************")
        print("The record has been removed successfully\n")
        return pb
    else:
        return pb


def delete_by_name_surname(pb):
    print("******************* Please, enter the name *******************")
    name = input()
    print("******************* Please, enter the surname *******************")
    surname = input()
    result = find_name_surname(pb, name, surname)
    if result is None:
        return
    record_id = result.index.values[0]
    pb = pb.drop(record_id, axis=0)
    return pb
