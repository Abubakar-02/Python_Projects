import json

contacts = {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load_contacts():
    global contacts
    try:
        with open ("contacts.json", "r") as file :
            contacts = json.load(file)
    except :
        contacts ={}

def add_contact(name, phone):
    contacts[name] = phone
    save_contacts()

def view_contacts():
    if not contacts:
        print("No contact Found.")
    else:
        print("\n📒 All Contacts:")
        print("-" * 30)
        for name, phone in contacts.items():
            print(f"Name : {name}, Phone : {phone}")
        print("-" * 30)

def search_contact(name):
    for contact_name, phone in contacts.items():
        if contact_name.lower() == name.lower():
            print(f"Name: {contact_name}, Phone: {phone}")
            return
    print("Contact not found....")

    
def delete_contact(name):
    if name in contacts :
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully.")
    else:
        print("Contact not found......")



load_contacts()

print("╔══════════════════════════════════╗")
print("║      📒 CONTACT BOOK 📒          ║")
print("╚══════════════════════════════════╝")

while True:

    print("\n Choose your option : ")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input (" Enter your choice (1-5) : ")

    if choice =="1":
        name = input("Enter contact name : ")
        phone = input(" Enter contact phone number : ")
        add_contact(name,phone)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        name = input("Enter contact name to search : ")
        search_contact(name)

    elif choice =="4":
        name = input("Enter contact name to delete : ")
        delete_contact(name)

    elif choice == "5":
        print("Exiting the contact book. Goodbye! -------- ")
        break
    else:
        print("Invalid choice. Please try again.")
