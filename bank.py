# Add these methods to class Account - deposit, withdraw. 
# Create two instances of account and verify they work as expected.

            
class Account:
    def __init__(self,name,acc_number):
        self.balance = 0
        self.name = name
        self.acc_number = acc_number
        self.deposits = []
        self.withdrawals = []
    def deposit (self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f"You've deposited {amount}.Your new balance is {self.balance}"  

    def withdraw (self,amount):
        if amount > self.balance:
           return  f"Your balance is {self.balance}, you cannot withdraw the {amount}"
        elif amount <= 0:
            return f"Amount must be greater than zero"
        else:
            self.balance -=amount
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount} your balance is {self.balance}"

    def deposits_statement(self):

        print(*self.deposits, sep="\n")

    def withdrawals_statement(self):
        print(*self.withdrawals, sep="\n")
    
            
