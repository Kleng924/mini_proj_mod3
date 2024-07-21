import re

# Initialize contacts dictionary
contacts = {}

# Function to display the menu
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

# Function to add a new contact
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

# Function to edit an existing contact
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

# Function to delete a contact
def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Function to search for a contact
def search_contact():
    phone = input("Enter the phone number of the contact to search for: ")
    if phone in contacts:
        print(f"Name: {contacts[phone]['Name']}")
        print(f"Phone: {contacts[phone]['Phone']}")
        print(f"Email: {contacts[phone]['Email']}")
        print(f"Additional Info: {contacts[phone]['Additional Info']}")
    else:
        print("Contact not found.")

# Function to display all contacts
def display_all_contacts():
    if not contacts:
        print("No contacts found.")
    for phone, details in contacts.items():
        print(f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}, Additional Info: {details['Additional Info']}")

# Function to export contacts to a text file
def export_contacts():
    with open("contacts.txt", "w") as file:
        for phone, details in contacts.items():
            file.write(f"{phone},{details['Name']},{details['Email']},{details['Additional Info']}\n")
    print("Contacts exported successfully!")

# Function to import contacts from a text file
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

# Main program loop
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



