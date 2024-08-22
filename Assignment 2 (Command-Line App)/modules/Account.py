class Account:

    # constructor 
    def __init__(self, account_number, account_holder, password, balance=0):
        self.account_number = account_number
        self.account_holder =account_holder
        self.password = password
        self.balance = balance

    # deposit to account 
    def deposit(self, amount):
        self.balance += amount
        balance_update_message("deposited", amount, self.balance)

    # withdraw from account 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")

        self.balance -= amount
        balance_update_message("withdrawn", amount, self.balance)


    # check for balance 
    def check_balance(self):
        print(f"your balance is UGX {self.balance}")  


# helper func for printing out withdraw or deposit message 
def balance_update_message(action, amount, balance):
    print(f"you have {action} UGX {amount}, your new balance is UGX {balance}")
