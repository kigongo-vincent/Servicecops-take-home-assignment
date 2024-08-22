from utils.options import *

def create_account(bank):
    account_holder = input("Your name: ")
    password = input("Please enter the password you'd like to use: ")
    if account_holder and password:
        bank.create_account(account_holder, password)
    else:    
        print("please fill out all the information")

def access_account(bank):
            account_number = input("Please enter your account number: ")
            password = input("Provide your password: ")

            if account_number and password:
                account = bank.authenticate(account_number, password)

                if account:
                    while True:
                        account_options()

                        choice = int(input("Please select what you'd wish to do: "))

                        if choice == 1:
                            deposit_amount = int(input("Please enter the amount to deposit (UGX): "))
                            if deposit_amount:
                                account.deposit(deposit_amount)
                                bank.save_data()
                            else:
                                print("invalid input!")

                        elif choice == 2:
                            withdraw_amount = int(input("Please enter the amount to withdraw (UGX): "))
                            if withdraw_amount:
                                account.withdraw(withdraw_amount)
                                bank.save_data()

                        elif choice == 3:
                            account.check_balance()   
                            

                        elif choice == 4:
                            bank.save_data()
                            break   

                        else:
                            print("invalid option")      
            else:    
                print("please fill out all the information")      
