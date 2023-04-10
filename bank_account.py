"""
Create a bank account class that has:
    A balance intially at 0
    Interest rate in decimal format
    deposit(self,amount)
        increase the account balance by the given amount
    withdraw(self,amount)
        decrease the account balance by the given amount
    display_account_info(self)
        print to console "balance: BLAH"
    yield_interst(self)
        increases t account balnce by the current balance * the interest rate (ONLY IF BALANCE IS POSTITVE)
"""

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficent funds: Charging a 5$ fee")
            self.balance = self.balance - 5
            self.balance = self.balance - amount
        return self
    def display_account_info(self):
        return self.balance
    def yield_interest(self):
        self.int_rate = self.int_rate / 100.0
        if self.balance > 0:
            self.balance = self.balance + (self.int_rate * self.balance)
        else:
            print("Your balance is too low")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {}
    def create_account(self, account_name, int_rate,balance):
        account=BankAccount(int_rate=int_rate,balance=balance)
        self.account[account_name] = account
        print(f"You created a new account {account_name} under {self.name}")
    def make_deposit(self, account_name, amount):
        if account_name in self.account:
            account = self.account[account_name]
            account.deposit(amount)
            print(f"You deposited {amount} into {self.name} {account_name} account")
    def make_withdraw(self,account_name, amount):
        if account_name in self.account:
            account = self.account[account_name]
            account.withdraw(amount)
            print(f"You withdrew {amount} from {self.name}'s {account_name} account")
    def user_balance(self,account_name):
        if account_name in self.account:
            account = self.account[account_name]
            balance = account.balance
            # print(f"Your balance is {balance}")
            print(f"Your {account_name}'s balance is {balance}")
    def transfer(self,account_name,amount, other_user):
        if account_name in self.account:
            account = self.account[account_name]
            if account.balance >= amount:
                account.withdraw(amount)
                other_user.make_deposit(account_name, amount)

luna_lovegood=User("Luna Lovegood", "lunalovegood@gmail.com")
luna_lovegood.create_account("Checking",20,0)
luna_lovegood.create_account("Saving",15,200)
ronald_weasly=User("Ronald Weasly", "ronaldweasly@gmail.com")
ronald_weasly.create_account("Checking",15,100)
luna_lovegood.transfer("Saving",20,ronald_weasly)
ronald_weasly.user_balance("Checking")