import csv
import os.path

class ContactManager:
    def __init__(self, filename):
        self.filename = filename
    def create_contact(self):
        name = input("Enter fullname: ").title()
        while True:
            try:
                number = int(input("Enter phone number: "))
                break
            except ValueError:
                print(f"Enter a valid phone number.")
                continue

        email = input("Enter email address: ").lower()

        contact = {"name": name, "number": number, "email": email}
        return contact

    def add_contact(self):
        contact_list = []
        while True:
            choice = input("Do you wana create a new contact: \"yes/no\": ").lower()
            if choice == "yes":
                new_contact = self.create_contact()
                contact_list.append(new_contact)
            else:
                break
        return contact_list

    def save_contacts_csv(self, contact_list):
        file_exists = os.path.isfile(self.filename)
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "number", "email"])

            if not file_exists:
                writer.writeheader()
            writer.writerows(contact_list)
        print(f"Contacts saved to {self.filename}")

    def read_contents_from_csv(self):
        contacts = []
        if os.path.isfile(self.filename):
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contacts.append(row)
        return contacts

    def find_contact(self, search_term):
        contacts = self.read_contents_from_csv()
        found_contacts = [
            contact for contact in contacts
            if search_term.lower() in contact["name"].lower() or
               search_term.lower() in contact["email"].lower()
            ]
        return found_contacts

    def update_contacts(self, update_item):
        contacts = self.read_contents_from_csv()
        update_item_lower = update_item.lower()
        updated = False

        for contact in contacts:
            if update_item_lower in contact["name"].lower() or \
                update_item_lower in contact["email"].lower():
                print(f"Current contact info: {contact}")
                contact["name"] = input("Enter new fullname: ").title()
                while True:
                    try:
                        contact["number"] = int(input("Enter new phone number: "))
                        break
                    except ValueError:
                        print("Enter valid phone number: ")
                        continue
                contact["email"] = input("Enter new email address: ").lower()
                updated = True

            if updated:
                with open(self.filename, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["name", "number", "email"])
                    writer.writeheader()
                    writer.writerows(contacts)
                print(f"Contact updated successfull in {self.filename}")
            else:
                print("No matching contact found.")

    def delete_contacts(self, search_item):
        contacts = self.read_contents_from_csv()
        search_item_lower = search_item.lower()
        new_contacts = [
            contact for contact in contacts
            if search_item_lower not in contact["name"].lower() and
               search_item_lower not in contact["email"].lower()
            ]

        if len(new_contacts) < len(contacts):
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fiednames=["name", "number", "email"])
                writer.writeheader()
                writer.writerows(new_contacts)
            print(f"Contact deleted successfully from {self.filename}")
        else:
            print("No matching contact found")


# contacts = add_contact()
#
# save_contacts_csv(contacts, "contacts.csv")
#
# search_term = input("Enter name or email to search: ")
# matching_contacts = find_contact("contacts.csv", search_term)
#
# if matching_contacts:
#     print("Matching contacts: ")
#     for contact in matching_contacts:
#         print(f"Name: {contact["name"]}, Phone: {contact["number"]} and E-mail: {contact["email"]}")
# else:
#     print("No matching contact: ")
#
# update_term = input("Enter name or email of contact to update: ")
# update_contacts("contacts.csv", update_term)