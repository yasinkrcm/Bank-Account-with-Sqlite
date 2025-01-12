from database import *

class UserManagement:
    def checkUsers(self):
        if fetchDatas() == [] or fetchDatas() == None :
            print("Please add new accounts.")
            self.addAcc()

    def addAcc(self):
            createTable()
            name = input("Name: ")
            surname = input("Surname: ")
            accNo = input("Account No: ")
            balance = int(input("Your Balance: "))
            while balance < 0:
                print("Please enter a valid number!")
                balance = int(input("Your Balance: "))
            newUserInsert(name, surname, accNo, balance)

    def listUsers(self):
        self.checkUsers()
        for row in fetchDatas():
            print(f"""
    {row[0]}. Person
    NAME:  {row[1]}
    SURNAME:  {row[2]}
    ACCOUNT NO:  {row[3]}
    ACCOUNT BALANCE:  {row[4]}
    """)
            