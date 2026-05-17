import json
import os

FILE_NAME = "contacts.json"


# Load contacts from file

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save contacts to file

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!\n")


# View all contacts

def view_contacts(contacts):
    print("\n--- Contact List ---")

    if not contacts:
        print("No contacts found.\n")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")

    print()


# Search contact by name or phone number

def search_contact(contacts):
    print("\n--- Search Contact ---")
    keyword = input("Enter Name or Phone Number: ").lower()

    found = False

    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\nContact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")

    print()


# Update contact details

def update_contact(contacts):
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave field empty to keep old value.\n")

            new_name = input(f"New Name ({contact['name']}): ")
            new_phone = input(f"New Phone ({contact['phone']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            save_contacts(contacts)
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


# Delete contact

def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


# Main menu

def main():
    contacts = load_contacts()

    while True:
        print("========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run the program

if __name__ == "__main__":
    main()
