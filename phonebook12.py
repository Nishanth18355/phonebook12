phonebook=[]
def add_contact():
    name=input("Enter Name: ")
    number=input("Enter Phone Number: ")
    contact={"name": name, "number": number}
    phonebook.append(contact)
    print("Contact  added successfully\n")
def view_contact():
    if not phonebook:
        print("NO CONTACT\n")
        return 
    print("Contact List\n")
    for contact in phonebook:
        print(f"{contact['name']} : {contact['number']}")
        print()
def search_contact():
    name=input("Enter name to search:").strip().lower()
    for contact in phonebook:
        if contact['name'].lower()==name:
            print(f"{contact['name']} : {contact['number']}")
            return
        print("No contacts found\n")
def delete_contact():
    name=input("Enter name to delete\n:").strip().lower()
    for contact in phonebook:
        if contact['name'].lower()==name:
            phonebook.remove(contact)
            print("Contact deleted\n")
            return
        print("Contact not found\n")
    
def sort_contacts():
    n=len(phonebook)
    if n<=1:
        print("Not enough to Arrange:\n")
        return 
    for i in range(n-1):
        for j in range(n-i-1):
            if phonebook[j]["name"]>phonebook[j+1]["name"]:
                phonebook[j],phonebook[j+1]=phonebook[j+1],phonebook[j]
                return phonebook
    print("Contacts sorted: You Can View Contacts As Sorted\n")
    return phonebook
def main():
    while True:
        print("_________PHONEBOOK MENU_________\n")
        print("1: Add Contact")
        print("2: View contact")
        print("3: Search contact")
        print("4: Delete contact")
        print("5: Arrange contact")
        print("6: Exit")
        choice=input("Enter your choice:\n")
        if choice=='1':
            add_contact()
        elif choice=='2':
            view_contact()
        elif choice=='3':
            search_contact()
        elif choice=='4':
            delete_contact()
        elif choice=='5':
            sort_contacts()
        elif choice=='6':
            print("Exiting Phonebook\n")
            break
        else:
            print("Invalid choice\n")
main()
            


        
