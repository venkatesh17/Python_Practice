import sys
class Customer:
    """ Customer class with bank related operations"""

    bankname = 'DURGASOFT'
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        print("After deposit the balance: ", self.balance)

    def withdraw(self, amt):
        if amt>self.balance:
            print("Insufficient Funds.. cannot perform this operation")
            sys.exit()
        self.balance = self.balance-amt
        print('After withdraw the balance: ', self.balance)

print('Welcome to ' ,Customer.bankname)
name = input('Enter Your Name: ')
c = Customer(name)
while  True:
    print('d-Deposit\nw-withdraw\ne-Exit')
    option = input("Choose Your Option: ")
    if option=='d' or option=="D":
        amt = float(input("Enter the amount to deposit: "))
        c.deposit(amt)

    elif option=='w' or option=='W':
        amt=float(input('Enter Amount to withdraw: '))
        c.withdraw(amt)

    elif option=='e' or option=='E':
        print("Thanks for Banking")
        sys.exit()

    else:
        print("Choose valid option")
