class Bank():
    def __init__(self, owner,balance='$0'):
        self.owner= owner
        self.balance = balance

    def __str__(self):
        return "Welcome {}".format(self.owner)

    def deposit(self,amount):
        self.balance+=amount
        print("You deposit ${} Successfully!".format(amount))

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("You withdraw ${} Successfully!".format(amount))
        else:
            print("Sorry! Funds Unavailable!")
            
b1= Bank('Ali',200)
print(b1)
while True:
    
    choice=int(input("Enter 1 for Balance Inquiry\nEnter 2 for Withdraw amount\nEnter 3 for desposit amount\nEnter your choice: "))
    if choice==1:
        print("\nYour Current Balance is ${}".format(b1.balance))
    elif choice==2:
        amount=int(input("Enter amount: "))
        b1.withdraw(amount)
    elif choice==3:
        amount=int(input("Enter amount: "))
        b1.deposit(amount)
    else:
        break


