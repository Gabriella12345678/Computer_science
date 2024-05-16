#1st National Bank of Browntown Online Banking Application


class Customer():
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)

    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount):
    #Add the ability to deposit
        pass

    #Add the ability to check balance

print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()
name = input("Let's Get Started! What is your name: ")
customer = Customer(name)
while True:
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance")
    choice = input("->")

    #Withdraw
    if choice == "1":
        print("How much are you withdrawing")
        amount = float(input("->"))
        customer.withdraw(amount)
        print("You have withdrawn ", amount)
        print("This is how much money you have left in you back account")
        print(customer.balance)
    #Add the ability to deposit

    #Deposit
    if choice == "2":
        pass 
    #Print how much they are depositing
        print("How much are you depositing? ")
        amount = float(input("->"))
        customer.deposit(amount)
        #Print how much money has been diposited to their account
        print("This much money has been diposited to your account ", amount)
        
    #Add the ability to check balance
    #Check Balance
    if choice == "3":
    #Print their balalnce
        print("Your balance is ",customer.balance)
    
