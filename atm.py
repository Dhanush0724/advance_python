class Bank:
    
    def __init__(self,accno):
        self.accno = accno
        self.balance = 0

    def check_balance(self):
        print("The balance is :",self.balance)

    def deposit(self,money):
        self.balance+=money
        print("Deposit successful in account!!")
    
    def withdraw(self,money):
        if money <= self.balance:
            print("withdraw success")
            self.balance-=money
        else :
            print("Insufficent funds")
    
b1 = Bank(102)
b1.deposit(100)



def user():
    while True:
        print("MENU")
        print("1.deposit\n2.withdraw\n3.balance")
        choice = int(input())
        if choice == 1:
            print("enter the amount to deposit")
            dep = int(input())
            b1.deposit(dep)
        elif choice == 2:
            print("enter the amount to withdraw")
            wit = int(input())
            b1.withdraw(wit)
        elif choice == 3:
            b1.check_balance()
        else :
            print("wrong input")
user()



