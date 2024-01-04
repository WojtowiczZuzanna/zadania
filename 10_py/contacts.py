class Contact():
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone


class Contact_List():
    def __init__(self):
        self.contacts = []

    def add_new_contact(self, contact):
        self.contacts.append(contact)

    def display_list(self):
        print("Contacts list: ")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Email: {contact.email}, Telephone: {contact.telephone}")

