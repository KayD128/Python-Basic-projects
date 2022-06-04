# def name_age():
#     name = input("Enter your name> ")
#     age = input("Enter your age> ")
#     print(name)
#     print(age)
# name_age()

# Transfer
# Register
# Cash withdrawal
# Balance enquiry
# PIN changeable
# Quit
import sys
from numpy import random
balance = 0.00


def transact_again():
    print("\n")
    transaction_option = input("Would you like to perform another transaction?>> ")
    if transaction_option.strip().lower() == "yes":
        menu()
    else:
        sys.exit


def menu():
    top_menu = ["1. Transfer", "2. Cash withdrawal", "3. Balance enquiry", "4. Deposit", "5. Back"]
    print("Welcome, pick out of any of the transactions below")
    for option in top_menu:
        print(option)
    user = input("Enter your Choice>> ")
    if user == "1":
        transfer()
    elif user == "2":
        cashWithdraw()
    elif user == "3":
        balanceCheck()
    elif user == "4":
        deposit()
    elif user == "5":
        opening_page()
    else:
        print("Error!! Invalid entry")
        opening_page()

def cashWithdraw():
    global balance
    print("\n")
    moneyToWithdraw = int(input("How much would you like to withdraw "))

    if moneyToWithdraw <= balance:
        balance = balance - moneyToWithdraw
        print("Please receive your money from the dispenser")
    elif moneyToWithdraw > balance:
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
    transact_again()
    # if amount_withdrawn == "1":
    #     print("Please take your N1000 cash from the dispenser")
    # elif amount_withdrawn == "2":
    #     print("Please take your N2000 cash from the dispenser")
    # elif amount_withdrawn == "3":
    #     print("Please take your N5000 cash from the dispenser")
    # elif amount_withdrawn == "4":
    #     print("Please take your N10,000 cash from the dispenser")
    # elif amount_withdrawn == "5":
    #     print("Please take your N20,000 cash from the dispenser")
    # elif amount_withdrawn == "6":
    #     print("Please take your N50,000 cash from the dispenser")
    # elif amount_withdrawn == "7":
    #     others = input("Fill in the amount you want to withdraw>> ")
    # else:
    #     print("Invalid amount")




def transfer():
    global balance
    print("\n")
    amount_transferred = int(input("How much would you like to transfer?>> "))

    if amount_transferred <= balance:
        account_transferred = int(input("Enter Account number>> "))
        if account_transferred in loginUser[4]:
            print("Transaction successful!!")
        else:
            print("Account doesn't exist")
    else:
        print("Insufficient Funds")
    
    
    
        # if account_transferred > 0:
        # print("\n")
        # print("Please wait while your request is being forwarded")
    transact_again()

def deposit():
    global balance
    moneyToDeposit = float(input("How much would you like to deposit? "))

    if moneyToDeposit > 0:
        balance += moneyToDeposit
        print("Your deposit has been added to your balance successfully")
    else:
        print("Invalid request, Try again")
        deposit() 
    # print("Input your Name and Age in the form below")
    # enterName = input("Enter your name ")
    # enterAge = input("Enter your age ")
    # enterAdress = input("Enter your adress ")
    # if enterName and enterAge and enterAdress in allUsersDetails:
    #     print("Please wait while new PIN is being generated")
    #     print("Your new PIN is: ", random.randint(10000))    
    # else: 
    #     print("Username not found, error!!01")
    transact_again()




def balanceCheck():
    global balance
    print("Your account balance is:", balance)
    transact_again()

allUsersDetails = dict()

def register():
    accountNumber = random.randint(1000000000)
    pinGenerated = random.randint(10000)
    print("\n")
    print("Thank you for choosing this bank. Register your details below")
    user_details = ["Full Name","age", "mail"]
    oneUserDetail = []
    for j in user_details:
        user_name = input("Enter " + j + ">> ")
        oneUserDetail.append(user_name)
    oneUserDetail.append(balance)
    allUsersDetails[accountNumber] = oneUserDetail
    print(allUsersDetails)
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
        register()
    oneUserDetail.append(accountNumber)
    oneUserDetail.append(pinGenerated)
    print(allUsersDetails)
    opening_page()

def login_page():
    global loginUser
    user_account = int(input("Enter your account number>> "))
    if user_account in allUsersDetails:
        loginUser = allUsersDetails.get(user_account)
        # print(loginUser)
    else:
        print("Incorrect password, Try again")
        login_page()

    user_pin = int(input("Enter your pin>> "))
    if user_pin == loginUser[5]:
        menu()
    else:
        print("Incorrect password, Try again")
        login_page()



def opening_page():
    print("Welcome to MyBank")
    first_option = ["1. Open Account", "2. Transact", "3. Quit"]

    for options in first_option:
        print(options)
    pick_first_option = input("Enter your choice> ")

    if pick_first_option == "1":
        register()
    elif pick_first_option == "2":
        login_page()
    elif pick_first_option == "3":
        sys.exit
    else:
        print("Error!! Try again")
        opening_page()
opening_page()

    
