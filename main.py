from Add.add import add_record
from Delete.delete_record import delete_record
from Search.search_record import search_record
from Change.change_record import change_record
from Age.show_age import show_age
import pandas as pd


def main():
    user_input = 0
    phoneBook = pd.read_csv("pb.csv", index_col="Id", parse_dates=True)
    while user_input != 7:
        print("\n********* Choose the number of the desired operations *********")
        print("\t1. Add new record to the phonebook")
        print("\t2. Introduce some change to the records")
        print("\t3. Delete a record")
        print("\t4. Show the age of a person")
        print("\t5. Print all records")
        print("\t6. Search record")
        print("\t7. Exit")
        print("\tEnter the number: ")
        try:
            user_input = int(input())
        except Exception:
            print("~~~~~~~~ Incorrect input: please enter a number ~~~~~~~~\n")
            continue
        if user_input == 1:
            add_record(phoneBook)
            continue
        if user_input == 2:
            phoneBook = change_record(phoneBook)
            continue
        if user_input == 3:
            phoneBook = delete_record(phoneBook)
            continue
        if user_input == 4:
            show_age(phoneBook)
            continue
        if user_input == 5:
            if phoneBook.empty:
                print("********************* Phonebook is empty **********************")
                continue
            print("\n**********************   Phonebook:   *************************")
            print(phoneBook)
            print("***************************************************************\n")
            continue
        if user_input == 6:
            search_record(phoneBook)
            continue
        if user_input == 7:
            break


main()