def create_contact(contacts):
  contact_name = input("Enter the contact name: ")
  contact_phone = input("Enter the contact phone: ")
  contact_email = input("Enter the contact email: ")
  contact_favorite = input("Enter YES/yes or NO/no to favorite: ")

  contact = { 
    "name": contact_name,
    "phone": contact_phone,
    "email": contact_email,
    "favorite": False
  }
    
  if(contact_favorite and contact_favorite.lower() == 'yes'):
    contact["favorite"] = True
  else:
    contact["favorite"] = False

  
  contacts.append(contact)

  print(f"\nContact {contact_name} was successfully created!")
  return

def show_contacts(contacts):
  if(len(contacts) != 0):
    print("\nContact List")
    for index, contact in enumerate(contacts, start = 1):
      favorite = "★" if contact["favorite"] else " "
      name = contact["name"]
      phone = contact["phone"]
      email = contact["email"]
      print(f"{index}. [{favorite}] {name} {phone} {email}")
  else:
    print("\nContact List is empty!")

  return

def update_contacts(contacts, index):
  adjusted_index = index - 1
  
  new_contact_name = input("Enter the contact name: ")
  new_contact_phone = input("Enter the contact phone: ")
  new_contact_email = input("Enter the contact email: ")
  new_contact_favorite = input("Enter YES/yes or NO/no to favorite: ")
  
  if adjusted_index >= 0 and adjusted_index < len(contacts):
    if(new_contact_name):
      contacts[adjusted_index]["name"] = new_contact_name
    if(new_contact_phone):
      contacts[adjusted_index]["phone"] = new_contact_phone
    if(new_contact_email):
      contacts[adjusted_index]["email"] = new_contact_email
      
    if(new_contact_favorite and new_contact_favorite.lower() == 'yes'):
      contacts[adjusted_index]["favorite"] = True
    else:
      contacts[adjusted_index]["favorite"] = False
        
    print(f"\nContact {new_contact_name} sucessfully updated!")
  else:
    print(f"Contact index {index} is invalid!")

  return

def mark_unmark_favorite_contact(contacts, index):
  adjusted_index = index - 1
  
  name = contacts[adjusted_index]["name"]
  contact_favorite = input("Enter YES/yes or NO/no to favorite: ")
  
  if adjusted_index >= 0 and adjusted_index < len(contacts):      
    if(contact_favorite and contact_favorite.lower() == 'yes'):
      contacts[adjusted_index]["favorite"] = True
    else:
      contacts[adjusted_index]["favorite"] = False
        
    print(f"\nContact {name} favorite sucessfully updated!")
  else:
    print(f"Contact index {index} is invalid!")

  return

def show_favorite_contacts(contacts):
  favorite_contacts = []

  if(len(contacts) != 0):
    print("\nFavorites Contacts List")
    for contact in contacts:
      if(contact["favorite"]):
        favorite_contacts.append(contact);

    for index, favorite_contact in enumerate(favorite_contacts, start=1):
      if(favorite_contact["favorite"]):
        favorite = "★" if favorite_contact["favorite"] else " "
        name = favorite_contact["name"]
        print(f"{index}. [{favorite}] {name}") 
  else:
     print(f"\nNo Contacts found. Please, type 1 to create new Contact!")

  return

def delete_contact(contacts, index):
  adjusted_index = index - 1

  if adjusted_index >= 0 and adjusted_index < len(contacts):
    contacts.remove(contacts[adjusted_index])
    print("\nContact sucessfully deleted!")
 
  return

contacts = [];
while True:
  print("\nMenu Contact Agenda")
  print("  1. Create Contact")
  print("  2. Show Contacts")
  print("  3. Update Contact")
  print("  4. Mark/Unmark Contact as Favorite")
  print("  5. Show Favorites Contacts")
  print("  6. Delete Contact")
  print("  7. Quit")

  choose = input("\nChoose an option: ")

  if choose == "1":
    create_contact(contacts)
    show_contacts(contacts)
  elif choose == "2":
    show_contacts(contacts)
  elif choose == "3":
    index = int(input("Enter the Contact number to update: "))
    update_contacts(contacts, index)
    show_contacts(contacts)
  elif choose == "4":
    index = int(input("Enter the Contact number: "))
    mark_unmark_favorite_contact(contacts, index)
    show_contacts(contacts)
  elif choose == "5":
    show_favorite_contacts(contacts)
  elif choose == "6":
    index = int(input("Enter the Contact number to delete: "))
    delete_contact(contacts, index)
    show_contacts(contacts)
  elif choose == "7":
    break

print("Application finalized.")