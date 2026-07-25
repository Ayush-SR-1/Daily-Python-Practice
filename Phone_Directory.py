import pickle

def add():
  
    while True:
    
      name = input("Name: ")
      number = input("Number: ")
      address = input("Address: ")
    
      with open("phone_directory_file.dat", "ab") as f:
        pickle.dump({"Name": name, "Number": number, "Address": address}, f)
      print("Contact added \n")
  
      check = input("Do you want to add more contact (Y/N): ")
      print()
      if check.upper() != "Y":
        break
        


def remove():
  try:
      with open("phone_directory_file.dat", "rb") as f:
        contacts = []
        while True:
          try: 
            contacts.append(pickle.load(f))
            
          except EOFError:
            break
          
  except FileNotFoundError:
    print("Contact does not exist.\n")
    return  
  
  if not contacts:
    print("Contact does not exist.\n")
    return 
  
  search_name = input("Enter the name of the contact you want to remove: ")
  found = False
  
  for i, contact in enumerate(contacts):
    if contact["Name"].lower() == search_name.lower():
      found = True
      del contacts[i]
      break
  
  if not found:
    print("Contact not found.\n")
    return
  
  with open("phone_directory_file.dat", "wb") as f:
    for c in contacts:
      pickle.dump(c,f)
  
  print("Contact Remove Successfully.\n")

def edit():
  
  try:

    with open("phone_directory_file.dat", "rb") as f:
      contact = []
      
      while True:
        try: 
          contact.append(pickle.load(f))
        except EOFError:
          break
        
  except FileNotFoundError:
    print("No Contact found. \n")
    return
  
  if not contact:
    print("No Contact found. \n")
    return
  
  search_name = input("Enter the Name of the Contact to Edit: ")
  found = False
  
  for contact in contact:
    if contact["Name"].lower() == search_name.lower():
      found = True
      
      field_choice = int(input("Enter the Option between (1-3)"))
      print("1. Edit Your Name. \n2. Edit Your Number.\n3. Edit your Address.")
      
      if field_choice == 1:
        contact["Name"] = input("Enter New Name: ")
      elif field_choice == 2:
        contact["Number"] = input("Enter New Number: ")
      elif field_choice == 3:
        contact["Address"] = input("Enter New Address: ")
      else:
        print("Invalid Input! Enter the correct input.\n")
        return
      
      break
      
    if not found:
      print("Contact not found.")
      return
    
    with open("phone_directory_file.dat", "rb") as f:
      for c in contact:
        pickle.dump(c,f)
    print("Contact updated successfully.\n")


def showdetail():
  
  try:
    
    with open("phone_directory_file.dat", "rb") as f:
      contact = []
      
      while True:
        try:
          contact.append(pickle.load(f))
        except EOFError:
          break
        
  except FileNotFoundError:
    print("No Contact found.\n")
    return
  
  if not contact:
    print("No Contact found")
  
  for c in contact:
    print(f"Name: {c['Name']}, Number: {c['Number']} Address: {c['Address']}")
  print()

def search():
  
  try:
    
    with open("phone_directory_file.dat", "rb") as f:
      contact = []
      while True:
        try:
          contact.append(pickle.load(f))
        except EOFError:
          break
        
  except FileNotFoundError:
    print("Contact Not Found")
    return
  
  if not contact:
    print("Contact Not Found")

  search_name =input("Enter the name 0f the contact you want to search: ")
  for c in contact:
    if c["Name"].lower() == search_name.lower():
      print(f"Name: {c['Name']}, Number: {c['Number']}, Address: {c['Address']}")
      return
  
  print("Contact not found.\n")



print("\n ------------- Phone Directory ------------- \n")

answer = "Y"
while answer.upper() == "Y":
  print("Choose the option u want to continue with:\n\n1. Add Contact \n2. Remove Contact \n3. Edit Contact \n4. Show All Contact \n5. Search Contact\n6. Exit\n")

  option = int(input("Enter the option between (1-6): "))
  print()

  if option == 1:
    add()
  elif option == 2:
    remove()
  elif option == 3:
    edit()
  elif option == 4:
    showdetail()
  elif option == 5:
    search()
  elif option == 6:
    print("Thank you for viewing Phone Directory.")
  else:
    print("Invalid Input!! Please Enter the correct input.")

  answer = input("Do you want to do anything else (Y/N):")
  print()
