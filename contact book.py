contacts = []

def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("Contact added successfully.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"Contact {idx}:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")

def search_contact(search_name):
    found_contacts = []
    for contact in contacts:
        if search_name.lower() in contact["name"].lower():
            found_contacts.append(contact)
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching contacts:")
        for idx, contact in enumerate(found_contacts, start=1):
            print(f"Contact {idx}:\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\n")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_name = input("Enter name to search: ")
            search_contact(search_name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
