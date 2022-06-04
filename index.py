# fName, lName, location, state = "Kolade", "Ogunleye", "Ogbomoso", "Oyo"
# score = 100
# score = 200
# print("My full name is "+ fName + " "+ lName + ". I stay at "+ location + ", " + state +" state and my total score is "+ str(score) +" in Mathematics.")

# firstName = input("Enter your name ")
# val1 = input("Enter first value ")
# val2 = input("Enter second value ")
# score = float(val1) + float(val2)
# print("Welcome " + firstName + " your total score is " + float(score))
# This is written to score someone

# a = 20

# enterFirstName = input("") 

# def addition():
#     global a
#     a = 30
#     b = 10
#     score = a + b
#     print("The addition is ", score)

# def addition(a, b):
#     score = a + b
#     print(score)
#     print("The addition is ", score)

# def subtract():
#     b = 10
#     score = a - b
#     print("Subtraction is ", score)

# addition()
# subtract()

# firstName = input("Enter your name ")
# val1 = input("Enter first value ")
# val2 = input("Enter second value ")
# score = float(val1) * float(val2)
# print("Welcome " + firstName + " your total score is " + str(score))

# Day 2
# Identity Operator: is, is not
# membership operator: in, not in
# Bitwise operator: &, |, ^, ~, <<, >>

# fval = 5
# sval = 3
# print('for addition '+str(fval + sval))
# print('for subtraction '+str(fval - sval))
# print('for multiplication '+str(fval * sval))
# print('for division '+str(fval / sval))
# print('for modulus '+str(fval % sval))
# print('for exponentiation '+str(fval ** sval))
# print('for floor division '+str(fval // sval))

# fval = 10
# sval = 5
# print(fval == sval)
# print(fval != sval)
# print(fval > sval)
# print(fval < sval)
# print(fval >= sval)
# print(fval <= sval)

# print((fval == sval or fval >= sval) and (fval > sval and fval >= sval))

# Bitwise operators
# fval = 45
# sval = 36
# print(bin(fval))
# print(bin(sval))
# print(bin(fval & sval))
# print(bin(fval | sval))
# print(bin(sval ^ fval))
# print(bin(~ fval))
# print(bin(sval << 2))
# print(bin(sval >> 2))

# Assignment
# write an application that wwill ask for name and 2 values and display operators which are add, sub, multiplication and division

# name = 'sunday'
# print(name[2])
# print(name[0:3])  #slicing
# print(len(name))

comment = '''My name is kolade and im from ogbomoso. I go to SQI'''
# if your string statement is taking more than a line use a triple quote. Just like you use quotes for
# multilined comments
# negative index starts counting from the back

# STRING METHODS   
# print(comment.startswith("commented"))
# print(comment.endswith("SQI"))
# print("The length of comment is ", len(comment))

# the space before first char is leading space and the one after is trailing space and they are all known as Y space
# Strip function

# val1 = float(input("enter value 1>> "))
# val2 = float(input("enter value 2 "))
# print('addition \n subtraction')

# oper = input('enter operation ')
# if oper.strip().lower() == 'addition':
#     print(val1 + val2)
# elif oper.strip() == 'subtraction':
#     print(val1 - val2)
# else:
#     print("Invalid solution")

# Lower function
# name = 'SUNDAY'
# print(name.lower())

# value = 'method'
# user = input("please enter 'method' to continue ")
# if value == user.lower():
#     print(user, 'is correct')
# else: print("invalid input")

# # There is also replace function, split function, count, encode, center, format

# print(comment.split('.'))

# Join() function
# word_split = comment.split() # This is provided you have used the split function
# print(word_split)
# print(" ".join(word_split))


# Python collection (Array)
# They are types of variables that can hold multiple variables at a time.
# list
# tuple
# set
# dictionary

# List: is a collection which is ordered and changeable
# use square bracket or constructor
# my_list = ["shade", "energy", "magnet", "charse", "light"]
# my_list2 = list(()) 
# for name in my_list
#     print(name)

# we use "append" to add to the list
# also you can use insert but you have to put a number
# my_list.insert(3, tunde)
# my_list.extend(my_list2)

# for name in my_list2:
#     my_list.append(name)

# my_list.remove("energy")

