import pickle
import os

Bank_history = "bank_history.dat"

def load_account():
  
  if os.path.exists(Bank_history):
    
    with open(Bank_history, "rb") as f:
      return pickle.load(f)
    
  return {}

def save_account(accounts):
  
  with open(Bank_history, "wb") as f:
    pickle.dump(accounts, f)


def create_account(accounts, account_number, name, balance = 0.0):
  
  if account_number in accounts:
    raise ValueError(f"The account number {account_number} already exist.")
  
  account = {"acc_no": account_number, "name": name, "balance": balance}
  print()
  accounts[account_number] = account
  save_account(accounts)
  return account

def deposit(accounts, account_number, amount):
  
  if amount <= 0:
    raise ValueError("Deposit must be in positive number.")

  account = get_account(accounts, account_number)
  account["balance"] += amount
  save_account(accounts)
  return account["balance"]

def withdraw(accounts, account_number, amount):
  
  if amount <= 0:
    raise ValueError("Withdrawal amount must be positive.")
  
  account = get_account(accounts, account_number)
  if amount > account["balance"]:
    raise ValueError("Insufficient Funds")
  
  account["balance"] -= amount
  save_account(accounts)
  return account["balance"]

def check_balance(accounts, account_number):
  
  account = get_account(accounts, account_number)
  return account["balance"]

def list_accounts(accounts):
  return list(accounts.values())

def get_account(accounts, account_number):
  if account_number not in accounts:
    raise ValueError(f"Account number {account_number} not found.")
  return accounts[account_number]

def format_account(account):
  return f"Account[{account['acc_no']}] {account['name']} - Balance: {account['balance']:.2f}"

def main():
  
  accounts = load_account()
  while True:
    
    print("\n==== Bank Account Simulator ====\n")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Lists Account")
    print("6. Exit\n")
    
    choice = int(input("Choice between (1-6): "))
    print()
    try: 
        
      if choice == 1:
        
        account_number = int(input("Enter the account number: "))
        name = input("Enter your name: ")
        balance = float(input("Enter the inital balance: "))
        
        acc = create_account(accounts, account_number, name, balance)
        print(f"Created: {format_account(acc)}")
      
      elif choice == 2:
        
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the deposit amount: "))
        new_balance = deposit(accounts, account_number, amount)
        print(f"New balance: {new_balance:.2f}")
      
      elif choice == 3:
        
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the withdraw amount: "))
        new_balance = withdraw(accounts, account_number, amount)
        print(f"New balance: {new_balance:.2f}")
      
      elif choice == 4:
        
        account_number = int(input("Enter the account number: "))
        Check_balance = check_balance(accounts, account_number)
        print(f"Balance: {Check_balance:.2f}")
      
      elif choice == 5:
        
        accts = list_accounts(accounts)
        if not accts:
          print("Account not found")
        else:
          for acc in accts:
            print(format_account(acc))
      
      elif choice == 6:
        
        print("----------GoodBye----------")
        break
      
      else: 
        print("Invalid Input. Enter the correct input between 1-6.")
        
    except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
  main()