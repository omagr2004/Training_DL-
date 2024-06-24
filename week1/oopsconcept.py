#OOPs Concepts in Python
#1. Class date 18.06.24
class Account:
    acn=1
    def __init__(self):
        self.acn=Account.acn
        Account.acn+=1
    balance=0
    def withdraw(self,amount):
        print("withdrawing :",amount)
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("balance=",self.balance)
        

    def deposit(self,amount):
        print("deposit :",amount)
        self.balance+=amount
        print("total balance=",self.balance)
        
e1=Account()
e1.deposit(4500)
e1.withdraw(5000)