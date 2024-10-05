

class BankAccount:
    def __init__(self,account_balance) :
        self.account_balance = account_balance
        pass

    def deposit(self,amount):
        self.account_balance = self.account_balance + amount
        return self.account_balance


    def withdraw(self,amount):
        if self.account_balance - amount >= 0:
            return True
        elif self.account_balance - amount < 0:
            return False

    def display_balance(self):
        print("Current Balance: ${:.2f}".format(self.account_balance))


