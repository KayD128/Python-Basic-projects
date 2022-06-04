# set1 = set(input("Enter your first set>> "))
# set2 = set(input("Enter your second set>> "))

# print(set1)
# set1 = set()
# for i in range(5):
#     number1 = input("Type your first set value here>> ")
#     set1.add(number1)
# print(set1)

# set2 = set()
# for i in range(5):
#     number2 = input("Type your second set value here>> ")
#     set2.add(number2)
# print(set2)

# intersect_set = set1.intersection(set2)
# union_set = set1.union(set2)
# operation = input("Enter the operation you want to perform>> ")

# if operation.strip().lower() == "intersect":
#     print(intersect_set)
# elif operation.strip().lower() == "union":
#     print(union_set)
# else:
#     print("Error")
# print(intersect_set)
# print(union_set)

# address = {"state": "Texas", 'city': 'Houston'}

# person = {'name': 'Jessa', 'company': 'Google', 'address': address}

# print("person:", person)
# print("City:", person['address']['city'])

# print("Person details")
# for key, value in person.items():
    # if key == 'address':
        # Iterating through nested dictionary
    #     print("Person Address")
    #     for nested_key, nested_value in value.items():
    #         print(nested_key, ':', nested_value)
    # else:
    #     print(key, ':', value)

# list1 = ["Ten", "Twenty", "Thirty"]
# list2 = [10, 20, 30]
# myDict = dict()
# number = 0
# for x in range(len(list1)):
    # for y in list2:
#     myDict.update({list1[x]: list2[x]})
# print(myDict)

# number += 0


# employees = ["Kolade", "Yemi"]
# works = {"Designation": "Developer", "salary": 80000}

# total = dict.fromkeys(employees, works)
# print(total)

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# for x in sample_dict.values():
#     print(x)

# if 200 in sample_dict.values():
#     print("200"+ "is in the list")

# people = ["Kolade", "January", "Carpicorn", "Tall", "Sleep"]
# others = dict()
# me = int(input("Enter your value here>> "))
# others[me] = people
# print(others)
# if me in people:
#     myself = others.get(me)
#     print(myself)

# self.allUsersDetails[accountNumber] = oneUserDetail


# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# for x in sample_dict.values():
#     print(min(x))


# class Vehicle:
#     def __init__(self):
#         self.name = "School volvo"
#         self.max_speed = 180
#         self.mileage = 20
#         self.capacity = 4

#     def seating_capacity(self):
#         print("The seating capacity of", self.name, "is", self.capacity, "passengers")

# class Bus(Vehicle):
#     def __init__(self):
#         Vehicle.__init__(self)
#         self.capacity = 50

# bus = Bus()
# bus.seating_capacity()
# print("Vehicle Name: ", bus.name, "Mileage: ", bus.max_speed, "max_speed: ", bus.mileage)

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Bus(Vehicle):
#     # assign default value to capacity
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)

# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.seating_capacity())

# import datetime
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print(f_extns)
# print ("The extension of the file is : " + f_extns[-1])

# exam_st_date = (11, 12, 2014)
# print(str(exam_st_date[0]), "/" + str(exam_st_date[1]), "/" + str(exam_st_date[2]))

# print("Hello, My name is {}. I am a {} and also like {}.".format("Kolade", 'Student', 'Programming'))

# print("I went to {0} with {name}.\nIt was {adjective}.\nWe waited for {hours} hours to ride {ride}.".format("Disneyland", name="Kolade", adjective="Frustrating", hours = 11, ride = "rollercoaster"))

# n = int(input('Enter a number '))
# n1 = int("%s" %(n))
# n2 = int("%s%s" %(n, n))
# n3 = int("%s%s%s" %(n, n, n))
# fact = n1 + n2 + n3
# print(fact) 

# rankings = {"Gonzaga": 31, "Baylor": 28, "Michigan": 25, "Illinois": 24, "Houston": 21}

# for team, score in rankings.items():
#     print(f"{team:10} ==> {score:10d}")

# print(round. __doc__)

# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))

