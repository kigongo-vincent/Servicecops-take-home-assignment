import random
import json
from modules.Account import *

class Bank:

    # constructor 
    def __init__(self):
        self.accounts = {}
        self.load_data()

    # fetch saved data 
    def load_data(self):
        try:

            with open("data/accounts.json", "r") as file:
                stored_accounts = json.load(file)
                accounts = dict()  
                for key, value in stored_accounts.items():
                    account = Account(value["account_number"], value["account_holder"], value["password"], value["balance"])
                    accounts[key] = account
                self.accounts = accounts   
                    
        except:
            pass

    # save snapshots of changes made on the system 
    def save_data(self):
        with open("data/accounts.json", "w") as file:
            json.dump(serialize_accounts(self.accounts), file)
            self.load_data()
            print("done")

    # register users 
    def create_account(self, account_holder, password):

        if account_holder in self.accounts:
            print("Account holder already exists")

        else:
            new_account_number = str(random.randint(100000,999999))
            new_account = Account(new_account_number, account_holder, password)
            self.accounts[new_account_number] = new_account
            self.save_data()
            print(f"account for {account_holder} has been created successfully with account number: {new_account_number}")

    # login users 
    def authenticate(self, account_number, password):
        if account_number in self.accounts and self.accounts[account_number].password == password:
            return self.accounts[account_number]

        else:
            print("invalid credentials, please try again")
            return

# helper function for converting account objects into dictionaries
def serialize_accounts(accounts):
    serialized_accounts = dict()
    for key, value in accounts.items():
        account = {
            "account_number": value.account_number,
            "account_holder": value.account_holder,
            "balance": value.balance,
            "password": value.password,
            }
        serialized_accounts[key] = account 
    return serialized_accounts      