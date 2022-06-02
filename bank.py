# Add these methods to class Account - deposit, withdraw. 
# Create two instances of account and verify they work as expected.

class Bank:
    Bank_name = "Cooperative"
    def __init__(self,balance,deposit,withdraw,account_number,name):
        self.balance = balance+deposit - withdraw
        self.deposit = deposit
        self.withdraw = withdraw
        self.account_number = account_number
        self.name = name



    def bank(self):
        return f"Hello {self.name} your account number is {self.account_number} you deposited {self.deposit} and withdrawn {self.withdraw} and your balance is {self.balance}"
            
