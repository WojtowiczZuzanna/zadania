from contacts import Contact
from contacts import Contact_List

contacts_list = Contact_List()

contacts_list.add_new_contact(Contact("John Brown", "brown@onet.pl", 555234000))
contacts_list.display_list()

print("\n")

contacts_list.add_new_contact(Contact("Anna May", "am@o2.pl", 232000199))
contacts_list.add_new_contact(Contact("George Small", "smallg@google.pl", 222999100))
contacts_list.add_new_contact(Contact("Paola Big", "bigpaola@poczta.pl", 100200300))
contacts_list.display_list()
