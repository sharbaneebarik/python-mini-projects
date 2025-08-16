contacts = []

def show_menu():
    print("\n-- Contact Master --")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
    else:
        print("\nContacts:")
        i = 1
        for contact in contacts:
            print(f"{i}. Name: {contact[0]}. Phone: {contact[1]}")
            i += 1

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts.append([name, phone])
    print("Contact added!")

def search_contact():
    name = input("Enter name to search: ").lower()
    found = False
    for contact in contacts:
        if name in contact[0].lower():
            print("Found→", "Name:", contact[0], "Phone:", contact[1])
            found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    number = input("Enter contact number to delete: ")
    if number.isdigit():
        index = int(number) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print("Deleted contact:", removed[0])
        else:
            print("Invalid number.")
    else:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose (1-5): ")
        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()