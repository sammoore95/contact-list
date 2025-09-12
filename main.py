import json
import phonenumbers
from validate_email_address import validate_email

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

    for i in range(num_of_items):
        print("Creating new contact:")
        name = input("Enter Name: ")
        phone = get_phone_num() # validated helper
        email = get_email()     # validated helper
        notes = input("Enter notes: ")

        # store contact info as a dictionary
        contact = {"Name":name, "Phone":phone, "email":email, "notes":notes}

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

def show_menu():
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
    
create_contact()

    

    