 # Main program file
 
# contact_book.py

import os

CONTACTS_FILE = "contacts.txt"

def add_contact():
    """Add a new contact to the file"""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully!\n")

def view_contacts():
    """View all contacts"""
    if not os.path.exists(CONTACTS_FILE):
        print("❌ No contacts found!\n")
        return

    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()

    if not contacts:
        print("❌ Contact list is empty.\n")
        return

    print("\n📒 Contact List:")
    print("-" * 40)
    for idx, contact in enumerate(contacts, 1):
        name, phone, email = contact.strip().split(",")
        print(f"{idx}. Name: {name}, Phone: {phone}, Email: {email}")
    print("-" * 40 + "\n")

def search_contact():
    """Search contact by name"""
    if not os.path.exists(CONTACTS_FILE):
        print("❌ No contacts found!\n")
        return

    search_name = input("Enter name to search: ").strip().lower()
    found = False

    with open(CONTACTS_FILE, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if search_name in name.lower():
                print(f"🔍 Found -> Name: {name}, Phone: {phone}, Email: {email}")
                found = True

    if not found:
        print("❌ Contact not found!\n")

def main():
    """Main menu loop"""
    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.\n")

if __name__ == "__main__":
    main()
