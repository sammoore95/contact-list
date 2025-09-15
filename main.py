import json
import phonenumbers
from validate_email_address import validate_email
from tabulate import tabulate


def get_phone_num():
    """Helper function to get user phone number, validate it, and return in a US phone number format"""
    while True:
        phone_num = input("Enter Phone (e.g., +1 650-253-0000 or 6502530000): ")

        # check if phone number passes validation
        try:
            parsed = phonenumbers.parse(phone_num, "US")  # default region
            if phonenumbers.is_valid_number(parsed):
                return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            else:
                print("❌ Invalid phone number. Please try again.")
        except phonenumbers.NumberParseException:
            print("❌ Could not parse number. Please enter a valid phone number.")
            

def get_email():
    """Helper function to get the user email, validate it, and return the email"""
    while True:
        email = input("Enter email: ")

        # check if email passes validation
        if validate_email(email) == True:
            return email
        else:
            print("Please enter a valid email ")


def get_int(promt):
    """Helper function to get valid integer input from user"""
    while True:
        try:
            num_of_items = int(input(promt))
            if num_of_items > 0:
                break
            else:
                print("Please enter a valid integer greater than 0")
        except ValueError:
            print("Please enter a valid integer")
    return(num_of_items)


def create_contact():
    """
    Get user input for a new contact. 
    Validates users information using helper functions. 
    Writes validated inputs as a JSON string to contacts.json
    """
    num_of_items = get_int("How many contacts would you like to add?")

    # Adds n number of contacts to the contact list
    for i in range(num_of_items):
        print("Creating new contact:")
        name = input("Enter Name: ")
        phone = get_phone_num() # validated helper
        email = get_email()     # validated helper
        notes = input("Enter notes: ")

        # store contact info as a dictionary
        contact = {"Name":name, "Phone":phone, "Email":email, "Notes":notes}

        # Try to load existing contacts (or create empty list if file is missing/invalid)
        try:
            with open("contacts.json", "r") as f:
                contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            contacts = []

        # Append new contact to the list
        contacts.append(contact)

        # Write the updated list back to the file
        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=4)


def show_contact_list():
    """Loads contacts from JSON file, sorts them alphabetically by the name, then prints the contacts in a table"""
    with open("contacts.json", "r") as f:
        contact_list = json.load(f)
        sorted_contact_list = sorted(contact_list, key=lambda x: x["Name"].lower())     # sorts the list of dicts by the Name key
        contact_table = tabulate(sorted_contact_list, headers="keys", tablefmt="fancy-grid")
        print(contact_table)


def search_contact_list():
    while True:
        print("""What key would you like to search the contact list by?
            1. Name
            2. Phone
            3. Email""")
        
        user_choice = get_int("Please enter selection (int) ")
        
        if user_choice <= 3:
            break
        else:
            print("Please choose a valid number")
    
    with open("contacts.json", "r") as f:
        contact_list = json.load(f) 

    # searches for matching Name values
    if user_choice == 1:
        while True:
            name_search = input("What name would you like to search for? ")
            
            # List of potential matches
            matches = []

            # searches the contact list for any Name matches, if they match, append to matches
            for i in contact_list:
                if i["Name"] == name_search:
                    matches.append(i)

            if matches:             # returns True if Matches list is not empty, else returns False
                sorted_matches = sorted(matches, keys=lambda x: x["Name"])              # sorts matches by Name
                print(tabulate(sorted_matches, headers="keys", tablefmt="fancy-grid"))  # prints table of sorted matches
                break   # breaks the While loop when matches is true (is not empty list)
            else:
                print("That name is not in the list, please enter a valid name")

    # Searches for matching Phone values
    if user_choice == 2:
        while True:
            phone_search = get_phone_num()

            # list of potential matches
            matches = []

            # Seaches the contact list for any Phone matches, if they match, append to matches
            for i in contact_list:
                if i["Phone"] == phone_search:
                    matches.append(i)

            if matches: # returns True if matches list is not empty, else returns False
                sorted_matches = sorted(matches, key=lambda x: x["Name"])               # sorts matches by Name
                print(tabulate(sorted_matches, headers="keys", tablefmt="fancy-grid"))  # prints table of sorted matches
                break
            else:
                print("That number is not in the contact list, please enter a valid phone number")

    # Seaches for matching Email values
    if user_choice == 3:
        while True:
            email_search = get_email()

            # list of potential matches
            matches = []

            # seaches contact list for any email matches, if they match, append to matches
            for i in contact_list:
                if i["Email"] == email_search:
                    matches.append(i)

            if matches: # returns True if matches list is not empty, else returns False and asks for valid input
                sorted_matches = sorted(matches, key=lambda x: x["Name"])               # sorts matches by Name
                print(tabulate(sorted_matches, headers="keys", tablefmt="fancy-grid"))  # prints table of sorted matches
                break
            else:
                print("That email is not in the contact list, please enter a valid email")
    

def update_contact():
    while True:
        contact_choice = input("What contact would you like to update? ")

        with open("contacts.json", "r") as f:
            contact_list = json.load(f)
        
        # list of potential matches
        matches = []

        for i in contact_list:  # searches the contact list for any Name value matches, if they match, append to matches
            if i["Name"] == contact_choice:
                matches.append(i)

        if matches:     # returns True, if Matches list is not empty, else return false and ask for new valid input
            break
        else:
            print("That name is not in the conact list, please select a valid name ")

    

        



def show_menu():
    """Prints Menu of User Options"""
    print("""
=====================
   Contact List Menu
=====================
1. View Contact List
2. Add Contact
3. Search Contact List
4. Update Contact Info
5. Remove Contact
6. Exit
""")
    
update_contact()
    

    


    

    