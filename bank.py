# Add these methods to class Account - deposit, withdraw. 
# # Create two instances of account and verify they work as expected.
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance

from datetime import datetime
          
class Account:
    def __init__(self,name,acc_number):
        self.balance = 0
        self.name = name
        self.acc_number = acc_number
        self.deposits = []
        self.withdrawals = []
        self.transction = []
        self.time = datetime.now().strftime('%x')
        self.full_statements = []
        self.dep_depo ={} 
        self.with_withdraw =  {}
        self.total_bal=[]
        self.loan_balance = 0
        self.loan_repayment = 0
        # self.amount = 0
    def deposit (self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance+=amount
            self.deposits.append(amount)
            self.dep_depo = {}
            self.dep_depo.update({"date":self.time})
            self.dep_depo.update({"amount":amount})
            self.dep_depo.update({"narration":"Deposits"})
            print(self.dep_depo)
            self.total_bal.append(self.dep_depo)
            print(self.total_bal)
         
            return f"You've deposited {amount}.Your new balance is {self.balance}" 
  

    def withdraw (self,amount):
        count = 0
        if amount > self.balance:
           return  f"Your balance is {self.balance}, you cannot withdraw the {amount}"
        elif amount <= 0:
            return f"Amount must be greater than zero"
        else:
            self.balance -=amount
            new_balance = self.balance-100
            self.withdrawals.append(amount)
            
            self.with_withdraw = {}
            self.with_withdraw.update({"date":self.time})
            self.with_withdraw.update({"amount":amount})
            self.with_withdraw.update({"narration":"withdrawals"})
            print(self.with_withdraw) 

            self.total_bal.append(self.with_withdraw)
            print(self.total_bal)

            return f"You have withdrawn {amount} your balance is {new_balance}"
   
    def deposits_statement(self):
        for x in self.deposits:
         print(f"You've deposited {x}")
         

    def withdrawals_statement(self):
        for i in self.withdrawals:
           print(f"You've withdrawn {i}")

    def current_balance(self):
        balance = self.balance
        return f"Your current balance is {balance}"

    def all_statements(self):
        for a in self.total_bal:
            date = a["date"]
            narration = a["narration"]
            amount = a["amount"]
            return f"{date}-----{narration}------{amount}"

    def loan(self, amount):
        sum=0
        for a in self.total_bal:
            sum+=a["amount"]
       
        if len(self.deposits)<10:
            print("Loan requested must be greater than 0")
        elif amount<100:
            print("Loan amount requested must be more than 100")
        elif amount <= (sum//3):
            print(f"You are legible for the loan and your balance is {amount}")
        elif self.balance== 0:
            print(f"You need to clear the outstanding loan of {amount}")
        elif self.loan_balance>0:
            return f"You cannot borrow {amount} you need to clear your loan first"     
        else:
            self.loan_balance+= (0.03*amount)+amount
            return f"You have borrowed{amount} with an interest of {0.03*amount} and your balance is {self.loan_balance}"    
    
    
    def repay_loan(self,amount):
        loan_repay = amount - self.loan_balance
        if amount<self.loan_balance:
            return f"You have paid {amount} and your loan balance is {self.loan_balance}"
        elif amount == self.loan_balance:
            return "Congratulations you have cleared you loan"
        else:
            return f"Congratulations you have cleared your loan and your new balance is {self.loan_balance}"        

    def transfer(self,amount,new_account):
        self.new_account=new_account
        self.amount=amount
        current_balance=self.balance-amount
        if amount<=0:
            print(f" Hello {self.account_name } You cannot transfer a non-existant amount")
        elif amount>self.balance:
            print(f"Hello {self.account_name} Your cannot transfer {amount}.Your current balance is {self.balance}")
        elif amount<self.balance:
             print(f"Hello {self.account_name} You have transferred {amount} to {self.new_account} your balance is {current_balance}")     

    
            
