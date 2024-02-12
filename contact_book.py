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
    contact = {"Name": name, "Email": email, "Phone": phone}
    contacts.append(contact)
    print("Contact added successfully!")
    
#Step3: Adding Search:

def search_contact():
    search_term = input("Enter the name  or email of the contact you want to search: ")
    found_contacts = []
    for contact in contacts: 
        if search_term.lower() in contact["Name"].lower() or search_term.lower() in contact["Email"].lower():
            found_contacts.append(contact) 
    if found_contacts:
        print("Matching contacts found: ")
        for contact in found_contacts: 
            print("Name", contact["Name"])
            print("Email", contact["Email"])
            print("Phone", contact["Phone"])
            print("-------------------------------")
    else:
        print("No matching contacts found.")
    
    
#Step4: Update function:

def update_contact():
    name= input("Enter the name of the contact to update: ")
    found_contact= None 
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            found_contact= contact 
            break 
        
    if found_contact: 
        print("Contact found. Enter new details:")
        found_contact["Name"] = input("Enter the new name:")
        found_contact["Email"] = input("Enter the new email: ")
        found_contact["Phone"] = input("Enter the new phone number: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
        
#Step5: Deleting a Contact from contacts list:

def delete_contact():
    name= input("Enter the name of the contact you want to delete")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            break
        
    else:
        print("Contact not found")

#Step6: Display all contacts:

def display_all_contacts():

    if contacts:
        print("All Contacts")
        for contact in contacts:
            
            print("Name", contact["Name"])
            print("Email", contact["Email"])
            print("Phone", contact["Phone"])
            print("========================")
    else:
        print("No contact found")
        
# Step7: The Driver Loop(Bucle del conductor):-> Main program to choice

while True:
 
    #funcion al comienzo del código
    display_menu()
    choice= input("Enter your choice(1-6)")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("Exiting the program...")
        break
        
    else:
        print("Invalid choice. Please enter a valid option (1-6).")

    