import pickle
import os

Password_manager = "password_history.dat"

def load_history():
  
  if os.path.exists(Password_manager):
    try:
      with open(Password_manager, "rb") as f:
        return pickle.load(f)
    except EOFError:
      return []
  return []

def save_history(passwords):
  
  with open(Password_manager, "wb") as f:
    pickle.dump(passwords, f)

def add_account():
  
  passwords = load_history()
  
  website = input("Enter the website: ")
  username = input("Enter the your username: ")
  password = input("Enter your password: ")
  print()
  
  passwords.append({
    'Website': website,
    'Username': username,
    'Password': password
  })
  
  save_history(passwords)
  print(f"Account is created for website -> {website}")

def view_accounts():
  
  passwords = load_history()
  
  if not passwords:
    print("No Account Found.")
    return
  
  print("----------Account List----------")
  for password in passwords:
    print(f"Found -> Website: {password['Website']}, Username: {password['Username']}, Password: {password['Password']}")
  print("--------------------------------")

def search_website():
  
  passwords = load_history()
  
  website = input("Enter the Website: ")
  for password in passwords:
    if password['Website'] == website:
      print(f"Found -> Website: {password['Website']}, Username: {password['Username']}, Password: {password['Password']}")
      return
  
  print("No Account Found.")

def update_info():
  
  passwords = load_history()
  
  website = input("Enter the Website: ")
  for password in passwords:
    
    if password['Website'] == website:
      username = input("Enter the username: ")
      print()
      
      if password['Username'] == username:
        
        print("Choice the option you want to edit: ")
        print("1. Website \n2. Username \n3. Password \n")
        
        choice = int(input("Choice between (1-3): "))
        
        if choice == 1:
          password["Website"] = input("Enter the New Website: ")
        
        elif choice == 2:
          password["Username"] = input("Enter the New Username: ")
        
        elif choice == 3:
          password["Password"] = input("Enter the New Password: ")
        
        else:
          print("Invalid input !! Enter the correct input between (1-3).")
          return
        
        save_history(passwords)
        print("Record Updated Successfully.")
        return
    
  print("No Account Found with the given username.")

def remove_account():
  
  passwords = load_history()
  
  website = input("Enter the Website: ")
  for password in passwords:
    
    if password['Website'] == website:
      username = input("Enter the username: ")
      print()
      
      if password['Username'] == username:
        passwords.remove(password)
        save_history(passwords)
        print(f"Found -> Website: {password['Website']}, Username: {password['Username']}, Password: {password['Password']}")
        return

      print("No Account Found with the given username")

def main():
  while True:
    
    print("\n======Password Manager======\n")
    print("1. Add Account.")
    print("2. View All Account.")
    print("3. Search Website.")
    print("4. Update Info.")
    print("5. Delete Account.")
    print("6. Exit.\n")
    
    choice = int(input("Choice Between (1-6): "))
    print()
    
    if choice == 1:
      add_account()
    
    elif choice == 2:
      view_accounts()
    
    elif choice == 3:
      search_website()
    
    elif choice == 4:
      update_info()
    
    elif choice == 5:
      remove_account()
    
    elif choice == 6:
      print("----------GoodBye----------\n")
      break
    
    else:
      print("Invalid input. Enter the correct input between (1-6).")

if __name__ == "__main__":
  main()