# from datetime import date
# f1 = date(2014, 7, 4)
# print(f1)

# num1 = int(input("Enter your number here>> "))
# if num1 <= 17:
#     print(17-num1)
# else:
#     print((num1 - 17) * 2)

# list1 = [4, 6, 7, 4, 7, 5]
# n = 0
# for i in list1:
#     if i == 4:
#         n = n+1
#     else:
#         pass
# print(n)

# def concatenate_list(items_in_list):
#     result = ''
#     for i in items_in_list:
#         result += str(i)
#     return result
# print(concatenate_list([12, 30, 40, 50]))

# i = 30
# print(type(i)())

# print("Input the value of x & y")
# x, y = map(int, input().split())
# print("The value of x & y are: ",x,y)

# def max_min(data):
#   l = data[0]
#   s = data[0]
#   for num in data:
#     if num> l:
#       l = num
#     elif num< s:
#         s = num
#   return l, s

# print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))

def stringRandomLetters():
    words = """Hay muchas variaciones de los pasajes de Lorem Ipsum disponibles, pero la mayoría 
    sufrió alteraciones en alguna manera, ya sea porque se le agregó humor, o palabras 
    aleatorias que no parecen ni un poco creíbles. Si vas a utilizar un pasaje de Lorem 
    Ipsum, necesitás estar seguro de que no hay nada avergonzante escondido en el medio 
    del texto. Todos los generadores de Lorem Ipsum que se encuentran en Internet tienden 
    a repetir trozos predefinidos cuando sea necesario, haciendo a este el único generador 
    verdadero (válido) en la Internet. Usa un diccionario de mas de 200 palabras provenientes 
    del latín, combinadas con estructuras muy útiles de sentencias, para generar texto de Lorem 
    Ipsum que parezca razonable. Este Lorem Ipsum generado siempre estará libre de repeticiones, 
    humor agregado o palabra"""

    me_list = words.split()
    print(me_list)
    count_word = me_list.count("e")
    print(count_word)
    # me = (2+0)%9
    # print(me) 
    # while my_list:
    #     print(my_list[2])
    #     my_list.pop(2)
    #     print(my_list)
    # for i in my_list:
    #     print(i)

# def remove_nums(int_list):
#   #list starts with 0 index
#     position = 2
#     idx = 0
#     len_list = (len(int_list))
#     while len_list>0:
#         idx = (position+idx)%len_list
#         print(int_list.pop(idx))
#         len_list -= 1
# nums = [10,20,30,40,50,60,70,80,90]
# remove_nums(nums)

# stringRandomLetters()
    
def median():
    group_of_numbers = ['z', 'y']
    group_of_numbers2 = ['a', 'b', 'c', 'd', 'e', 'f']
    # the_list = []
    # for x in group_of_numbers:
    #     for y in group_of_numbers2:
    #         me = x+y
    #         print(me)
    #         us = the_list.append(me)
    #         print(us)
    # group_of_numbers.sort()
    # print(group_of_numbers[round(len(group_of_numbers)/2)])
    # Arrange the group of numbers in ascending order
median()


# def letter_combinations():
    # digits = "47"

    # if digits == "":
    #     return []
    # string_maps = {
    #     "1": "abc",
    #     "2": "def",
    #     "3": "ghi",
    #     "4": "jkl",
    #     "5": "mno",
    #     "6": "pqrs",
    #     "7": "tuv",
    #     "8": "wxy",
    #     "9": "z"
    # }
    
    # a = int(input('Please enter an integer:\n'))
    # b = int(input('Please enter another integer:\n'))

    # print(f'{a} in binary is {str(bin(a))[2:]}')
    # print(f'{b} in binary is {str(bin(b))[2:]}')
    # print(f'Binary AND of {a} and {b} is {a&b}')


    # result = [""]
    # for num in digits:
    #     temp = []
    #     for an in result:
    #         for char in string_maps[num]:
    #             temp.append(an + char)
    #     result = temp
    # return result
        
        
# letter_combinations()
# digit_string = "29"
# print(letter_combinations(digit_string))

