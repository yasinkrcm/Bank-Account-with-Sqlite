from database import *
from userManagement import *

class Transaction(UserManagement):
    def __init__(self,user_manager):
        self.user_manager = user_manager

    def depositMoney(self):
        self.checkUsers()
        name = input("Name: ")
        surname = input("Surname: ")

        for row in fetchDatas():
            if row[1].capitalize() == name.capitalize() and row[2].capitalize() == surname.capitalize():    
                amount = int(input(f"Dear {row[1]} {row[2]}, How much would you like to deposit: "))
                if amount < 0:
                    print("Please enter a valid number!")
                    return 0
                else:
                    newBalance = row[4] + amount
                    print(f"\nDear {row[1]} {row[2]}, {row[3]} Account No: {amount} has been deposited to your account!\n\nYour New Balance: {newBalance}\n")
                    updateBalance(newBalance, row[4])
            else:
                print(f"{name}, {surname} user not found.")


    def WithdrawMoney(self):
        self.checkUsers()
        name = input("Name: ")
        surname = input("Surname: ")

        for row in fetchDatas():
            if row[1].capitalize() == name.capitalize() and row[2].capitalize() == surname.capitalize():    
                amount = int(input(f"Dear {row[1]} {row[2]}, How much would you like to withdraw: "))
                if amount < 0:
                    print("Please enter a valid number!")
                    return 0
                else:
                    newBalance = row[4] - amount
                    if row[4] >= amount:
                        try:
                            print(f"Dear {row[1]} {row[2]}, {row[3]} Account No: {amount} has been withdrawn from your account!\n\nYour New Balance: {newBalance}\n")
                            updateBalance(newBalance, row[4])
                        except ValueError:
                                print("Please enter a valid number!")
            else:
                print(f"\nDear {row[1]} {row[2]}, {row[3]} Account No: Insufficient funds in your account to complete the transaction!\n")
        