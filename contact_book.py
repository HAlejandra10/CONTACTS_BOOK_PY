#Step1: Adding The Menu(options):

contacts = []

#This is the menu for the Store or Contact Book app. Here you will select the action she/he wants to perform
def display_menu():
    print("Contact Book Menu")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Display all contacts")
    print("6. Exit")
    
#Step2: Adding New Contact:

def add_contact():
    name = input("Enter the contact´s name: ")
    email = input("Enter the contact´s email: ")
    phone = input("Enter the contact´s phone number: ")
    # creamos un diccionario usando la información de arriba
    contact = {"Name": name, "Email": email, "Phone": phone}
    contacts.append(contact)
    print("Contact added successfully!")