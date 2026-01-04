class bankAccount:
    def __init__(self,account_number,account_name,balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    def display_balance(self):
        print(f"Account Balance: {self.balance}")   
account_number=int(input("Enter your account number: "))
account_name=input("Enter your name: ")


u1=bankAccount(account_number,account_name,5000)
a=input(f"Hello {account_name}, enter D for deposit and W for withdraw and E for exit: ")
while a!="E":
   if a.upper()=="D":
      amt=int(input("Enter amount to deposit: "))
      u1.deposit(amt)
      a=input(f"Hello {account_name}, enter D for deposit and W for withdraw and E for exit: ")
   elif a.upper()=="W":
        
      amt=int(input("Enter amount to withdraw: "))
      u1.withdraw(amt)
      a=input(f"Hello {account_name}, enter D for deposit and W for withdraw and E for exit: ")
   elif a.upper()=="E":
       break
   else:
    print("enter valid keyword")
    a=input(f"Hello {account_name}, enter D for deposit and W for withdraw and E for exit: ")

print ("exited sucessfully")