# output = []
# for name in my_list:
#     if "e" in name:
#         value = "".join(name.split('e'))
#         output.append(value)
#         print(output)

# can use .pop to remove any word also .index to get the index and .clear to clear the whole thing
# del which is a keyword can also delete the list
# .sort will the list in ascending order, for descending order is .sort(reverse=True)
# .reverse is just for rotating the values
# .copy is to put itemsin one list to another empty list or use name = list(my_list2)
# if you use + operator to concatenate it, they will merge
# .count is to give number of a particular item
# num = 0
# questions = ["Who is the president of Nigeria?", "What zone is Lagos located in?", "What is the currency in Nigeria?"]
# options = ["(a) Obasanjo (b) Osinbanjo (c) Buhari", "(a) SW (b) SS (c) NE", "(a) dollars (b) naira (c) euros"]
# answer = ["c", "a", "b"]
# score = 0

# for que in questions:
#     print(que)
#     print(options[num])
#     user = input(">> ")
#     if user.strip().lower() == answer[num]:
#         print("You are right")
#         score += 5
#     else:
#         print("You are wrong")
#     num += 1
# print("Your total score is", score)

# Assignment
# Name matric no and class and also return the highest number of student with score


# Tuple
# It is a collection that is ordered but not changeable. It is created using braces i.e () or tuple()
# unpacking values in a tuple

# set is a collection which is unordered AND unindexed
# difference btw discard and .remove, discard wont output error if the item is not existing in the set
# can be used to perform mathematical equation like the normal sets
# you can use union and also use update, update will just override the first set, it wont bring in a new variable

# print("You can only supply 5 numbers")
# set1 = set()
# for i in range(5):
#     user = input("enter your value ")
#     set1.add(user)
# print(set1)

# # OR

# print("You can only supply 5 numbers")
# set1 = set()
# set2 = set()
# set3 = set()
# group = [set1, set2, set3]
# for i in range(3):
#     for i in range(5):
#         user = input("enter your value " + str(i+1))
#         # set1.add(user)
#         group[i].add(user)
# print(set1)
# print(set2)
# print(set3)

# an app that collects 2 sets and asks if u want union or intersection for it 

# Dictionary is ordered changeable and also unindexed and does not accept duplicate
# it comes in key:value pairs
# # example
# product = {'producer':'Toyota', 'model':'venza 2021', 'engine':'6 engine', 'color': 'black', 'gear': 6, 'ok':True}

# print(product["color"])
# print(product.get("producer"))
# print(product.keys())
# print(product.values())
# product.update({"year":2021, "color": "white"})
# product.update(dict("year": 2021, "color": "white"))
# product.pop('color')

# student_record = dict(name = "Tony Johnson", level = 300, course = 'MCE', subjects = 10)
# for x in student_record:
#     print(x) - to return keys alone

# for x in student_record:
#     print(student_record[x]) - to return keys and values

# for x, y in student_record.items():
#     print(x + "=", y)

# Assignment
# do ussd
# from numpy import random
# print(random.randint(1000000000))
# print(random.randint(10000))

# conditional statements

# food_list = ['rice', 'beans', 'yam']
# food = input("Enter what you will buy ")
# for fo in food_list: 
#     if food.split() in food_list:
#         print("I will buy ", fo)
#     else:
#         print("I will not buy ", fo)

# x = 1
# while x <= 10:
#     print("Welcome to today's class", x)
#     x+=1 

# x = 10
# while x > 0:
#     if x == 5:
#         break
#     print("I will not do it again", x)
#     x -= 1

# std_name = []
# x = 1
# while x <= 10:
#     print()
#     name = input()
#     if name == "q":
#         break
#     std_name.append(name)
#     x+=1
# print(std_name)

# x = 10
# while x> 0:
#     age = input("Enter your age ")
#     if int(age) < 18:
#         print("Too young")
#         continue
#     print("Please take your ticket and enter the hall", x)

# when the whilw loop is through, you can put the else to print something else

# functions
# you delare function with def functionName(parameter_a, parameter_b):
# THen function declaration is next and tell it what to do
# function invocation is when you tell it what to do

# val1 = 50
# val2 = 20
# def addition():
#     """This is a function that displays the addition of two values"""
#     # A docstring, used for explaining the function of variable
#     result = val1 + val2
#     print(result)
# addition()


