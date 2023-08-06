import sys
import re


def add_phonebook_entry(phonebook):
    contact_name = str(input("Please enter your phonebook name:"))
    if contact_name == '' or contact_name == ' ':
        sys.exit("Name cannot be empty")
    phone_number = int(input("Please enter your phonebook number:"))
    if phone_number is None or is_valid(str(phone_number)) is False:
        sys.exit("Number cannot be empty or invalid")
    phonebook[contact_name] = phone_number
    print("Added phonebook entry", phonebook)
    return phonebook


def remove_phonebook_entry(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print("Removed phonebook entry", phonebook)
    else:
        print("Name not found")
    return phonebook


def search_phonebook_entry(phonebook, name):
    search_queries_dict = {}
    for i in phonebook.keys():
        if name in i:
            search_queries_dict[i] = phonebook[i]
    if len(search_queries_dict) == 0:
        print("Name not found")
    else:
        print(search_queries_dict)
    return search_queries_dict


def is_valid(mobile_number):
    pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return pattern.match(mobile_number)


def display_menu():
    entry = int(input("What do you want to do? \n 1.Add a new entry \n 2.Remove an entry \n 3.Search an entry"))
    return entry


print("Welcome to Phonebook")
phonebook = {}
choice = 1
while choice is not None and choice in range(1, 4):
    choice = display_menu()
    if choice == 1:
        phonebook = add_phonebook_entry(phonebook)
    elif choice == 2:
        name = input("Please enter name to be deleted:")
        phonebook = remove_phonebook_entry(phonebook, name)
    elif choice == 3:
        name = input("Please enter name to be searched:")
        search_phonebook_entry(phonebook, name)
