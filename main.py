from transaction import *
from userManagement import *



def menu():
    print("""
1- Add New Account
2- View Accounts
3- Deposit Money
4- Withdraw Money
5- Exit
""")
    return input("Choose an option: ")

def main():

    user_manager = UserManagement()
    transaction_manager = Transaction(user_manager)

    while True:
        # try: 
            choice = menu()
            if choice == "1": 
                user_manager.addAcc()
            elif choice == "2":
                user_manager.listUsers()
            elif choice == "3":
                transaction_manager.depositMoney()
            elif choice == "4":
                transaction_manager.WithdrawMoney()
            elif choice == "5":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
        # except Exception as e:
        #     print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()