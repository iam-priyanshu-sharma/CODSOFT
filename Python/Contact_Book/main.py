from art import logo


class Contact:
    """Class to store Contacts"""
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address


class ContactBook:
    """Class for all menu's functions performed in Contact Book Project"""
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact.name}: {contact.phone_number}: {contact.email}: {contact.address}")

    def search_contact(self, query):
        matching_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                matching_contacts.append(contact)
        return matching_contacts

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            return True
        return False

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            return True
        return False


def main():
    contact_book = ContactBook()
    print(logo)
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            print("\nList of Contacts:")
            contact_book.display_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            matching_contacts = contact_book.search_contact(query)
            if matching_contacts:
                print("\nMatching Contacts:")
                for contact in matching_contacts:
                    print(f"{contact.name}: {contact.phone_number}: {contact.email}: {contact.address}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(input("Enter the index of the contact to update: ")) - 1
            if contact_book.update_contact(index, Contact(
                    input("Enter new name: "),
                    input("Enter new phone number: "),
                    input("Enter new email: "),
                    input("Enter new address: ")
            )):
                print("Contact updated successfully!")
            else:
                print("Invalid index. Contact not updated.")

        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if contact_book.delete_contact(index):
                print("Contact deleted successfully!")
            else:
                print("Invalid index. Contact not deleted.")

        elif choice == "6":
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
