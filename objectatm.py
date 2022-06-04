# def name_age():
#     name = input("Enter your name> ")
#     age = input("Enter your age> ")
#     print(name)
#     print(age)
# name_age()

import sys
from numpy import random
import time

class Atm:
    def __init__(self):
        self.balance = 0.00
        self.allUsersDetails = dict()
        self.opening_page()

    def opening_page(self):
        print("Welcome to MyBank")
        first_option = ["1. Open Account", "2. Transact", "3. Quit"]

        for options in first_option:
            print(options)
        pick_first_option = input("Enter your choice> ")

        if pick_first_option == "1":
            self.register()
        elif pick_first_option == "2":
            self.login_page()
        elif pick_first_option == "3":
            sys.exit
        else:
            print("Error!! Try again")
            self.opening_page()

    def login_page(self):
        user_account = int(input("Enter your account number>> "))
        if user_account in self.allUsersDetails:
            self.loginUser = self.allUsersDetails.get(user_account)
            # print(loginUser)
        else:
            print("Incorrect password, Try again")
            self.login_page()

        user_pin = int(input("Enter your pin>> "))
        if user_pin == self.loginUser[5]:
            self.menu()
        else:
            print("Incorrect password, Try again")
            self.login_page()

    def register(self):
        accountNumber = random.randint(1000000000)
        pinGenerated = random.randint(10000)
        print("\n")
        print("Thank you for choosing this bank. Register your details below")
        user_details = ["Full Name","age", "mail"]
        oneUserDetail = []
        for j in user_details:
            user_name = input("Enter " + j + ">> ")
            oneUserDetail.append(user_name)
        oneUserDetail.append(self.balance)
        self.allUsersDetails[accountNumber] = oneUserDetail
        print(self.allUsersDetails)
        # while True:
        #     for j in user_details:
        #         user_name = input("Enter " + str(j) + ">> ")
        #         oneUserDetail.append(user_name)
        #     print(oneUserDetail)

        if oneUserDetail != " ":
            
            print("\n")
            print("Please wait, Your PIN and Account Number is being generated")        
            print("Your accoount number is: ", accountNumber)
            print("Your PIN is: ", pinGenerated)    
        else: 
            print("Fill in your details, please")
            self.register()
        oneUserDetail.append(accountNumber)
        oneUserDetail.append(pinGenerated)
        print(self.allUsersDetails)
        self.opening_page()


    def menu(self):
        top_menu = ["1. Transfer", "2. Cash withdrawal", "3. Balance enquiry", "4. Deposit", "5. Back"]
        print("Welcome, pick out of any of the transactions below")
        for option in top_menu:
            print(option)
        user = input("Enter your Choice>> ")
        if user == "1":
            self.transfer()
        elif user == "2":
            self.cashWithdraw()
        elif user == "3":
            self.balanceCheck()
        elif user == "4":
            self.deposit()
        elif user == "5":
            self.opening_page()
        else:
            print("Error!! Invalid entry")
            self.opening_page()


    def cashWithdraw(self):
        print("\n")
        moneyToWithdraw = int(input("How much would you like to withdraw "))

        if moneyToWithdraw <= self.balance:
            self.balance = self.balance - moneyToWithdraw
            print("Please receive your money from the dispenser")
        elif moneyToWithdraw > self.balance:
            print("Insufficient Funds")
        else:
            print("Error, Try again later")
            
        # amount_withdrawn = input("Enter the number chosen here>> ")
            
        # number = 0
        # for x in amounts[number]:
        #     for y in options_to_pick[number]:
        #         if options_to_pick[number] == amount_withdrawn:
        #             print("Please take your"+ amounts[number] +" cash from the dispenser")     
        #     number += 1
        # menu()
        self.transact_again()


    def transfer(self):
        print("\n")
        amount_transferred = int(input("How much would you like to transfer?>> "))

        if amount_transferred <= self.balance:
            account_transferred = int(input("Enter Account number>> "))
            if account_transferred in self.loginUser[4]:
                print("Transaction successful!!")
            else:
                print("Account doesn't exist")
        else:
            print("Insufficient Funds")
        
        
        
            # if account_transferred > 0:
            # print("\n")
            # print("Please wait while your request is being forwarded")
        self.transact_again()

    def deposit(self):
        moneyToDeposit = float(input("How much would you like to deposit? "))

        if moneyToDeposit > 0:
            self.balance += moneyToDeposit
            print("Your deposit has been added to your balance successfully")
        else:
            print("Invalid request, Try again")
            self.deposit() 
        # print("Input your Name and Age in the form below")
        # enterName = input("Enter your name ")
        # enterAge = input("Enter your age ")
        # enterAdress = input("Enter your adress ")
        # if enterName and enterAge and enterAdress in allUsersDetails:
        #     print("Please wait while new PIN is being generated")
        #     print("Your new PIN is: ", random.randint(10000))    
        # else: 
        #     print("Username not found, error!!01")
        self.transact_again()


    def balanceCheck(self):
        print("Your account balance is:" + self.balance)
        self.transact_again()

    
    def transact_again(self):
        print("\n")
        transaction_option = input("Would you like to perform another transaction?>> ")
        if transaction_option.strip().lower() == "yes":
            self.menu()
        else:
            sys.exit

auto = Atm()

    
