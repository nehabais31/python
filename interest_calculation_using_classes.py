"""
program that creates an Account object with an account id of 1122, a
balance of $20,000, and an annual interest rate of 4.5%. 
Use the withdraw method to withdraw $2,500, 
use the deposit method to deposit $3,000, 
and print the id, balance, monthly interest rate, and monthly interest

@author: Neha Bais
MET CS-521 A3
"""

class Account:
    # constructor with default values
    def __init__(self, id = 0, balance = 100.00, annual_int_rate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annual_int_rate = annual_int_rate
     
    # get account_id    
    def get_id(self):
        return self.__id
    
    # get account balance    
    def get_balance(self):
        return self.__balance
     
    # get annual interest rate    
    def get_annual_int_rate(self):
        return self.__annual_int_rate

    #st id to the value passsed from user
    def set_id(self, id):
        self.__id = id
    
    # set balance to value passed from user
    def set_balance(self, balance):
        self.__balance = balance
     
    # set annual int rate to value passed from user    
    def set_annual_int_rate(self, annual_int_rate):
        self.__annual_int_rate = annual_int_rate
     
    # Calculate the monthly interest rate    
    def get_monthly_int_rate(self):
        return (self.__annual_int_rate/100) / 12
    
    # calculate monthly interest
    def get_monthly_interest(self):
        return self.__balance * self.get_monthly_int_rate()
    
    # update balance when some amount is withdrawn
    def withdraw(self, withdrawal_amnt):
        self.__balance = self.__balance - withdrawal_amnt
        return self.__balance
    
    # update balance when some amount is deposited
    def deposit(self, deposit_amnt):
        self.__balance = self.__balance + deposit_amnt
        return self.__balance 
        
def main():
   
    # values to create an account object
    account_id = 1122
    account_balance = 20000.00
    annual_int_rate = 4.5
    
    withdrawal_amnt = 2500.00
    deposit_amnt = 3000.00
    
    # Create an account object
    account = Account(account_id, account_balance, annual_int_rate)
    
    #calling the withdraw method
    account.withdraw(withdrawal_amnt)
    
    # calling the deposit method of account class
    account.deposit(deposit_amnt)
        
    print('Account Id is: ', account.get_id())
    print('Acount Balance: ', account.get_balance())
    
    print('Monthly Interest Rate: ', (account.get_monthly_int_rate())*100 , '%')
    print('Monthly Interest: ', account.get_monthly_interest())
    
main()    
    
    
    
     
        
    