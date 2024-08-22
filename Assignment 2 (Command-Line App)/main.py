from modules.Bank import *
from controllers.controllers import *

def main():
    bank = Bank()
    while True:
        start_menu_options()
        choice = int(input("Welcome to our banking system, please select an option to continue: "))
        if choice == 1:
            create_account(bank)
        elif choice == 2:
            access_account(bank)
        elif choice == 3:
            break      
        else:
            print("invalid option")


main()               







            












        

            