# you can import sys and use it for maybe sys.exit()
# allUserDetails = []
# for loop

# Object Oriented Programming (OOP)
# Objects attributes and methods (Functions)
# The name if every calss should start with capital letter.
# Example

# class Car:
#     owner = "John Smith"
#     location = "Lagos"
#     gear = 5
#     tire = 4

#     def run(self, value):
#         print("the car is running at full speed of "+value)

#     def pack(self):
#         print("the car just packed now.") 

# myCar = Car()
# print(myCar.gear)
# myCar.run("34")
# myCar.location = "Abuja"

# import time

# class Car:
#     def __init__(self):
#         self.owner = "John Smith"
#         self.location = "Ogbomoso"
#         self.name = "Toyota"
#         self.color = "Brown"
#         self.brand = "2019 model"
#         self.trafficator = "straight"
#         self.tyre = 4
#         self.steering = 1
#         self.gear = "0"
#         self.details()

#     def details(self):
#         print("This car is owned by "+ self.owner + " and is located in " + self.location)
#         time.sleep(2)
#         self.startEngine()

#     def startEngine(self):
#         print("The engine has started")
#         time.sleep(2)
#         self.gear = input("Enter gear 1 to take off")
#         if self.gear == "1":
#             self.moveCar()
#         else:
#             print("That is not the right gear to take off")
#             self.startEngine()

#     def moveCar(self):
#         print(self.name+ " is in gear " + self.gear + "and the car is moving " + self.trafficator)
#         self.driver = input("press Y to change gear, D to change direction and P to pack")
#         if self.driver.upper() == "Y":
#             self.changeSpeed()
#         elif self.driver.upper() == "D":
#             self.direction()
#         elif self.driver.upper() == "P":
#             self.park()
#         else:
#             self.moveCar()

#     def changeSpeed(self):
#         self.gear = input("Enter gear number ")
#         if self.gear == "1":
#             self.moveCar()
#         elif self.gear == "2":
#             self.moveCar()
#         elif self.gear == "3":
#             self.moveCar()
#         elif self.gear == "4":
#             self.moveCar()

#     def direction(self):
#         self.trafficator = input("please enter your direction ")
#         if self.trafficator.lower() == "straight":
#             self.moveCar()
#         elif self.trafficator.lower() == "left":
#             self.moveCar()
#         elif self.trafficator.lower() == "right":
#             self.moveCar()

#     def park(self):
#         print('the car is parking now... ')
#         time.sleep(2)
#         print("The car has finished parking and application exited")

# cr = Car()

# PYTHON INHERITANCE
# class Father:
#     def __init__(self):
#         self.family_name = "Adeowo"
#         self.name = "Owolabi"
#         self.language = "Yoruba"
#         self.height = "tall"
#         self.skinColour = "Dark"

#     def walk(self):
#         print(self.name + " is walking")

#     def talk(self):
#         print(self.name + " is talking")

#     def sleep(self):
#         print(self.name + " is still sleeping")


# class Child1(Father):
#     def __init__(self):
#         Father.__init__(self)
# or      super().__init__()
    #     self.name = "Johnson"
    #     self.height = "short"

    # def run(self):
    #     print(self.name+ " is running up and down")

    # pass

# fd = Father()
# print("Father: ", fd.name)

# ch = Child1()
# ch.run()
# ch.name = "Sunday"
# print("Child: ", ch.name)

# class Child2(Father):
#     def __init__(self):
#         Father.__init__(self)
# or      super().__init__()
        # self.name = "Charles"
        # self.height = "short"

    # def jump(self):
    #     print(self.name+ " is running up and down")

# fd = Father()
# ch = Child1()
# ch2 = Child2()
# ch.talk()
# print(ch.name)
# fd.talk()
# print(ch2.family_name)

# class GrandChild(Child1):
#     def __init__(self):
#         super().__init__()
#         self.name = "Micheal"

# ch = Child1()
# print(ch.language)
# ch.walk()
# gd = GrandChild()
# gd.run()
# gd.walk()


#PYTHON MODULE
# import atmmodule as am
# am.UssdAtm.registerUssd()

# OR
# from atmmodule import UssdAtm as ua
# ua.intro()

