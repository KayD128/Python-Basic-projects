import mysql.connector as sql

# mycursor.execute("CREATE DATABASE cbt_exam")
# mycursor.execute("CREATE TABLE student_table(ctm_id INT(3), Full_Name VARCHAR(30), Level VARCHAR(3), Matric_Number VARCHAR(9))")
# mycursor.execute("ALTER TABLE student_table CHANGE ctm_id students_id INT(3) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE student_dets ADD UNIQUE(Full_Name);")
# mycursor.execute("ALTER TABLE student_dets ADD UNIQUE(Matric_Number);")
# mycursor.execute("CREATE TABLE course_table(ctm_id INT(3), courses VARCHAR(30), number_of_questions INT(2))")
# mycursor.execute("CREATE TABLE result_table(ctm_id INT(3), student_id INT(3), math_score INT(3), english_score INT(3), general_score INT(3), total_score INT(3))")
# mycursor.execute("ALTER TABLE result_table CHANGE ctm_id result_id INT(3) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE course_table DROP course_id;")

import sys
# from numpy import random
# import time


class Exam:
    def __init__(self):
        self.mycursor = ""
        self.mycon = ""
        self.real_english_id = 0
        self.real_maths_id = 0
        self.real_gen_id = 0
        self.gen_score = 0
        self.eng_score = 0
        self.math_score = 0
        self.total_score = 0
        self.student_id = 0
        self.login()
        # self.registerHere()
        # self.mathQuestions()
        # self.englishQuestions()
        # self.generalQuestions()
        # self.opening()

    def connection(self):
        self.mycon = sql.connect(host = '127.0.0.1', user = 'root', passwd = '', database = "cbt_exam")
        self.mycursor = self.mycon.cursor()
        # self.mycursor.execute("ALTER TABLE results_table CHANGE ctm_id score_id INT(3) PRIMARY KEY AUTO_INCREMENT")
        # self.mycursor.execute("ALTER TABLE student_table ADD UNIQUE(Full_Name);")


        # self.mycursor.execute("ALTER TABLE results_table CHANGE student_id INT(3) FOREIGN KEY")
       
        # self.mycursor.execute("ALTER TABLE results_table ADD FOREIGN KEY (student_id) REFERENCES student_table(student_id)")
    
    def opening(self):
        self.connection()
        print("Welcome to the Exam hall.")
        reg_or_login = input("Enter 1 to Register or 2 to login to your exam page>> ")
        if reg_or_login == "1":
            self.registerHere()
        elif reg_or_login == "2":
            self.login()
        else:
            print("Error!!! Try again")
            self.opening()
    # self.opening()

    def registerHere(self):
        self.connection()
        register_student_name = input("Enter your Name here>> ")
        register_level = input("Enter your level here>> ")
        register_student_matric = input("Enter your matric number>> ")

        myquery = "INSERT INTO student_table(Full_Name, Level, Matric_Number) VALUES(%s, %s, %s)"
        value = (register_student_name, register_level, register_student_matric)
        self.mycursor.execute(myquery, value)
        self.mycon.commit()
        print(self.mycursor.rowcount, "registered successfully")
        self.mycon.close()

        loginOrRegister = input("Type 1 to register again/Type 2 to login/3 to exit the registration.>> ")

        if loginOrRegister.strip().lower() == "1":
            self.registerHere()
        elif loginOrRegister.strip().lower() == "2":
            self.login()
        elif loginOrRegister.strip().lower() == "3":
            sys.exit
        else:
            print("Error!!! Try again")
            self.registerHere()

    def login(self):
        self.connection()
        student_name = input("Enter your Name here>> ") 
        student_matric = input("Enter your matric number>> ")

        query = "SELECT student_id, Full_Name, Matric_Number FROM student_table WHERE Full_Name=%s AND Matric_Number=%s"
        sql = (student_name, student_matric)
        self.mycursor.execute(query, sql)
        myLogin = self.mycursor.fetchone()
        self.mycon.close()

        if myLogin:
            print("Welcome " + student_name + ", pick your course and answer the following questions")
            self.student_id = myLogin[0]
            # print(self.student_id)
            self.courses()
        else:
            print("Access Denied!")
            denied = input("Press 1 to try again/Press 2 to go to register")
            if denied == 1:
                self.login()     
            elif denied == 2:
                self.registerHere()

    def courses(self):
        self.connection()
        course = ["1. Mathematics", "2. English Language", "3. General Studies"]
        for cou in course:
            print(cou)
        course_picked = input("Type the exam you wish to enter>> ")
        if course_picked == "1":
            query = "SELECT course_id FROM course_table WHERE courses=\"Mathematics\""
            # sql = ()
            self.mycursor.execute(query)
            maths_id = self.mycursor.fetchone()
            self.mycon.close()
            self.real_maths_id = maths_id[0]
            # print(self.real_maths_id)

            self.mathQuestions()

        elif course_picked == "2":
            query = "SELECT course_id FROM course_table WHERE courses=\"English\""
            # sql = ()
            self.mycursor.execute(query, sql)
            english_id = self.mycursor.fetchone()
            self.mycon.close()
            self.real_english_id = english_id[0]

            self.englishQuestions()

        elif course_picked == "3":
            query = "SELECT course_id FROM course_table WHERE courses=\"General Studies\""
            # sql = ()
            self.mycursor.execute(query, sql)
            gen_id = self.mycursor.fetchone()
            self.mycon.close()
            self.real_gen_id = gen_id[0]

            self.generalQuestions()
        else:
            print("Invalid input")
            self.courses()

    def mathQuestions(self):
        self.connection()
        print("MATHEMATICS")
        print("Answer the following questions carefully")
        query = "SELECT Questions FROM question_table WHERE course_id=%s"
        val = (1, )
        self.mycursor.execute(query, val)
        first_questions = self.mycursor.fetchall()

        query = "SELECT Option_a FROM question_table WHERE course_id=%s"
        val = (1, )
        self.mycursor.execute(query, val)
        option_a = self.mycursor.fetchall()
        # print(option_a)

        query = "SELECT Option_b FROM question_table WHERE course_id=%s"
        val = (1, ) 
        self.mycursor.execute(query, val)
        option_b = self.mycursor.fetchall()

        query = "SELECT option_c FROM question_table WHERE course_id=%s"
        val = (1, ) 
        self.mycursor.execute(query, val)
        option_c = self.mycursor.fetchall()

        query = "SELECT correct_option FROM question_table WHERE course_id=%s"
        val = (1, ) 
        self.mycursor.execute(query, val)
        correct_option = self.mycursor.fetchall()        

        num1 = 0
        for mat in first_questions:
            print(mat[0])
            print(option_a[num1][0])
            print(option_b[num1][0])
            print(option_c[num1][0])
            my_answer = input("Enter your answer here>> ")
            if my_answer.strip().capitalize() == correct_option[num1][0]:
                self.math_score += 4
            else:
                pass
            num1 += 1
        print(self.math_score)

        myquery_1 = "INSERT INTO results_table(student_id, course_id, Scores) VALUES(%s,%s,%s)"
        value_1 = (self.student_id, self.real_maths_id, self.math_score)
        self.mycursor.execute(myquery_1, value_1)
        self.mycon.commit()
        self.mycon.close()
        # print(self.mycursor.rowcount, "registered successfully")
        
        print("Click on 1 to go back to the list of courses and answer another course if needed or another key to exit the exam")
        another_course = input("Enter Here>> ")
        if another_course == "1":
            self.courses()
        else:
            self.login()

        # sql = "DELETE FROM student_table WHERE Full_Name=%s"
        # val = ("Kolade Ogunleye", )
        # self.mycursor.execute(sql, val)
        # self.mycon.commit()
        # print(self.mycursor.rowcount, "registered successfully")

        # sql = "UPDATE student_table SET students_id = 3 WHERE Full_Name=%s"
        # val = ('Amarachi Chiamaka', )
        # self.mycursor.execute(sql, val)
        # self.mycon.commit()

    
    def englishQuestions(self):
        self.connection()

        # sql = "UPDATE question_table SET correct_option = %s WHERE Option_a=%s"
        # val = ('B','(A) 25', )
        # self.mycursor.execute(sql, val)
        # self.mycon.commit()
        print("ENGLISH LANGUAGE")
        print("Answer the following questions carefully")
        query = "SELECT Questions FROM question_table WHERE course_id=%s"
        val = (2, ) 
        self.mycursor.execute(query, val)
        second_questions = self.mycursor.fetchall()

        query = "SELECT Option_a FROM question_table WHERE course_id=%s"
        val = (2, ) 
        self.mycursor.execute(query, val)
        option_2a = self.mycursor.fetchall()

        query = "SELECT Option_b FROM question_table WHERE course_id=%s"
        val = (2, ) 
        self.mycursor.execute(query, val)
        option_2b = self.mycursor.fetchall()

        query = "SELECT option_c FROM question_table WHERE course_id=%s"
        val = (2, ) 
        self.mycursor.execute(query, val)
        option_2c = self.mycursor.fetchall()

        query = "SELECT correct_option FROM question_table WHERE course_id=%s"
        val = (2, ) 
        self.mycursor.execute(query, val)
        second_correct_option = self.mycursor.fetchall()     

        num2 = 0
        for eng in second_questions:
            print(eng[0])
            print(option_2a[num2][0])
            print(option_2b[num2][0])
            print(option_2c[num2][0])
            my_answer = input("Enter your answer here>> ")
            if my_answer.strip().capitalize() == second_correct_option[num2][0]:
                self.eng_score += 4
            else:
                pass
            num2 += 1
        print(self.eng_score)

        myquery_2 = "INSERT INTO results_table(student_id, course_id, Scores) VALUES(%s,%s,%s)"
        value_2 = (self.student_id, self.real_english_id, self.eng_score)
        self.mycursor.execute(myquery_2, value_2)
        self.mycon.commit()
        self.mycon.close()
        # print(self.mycursor.rowcount, "registered successfully")

        print("Click on 1 to go back to the list of courses and answer another course if needed or another key to exit the exam")
        another_course_2 = input("Enter Here>> ")
        if another_course_2 == "1":
            self.courses()
        else:
            self.login()

    def generalQuestions(self):
        self.connection()
        print("GENERAL STUDIES")
        print("Answer the following questions carefully")
        query = "SELECT Questions FROM question_table WHERE course_id=%s"
        val = (3, ) 
        self.mycursor.execute(query, val)
        third_questions = self.mycursor.fetchall()

        query = "SELECT Option_a FROM question_table WHERE course_id=%s"
        val = (3, ) 
        self.mycursor.execute(query, val)
        option_3a = self.mycursor.fetchall()
        # print(option_a)

        query = "SELECT Option_b FROM question_table WHERE course_id=%s"
        val = (3, ) 
        self.mycursor.execute(query, val)
        option_3b = self.mycursor.fetchall()

        query = "SELECT option_c FROM question_table WHERE course_id=%s"
        val = (3, ) 
        self.mycursor.execute(query, val)
        option_3c = self.mycursor.fetchall()

        query = "SELECT correct_option FROM question_table WHERE course_id=%s"
        val = (3, ) 
        self.mycursor.execute(query, val)
        third_correct_option = self.mycursor.fetchall()        

        num3 = 0
        for gen in third_questions:
            print(gen[0])
            print(option_3a[num3][0])
            print(option_3b[num3][0])
            print(option_3c[num3][0])
            my_answer = input("Enter your answer here>> ")
            if my_answer.strip().capitalize() == third_correct_option[num3][0]:
                self.gen_score += 4
            else:
                pass
            num3 += 1
        print(self.gen_score)

        myquery_3 = "INSERT INTO results_table(student_id, course_id, Scores) VALUES(%s,%s,%s)"
        value_3 = (self.student_id, self.real_gen_id, self.gen_score)
        self.mycursor.execute(myquery_3, value_3)
        self.mycon.commit()
        self.mycon.close()
        # print(self.mycursor.rowcount, "registered successfully")

        print("Click on 1 to go back to the list of courses and answer another course if needed or another key to exit the exam")
        another_course_3 = input("Enter Here>> ")
        if another_course_3 == "1":
            self.courses()
        else:
            self.login()

    # def total(self):
    #     self.connection()
    #     self.total_score = self.math_score + self.eng_score + self.gen_score
    #     print(self.student_id)

    #     myquery = "INSERT INTO result_table(student_id, math_score, english_score, general_score, total_score) VALUES(%s,%s,%s,%s,%s)"
    #     value = (self.student_id, self.math_score, self.eng_score, self.gen_score, self.total_score)
    #     self.mycursor.execute(myquery, value)
    #     self.mycon.commit()
    #     self.mycon.close()
    #     self.login()

Ex = Exam()


