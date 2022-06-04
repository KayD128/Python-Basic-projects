import mysql.connector as sql

# mycursor.execute("CREATE DATABASE onlineweb_db")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE customers_sheet(ctm_id INT(4), Account_Number VARCHAR(10), Full_Name VARCHAR(20), Age INT(3), PIN VARCHAR(4), Mail VARCHAR(30), Balance INT(7))")

# mycursor.execute("ALTER TABLE customers_sheet CHANGE result_sheet Customer_id INT(4) PRIMARY KEY AUTO_INCREMENT")

# mycursor.execute("ALTER TABLE customers_sheet ADD UNIQUE(Account_Number);")
# mycursor.execute("ALTER TABLE customers_sheet ADD UNIQUE(PIN);")
# mycursor.execute("ALTER TABLE customers_sheet ADD UNIQUE(Mail);")

import sys
from numpy import random
import time

class Atm:
    def __init__(self):
        self.balance = 0.00
        self.mycursor = ""
        self.mycon = ""
        self.opening_page()
        # self.connection()

    def connection(self):
        self.mycon = sql.connect(host = '127.0.0.1', user = 'root', passwd = '', database = 'onlineweb_db' )
        self.mycursor = self.mycon.cursor()

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
        self.connection()
        self.user_account = int(input("Enter your account number>> "))
        # if user_account in self.allUsersDetails:
        #     self.loginUser = self.allUsersDetails.get(user_account)
        #     # print(loginUser)
        # else:
        #     print("Incorrect password, Try again")
        #     self.login_page()

        user_pin = int(input("Enter your pin>> "))
        # if user_pin == self.loginUser[5]:
        #     self.menu()
        # else:
        #     print("Incorrect password, Try again")
        #     self.login_page()
        query = "SELECT Account_Number, PIN FROM customers_sheet WHERE Account_Number=%s AND PIN=%s"
        val = (self.user_account, user_pin)
        self.mycursor.execute(query, val)
        myreg = self.mycursor.fetchone()
        self.mycon.close()
        if myreg:
            print("Access Granted")
            self.menu()

        else:
            print("Access Denied")
            self.login_page()

    def register(self):
        oneUserDetail = []
        self.connection()
        accountNumber = random.randint(1000000000)
        pinGenerated = random.randint(10000)
        print("\n")
        print("Thank you for choosing this bank. Register your details below")
        user_details = ["Full Name","age", "mail"]
        for j in user_details:
            user_name = input("Enter " + j + ">> ")
            oneUserDetail.append(user_name)

        if oneUserDetail != " ":
            print("\n")
            print("Please wait, Your PIN and Account Number is being generated")        
        else: 
            print("Fill in your details, please")
            self.register()
        myquery = "INSERT INTO customers_sheet(Account_Number, Full_Name, Age, PIN, Mail, Balance) VALUES(%s, %s, %s, %s, %s, %s)"
        value = (accountNumber, oneUserDetail[0], oneUserDetail[1], pinGenerated, oneUserDetail[2], self.balance)
        self.mycursor.execute(myquery, value)
        self.mycon.commit()
        print(self.mycursor.rowcount, "registered successfully")
        self.mycon.close()
        # print(self.allUsersDetails)
        # while True:
        #     for j in user_details:
        #         user_name = input("Enter " + str(j) + ">> ")
        #         oneUserDetail.append(user_name)
        #     print(oneUserDetail)

        print(value)
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
        self.connection()
        query = "SELECT Balance FROM customers_sheet WHERE Account_Number = %s"
        val = (self.user_account, )
        self.mycursor.execute(query, val)
        myreg2 = self.mycursor.fetchone()

        moneyToWithdraw = int(input("How much would you like to withdraw "))

        if moneyToWithdraw <= self.balance:
            self.balance = self.balance - moneyToWithdraw
            print("Please receive your money from the dispenser")
        elif moneyToWithdraw > self.balance:
            print("Insufficient Funds")
        else:
            print("Error, Try again later")
            
        # amount_withdrawn = input("Enter the number chosen here>> ")
        sql = "UPDATE customers_sheet SET Balance = %s WHERE Account_Number = %s"
        value = (self.balance, self.user_account)
        self.mycursor.execute(sql, value)
        self.mycon.commit()
        # print(mycursor.rowcount, 'record updated successfully')
        self.mycon.close()
        self.transact_again()


    def transfer(self):
        print("\n")
        self.connection()
        query = "SELECT Balance FROM customers_sheet WHERE Account_Number = %s"
        val = (self.user_account, )
        self.mycursor.execute(query, val)
        myreg3 = self.mycursor.fetchone()

        amount_transferred = int(input("How much would you like to transfer?>> "))
        account_transferred = input("Enter Account number>> ")
        query = "SELECT Balance, Account_Number FROM customers_sheet WHERE Account_Number = %s"
        val = (account_transferred, )
        self.mycursor.execute(query, val)
        myreg2 = self.mycursor.fetchone()
        
        # print(myreg2)
        recipient_amount = myreg2[0]
        owner_amount = myreg3[0]

        if owner_amount >= amount_transferred:
            if myreg2:
                owner_amount -= amount_transferred
                recipient_amount += amount_transferred
                sql = "UPDATE customers_sheet SET Balance = %s WHERE Account_Number = %s"
                value = (owner_amount, self.user_account)
                self.mycursor.execute(sql, value)
                # print(mycursor.rowcount, 'record updated successfully')
                self.mycon.commit()

                sql2 = "UPDATE customers_sheet SET Balance = %s WHERE Account_Number = %s"
                value2 = (recipient_amount, account_transferred)
                self.mycursor.execute(sql2, value2)
                self.mycon.commit()
                self.mycon.close()

                print("Transaction successful!!")
            else:
                print("Account doesn't exist")
        else:
            print("Insufficient Funds") 
        
        self.transact_again()

    def deposit(self):
        self.connection()
        query = "SELECT Balance FROM customers_sheet WHERE Account_Number = %s"
        val = (self.user_account, )
        self.mycursor.execute(query, val)
        myreg2 = self.mycursor.fetchone()

        moneyToDeposit = float(input("How much would you like to deposit? "))

        if moneyToDeposit > 0:
            self.balance += moneyToDeposit
            print("Your deposit has been added to your balance successfully")
        else:
            print("Invalid request, Try again")
            self.deposit() 
        sql = "UPDATE customers_sheet SET Balance = %s WHERE Account_Number = %s"
        value = (self.balance, self.user_account)
        self.mycursor.execute(sql, value)
        self.mycon.commit()
        # print(mycursor.rowcount, 'record updated successfully')
        self.mycon.close()  
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
        self.connection()
        query = "SELECT Balance FROM customers_sheet WHERE Account_Number = %s"
        val = (self.user_account, )
        self.mycursor.execute(query, val)
        myreg = self.mycursor.fetchone()
        my_amount = myreg[0]
        # print(myreg)

        print("Your account balance is: " + str(my_amount))
        self.mycon.commit()
        # print(mycursor.rowcount, 'record updated successfully')
        self.mycon.close()  


        self.transact_again()

    
    def transact_again(self):
        print("\n")
        transaction_option = input("Would you like to perform another transaction?>> ")
        if transaction_option.strip().lower() == "yes":
            self.menu()
        else:
            sys.exit

atm = Atm()




