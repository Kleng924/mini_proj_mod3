# Introduction:
# Welcome to the Contact Management System project! In this project, you will apply your Python programming 
# skills to create a functional command-line-based application that simplifies the management of your contacts. 
# The Contact Management System will empower you to add, edit, delete, and search for contacts with ease, 
# all while reinforcing your understanding of Python dictionaries, file handling, user interaction, and error handling.

# Project Requirements
# Your task is to develop a Contact Management System with the following features:

# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:

# Welcome to the Contact Management System! 
# Menu:
# 1. Add a new contact
# 2. Edit an existing contact
# 3. Delete a contact
# 4. Search for a contact
# 5. Display all contacts
# 6. Export contacts to a text file
# 7. Import contacts from a text file *BONUS*
# 8. Quit

# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).

# Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact with all relevant details.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact by searching for their unique identifier.
# Searching for a contact by their unique identifier and displaying their details.
# Displaying a list of all contacts with their unique identifiers.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system. * BONUS

# User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

# Error Handling:
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise 
# during execution.

import re

contacts = {}

def display_menu():
    print("Welcome to the Contact Management System!")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (optional): ")
    
    if phone in contacts:
        print("A contact with this phone number already exists.")
        return
    
    contacts[phone] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print("Contact added successfully!")

def edit_contact():
    phone = input("Enter the phone number of the contact to edit: ")
    if phone not in contacts:
        print("Contact not found.")
        return
    
    name = input("Enter new name: ")
    email = input("Enter new email address: ")
    additional_info = input("Enter new additional information (optional): ")
    
    contacts[phone] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Additional Info": additional_info
    }
    print("Contact updated successfully!")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact():
    phone = input("Enter the phone number of the contact to search for: ")
    if phone in contacts:
        print(f"Name: {contacts[phone]['Name']}")
        print(f"Phone: {contacts[phone]['Phone']}")
        print(f"Email: {contacts[phone]['Email']}")
        print(f"Additional Info: {contacts[phone]['Additional Info']}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if not contacts:
        print("No contacts found.")
    for phone, details in contacts.items():
        print(f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}, Additional Info: 
              {details['Additional Info']}")

def export_contacts():
    with open("contacts.txt", "w") as file:
        for phone, details in contacts.items():
            file.write(f"{phone},{details['Name']},{details['Email']},{details['Additional Info']}\n")
    print("Contacts exported successfully!")

def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                phone, name, email, additional_info = line.strip().split(',')
                contacts[phone] = {
                    "Name": name,
                    "Phone": phone,
                    "Email": email,
                    "Additional Info": additional_info
                }
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("File not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()



# GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Create a clean and interactive README.md file in your GitHub repository.
# Include clear instructions on how to run the application and explanations of its features.
# Provide examples and screenshots, if possible, to enhance user understanding.
# Include a link to your GitHub repository in your project documentation.

