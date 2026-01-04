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
u1=bankAccount(1,"sahan",5000)
a=input("Enter D for deposit and W for withdraw and E for exit: ")
while a!="E":
   if a=="D":
      amt=int(input("Enter amount to deposit: "))
      u1.deposit(amt)
      a=input("Enter D for deposit and W for withdraw and E for exit: ")
   elif a=="W":
        
      amt=int(input("Enter amount to withdraw: "))
      u1.withdraw(amt)
      a=input("Enter D for deposit and W for withdraw and E for exit: ")
   elif a=="E":
       break
   else:
    print("enter valid keyword")
    a=input("Enter D for deposit and W for withdraw and E for exit: ")

print ("exited sucessfully")
