import random
class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.transactions=[]
    
    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f"Deposit = +{amount}")
        print(f"Rs {amount} deposit ho gay hein ! New Balance = {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficent amount ! Current balance = Rs{self.balance}")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw = -{amount}")
            print(f"Rs {amount} withdraw ho gay hein ! New Balance = Rs{self.balance}")
    
    def check_balance(self):
        print(f"Username = {self.name}")
        print(f"Account Number = {self.account_number}")
        print(f"Current Balance = {self.balance}")
     
    def mini_statement(self):
        if len(self.transactions)==0:
            print("No Transactions yet!")
        else:
            print(f" Ministatement --- {self.name}")
            print("-" * 35)
            for transactions in self.transactions:
                print(transactions)
            print("-" * 35)
            print(f"Current Balnace = {self.balance}")

class Bank:

    def __init__(self,bank_name):
        self.bank_name = bank_name
        self.accounts={}
 
 

    def create_account(self, name, balance):
        account_number = str(random.randint(10000000, 99999999))  # 8 digit random number
        self.accounts[account_number] = BankAccount(name, account_number, balance)
        print(f"✅ Account created for {name}!")
        print(f"🔢 Your Account Number: {account_number}")
        print("⚠️ Please save your account number!")

    def deposit(self,account_number,amount):
        if account_number in self.accounts :
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found!")

    def withdraw(self,account_number,amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found")
    
    def  check_balance(self,account_number):
        if account_number in self.accounts:
            self.accounts[account_number].check_balance()
        else:
            print("Account not found")
        
    def mini_statement(self,account_number):
        if account_number in self.accounts:
            self.accounts[account_number].mini_statement()
        else:
            print("Account not found")


bank = Bank("HBL Bank")

print("\n" + "=" * 40)
print("     🏦 WELCOME TO HBL BANK 🏦")
print("=" * 40)

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Mini Statement")
    print("6. Exit")
    print()
    
    choice = input("Enter Your chooice (1-6) ")

    if choice == "1":
        name= input("Enter Your Name : ")
        balance=float(input("Enter your Initial Balance : "))
        bank.create_account(name,balance)
    
    elif choice =="2":
          account_number = input("Enter your Account Number: ")
          amount = float(input("Enter your Amount to deposit : "))
          bank.deposit(account_number,amount)

    elif choice == "3":
        account_number = input("Enter your Account Number: ")
        amount = float(input("Enter your Amount to Withdraw: "))
        bank.withdraw(account_number,amount)

    elif choice == "4":
        account_number = input("Enter your Account Number: ")
        bank.check_balance(account_number)
    
    elif choice == "5":
        account_number= input("Enter Your Account Number: ")
        bank.mini_statement(account_number)

    elif choice == "6":
        print(" Thank you for using HBL Bank ! GoodBye---------")
        break
    else:
        print("Invalid Choice! Please Try Again .")
         
       