# from atmmodule.Atm import register
# register()

# import numpy
# print(dir(numpy))
# print(numpy.random.randint(1, 10))
# from numpy import linspace, argmin, ones
# print(linspace(1, 10, 5)) 

# Python Database (Mysql)
# To download mysql connector user: pip install "Library name" in this case mysql-connector

# print("Twinkle, twinkle, little star,\n How I wonder what you are!\n Up above the world so high,\n Like a diamond in the sky.\n Twinkle, twinkle, little star,\n How I wonder what you are")

# File Handling
# myFile = open("filename", mode = 'r', 'a', 'w', 'x', encoding = 't', 'b')
# 'r': is read only and default for open function. It will raise error if file doesnt exist.
# 'a': Append new content in the file. If the file doesnt exist, it will create new file
# 'w': Open file for writing. wil also create file if it doesnt exist.
# 'x': To create new file. will raise error if file exists

# with open("filename", mode = "rt") as myFile:

# myFile = open('C:\\Users\\USER\\Desktop\\Python class\\lessons.txt', 'rt')
# print(myFile.read())
# print(myFile.read(20))
# for i in range(20):
#     print(myFile.readline())

# for text in myFile:
#     print(text)

# using with open
# with open("infile.txt", mode='rt') as myFile:
#     print(myFile.read())

# myFile = open("infile2.txt", 'a')
# myFile.write("\n this is a new content to append to the old file")
# print("text appended successfully")

# myFile = open("infile,txt", 'w')
# myFile.write("This is use to add another content to the file")

# myFile = open()


# import os
# if os.path.exixts("new file,txt"):

# mkdir new folder, will create folder for u on command prompt
# import time
# for roots, dirs, files in os.walk("new folder"):
#     print("Wait while folder is being deleted")
#     time.sleep(3)
#     for dir in dirs:
#         os.remove ("new folder\\"+dir)
#     print("Please wait while files are being deleted")
#     time.sleep(3)
#     for file in files:
#         os.remove("new folder\\"+file)

# print("Wait while file is")
# time.sleep(3)
# os.rmdir("New Folder")

# import os path
# create an application that will copy content of one file and paste in another

# import os
# if os.path.exists("newfile.text"):
#     with open("newfile.txt", mode = 'rt') as myFile:
#         print(myFile.read())
# else:
#     print("file does not exists")
#     with open("newfile.txt", mode = 'xt') as myFile:
#         print("file created successfully")


# Python Error Handling
# Compile time error and run time error

# TRY AND EXCEPT, Finally

# def simpleCal():
#     for i in range(5):
#         a = input("enter your number")
#         b = input("Entr ur number")
#         print(a/b)
# simpleCal()


# def cal():
#     for i in range(5):
#         a = int(input("enter your number"))
#         b = int(input("Entr ur number"))
#         try:
#             print(a/b)
#         except:
#             print("divisor cannot be zero")
# cal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter your number"))
#             b = int(input("Entr ur number"))
#             print(a/b)
#         except:
#             print("divisor cannot be zero")
# cal()

# import re
# a = input("enter your number")
# b = input("Entr ur number")
# if re.search(r'[a-zA-Z]', a) or re.search(r'[a-zA-Z]', b):
#     raise TypeError("divisor must be an integer")
# else:
#     print(int(a)/int(b))


# Python Regular Expression or RegEx
# A sequence of character used to form pattern of search

# import re
# text = """the value of a thing will det the capacity u put in it"""
# val = re.search("^the.*it$", text)
# print(val)
# if val:
#     print("We have a match")
# else:
#     print("No match")

# Python DateTime
# import datetime as dt
# tim = dt.datetime.now()
# print(tim)
# print(tim.date())
# print(tim.time())
# print(tim.year)
# print(tim.month)
# print(tim.day)
# print(tim.hour)
# print(tim.microsecond)

# tm = dt.datetime(2021, 4, 10)
# print(tm)

# tom = dt.datetime(2021, 4, 10, 12, 30, 20)
# print(tom)

# strftime() method- use to format datetime object in readable form  

# import math
# me = math.gcd(10, 60)
# print(me)

# words = "I didn't know there was yam available"
# myWords = list(words)
# print(myWords)

