'''print("Hello world")
# print("naina")
"""so thanks that was my program 
"""
# practice set 1
# write a program to print twinkle twinkle little star poen in pythom
print(" twinkle twinkle little star /n how i wonder what you are/n up above the world so hogh/n like the diamond in the star")


import numpy_financial as npf
print(npf.fv(0.10, 5, 0, -10000))
# Input taking concept
age=int(input("enter your age: "))
if(age>=18):
    print("you have right to vote")
else:
    print("not right")
marks=float(input("Enter your marks :"))
if(marks>=90):
    print("Grade :'A'")
elif(marks>=80):
    print("Grade:'B'")
elif(marks>=70):
    print("Grade:'C'")
else:
    print("poor performance")
 # day 2

  
# variable &data types

a=1
b=3
print(a+b)
name="creator"   
a= 2 # a is an integer
b=5.333 #b is a floating number
c= "creator" #c is string
e=None # e is none type of variable

# rules of variable
a =23
aaa=45
_a=56
# @simran=3
# variable can't start with number
# simr@n # invalid

# OPERATOR IN PYTHON
# 1 airthemetic operator
a=45
b=56
c=a+b
print(c)
#  assignment operator
a= 4-3
b=5
b+=3 #increment the value of b by 3 and then assign to b
# comparison operator # always returns true or false
d=5<4
print(d)
# logical operators
e = True or False
print(e)
#  truth tble of 'or'
# type casting & type function
a=23.
b=float(a)# here integer is converted into float
t=type(a)
c="creator"
t=type(c)
# input function
a=input("enter number 1")
b=input("enter number 2")
print("number a is: ", a)
print("number b is : ", b)
print("sum is", a+b)
#  PRACTICE SET 2
# write a program to add sum of two numbers
a= 5
b= 6
c=a+b
print(c)
# write a program to find the remainder when a number is divided by z
y=8
z=4
x=y%z
print(x)
# check the type of variable assigned using input() function
a= input("enter number 1: ")
t=type(a)
print(t)
#  use comparison operator to find out whwther a given number is greater than 'b' or not . Take a=34 and b=80
a=34
b=80
c=a>b 
c = True or False
#  write a program to find an average of two numbers entered by the user 
a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
average = (a+b)/2
print(average)
# write a python code to calculate the square of a number entered by the user
a= int(input("enter  any number : "))
square=a*a
print(square)'''
# DAY3
# String
# name="creator" 
# a='crator'
# b='''creator'''
# nameshort= len(name)
#nameshort=name[0:3] #start from index 0 all the wat till 3 (excluding 3)
# print(nameshort)
# print(name[0:3])
# print(name[-4:-1])
# slicing technique
#print(name[0:4]) # is same as print(name[0:4])
#print(name[1:])#is same as print(name[1:0]) 
#print(name[1:5])
# function
#name="creator"
# print(len(name))
# print(name.endswith("tor"))
# print(name.startswith("cr"))

# escape sequence character
# a= "Reena is a good girl\nbut not\t a bad \"girl\""
# print(a)
# PRACTICE SET 3
# write a python program to display user entered name followed by good afternoon using input function
# name = input("enter your name: ")
# print("Good Afternoon ,(name)")
# write a program to fill in a letter template given below with name and date 
# letter='''
# Dear<|Name|>
# You are selected!
# <|Date|>
# '''
# '''letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>

'''name_input = input("Enter Name: ")
date_input = input("Enter Date: ")
letter = letter.replace("<|Name|>", name_input)
letter = letter.replace("<|Date|>", date_input)

print(letter)
# write a program to detect double space in string
sentence= "Reena is very beautiful   girl"
print(sentence.find("  "))
# replace the double space from problem 3 with single space
sentence= "Reena is very beautiful girl"
print(sentence.find(" "))
# wtite a program to format the following letter using escape sequence characters. letter= "Dear creator, this pyhton course is nice. Thanks!"
Letter="Dear Creator,\nthis python course is nice.\nThanks!"
print(Letter)'''
# DAY 4
# list
# friends= ["Apple","Orange",5, 345.55,False,"Akash","Rohan"]
# print(friends)
# friends.append("Creator")
# print(friends)
# practice set 
# Write a program to store seven fruits in a list entered by the user.
# fruit1= input("enter fruit1 name: ")
# fruit2=input("enter fruit2 name: ")
# fruit3=input("enter fruit3 name: ")
# fruit4=input("enter fruit4 name: ")
# fruit5= input("enter fruit5 name: ")
# fruit6=input("enter fruit6 name: ")
# fruit7=input("enter fruit7 name: ")
# fruits_list= [fruit1, fruit2,fruit3,fruit4,fruit5,fruit6,fruit7]
# print("fruit list is :", fruits_list)
# Write a program to accept marks of 6 students and display them in a sorted manner.
# marks1=int(input("enter marks for student1 : "))
# marks2=int(input("enter marks for student2 : "))
# marks3=int(input("enter marks for student3 : "))
# marks4=int(input("enter marks for student4 : "))
# marks5=int(input("enter marks for student5 : "))
# marks6=int(input("enter marks for student6 : "))
# marks_list=[marks1,marks2,marks3,marks4,marks5,marks6]
# marks_list.sort()
# print("Sorted marks:, marks_list")
# Check that a type cannot be changed in Python
# my_tuple=(20,40,60)
# my_tuple=99
# Write a program to sum a list with 4 numbers
# numbers= 7,8,9,3
# total_sum=sum(numbers)
# print("sum of the list is:",total_sum)
# Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
# a=(7,0,8,0,0,9)
# zero_count=a.count(0)
# print("the number of zeros in the tuple is:", zero_count)
# day 5
# sets & dictionary
# d={} #empty dictionary
# marks= {
#     "creator": 100,
#     "Neha":56,
#     "Rohan":23

# }

# marks=[["creator",100]]

# print(marks,type(marks))
# print(marks["creator"])
# methods
# marks= {
#     "creator": 100,
#     "Neha":56,
#     "Rohan":23,
#      0:"creator"
# }
# print(marks.keys())
# print(marks.values())
# marks.update({"creator":99,"renuka":88})
# print(marks)
# print(marks.get("creator2")) # returns none
# print(marks["creator2"]) # returns error
# SETS
# e = set() # empty set dont use s={} as it will create an empty dictionary

# s= {1,45,56,89,67,89,"creator"}
# print(s, type(s))
# s.add(566)
# print(s,type(s))
# operation on sets
# len(s)
# s.remove(1)
# print(s,type(s))
# s.clear(s)
# print(s,type(s))
# s1={1,45,6}
# s2={7,8,1,7}
# print(s1.union(s2))
# print(s1.intersection(s2))
# practice set
# write a program to create a dictionary of hindi words with valaues as their english translation. provide user with an option to look it up!
# words={ 
#     "madad":"help",
#     "kursi":"chair",
#     "billi":"cat",
# }
# word = input("enter the word you want meaning of: ")
# print(words(word))
# write a program to input eight numbers from the user and display all the unique numbers (once)
# n=input("enter number :")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# n=input("enter number : ")
# s.add(int(n))
# can we have set with18 (int) and  '18'(string) as a value in it?
# s= set()
# s.add(18)
# s.add("18")
# print(s)
#  what will be lenght of following as 
# s= set()
# s.add(20)
# s.add(20.0)
# s.add('20') # lenght of s after these operations?
# print( len(s))
# s={} #whtabis the type of's'
# print(type(s))
 # it is an emptty dictionary
#  create an empty dictionary .allow 4 friends to enter their favourite language as valie and use key as their names. assume that the names are unique
# d={}
# name= input("enter friends name: ")
# lang= input("enter language name: ")
# d.update({name: lang})
# name= input("enter friends name: ")
# lang= input("enter language name: ")
# d.update({name: lang})
# name= input("enter friends name: ")
# lang= input("enter language name: ")
# d.update({name: lang})
# name= input("enter friends name: ")
# lang= input("enter language name: ")
# d.update({name: lang})
# print(d)
#  if the names of 2 friends are same ; what will happen to the program in problem 6?
#  if languages of two friends are same;whta will happen to the program in problem 6?
#  nothig will be happen values will be same

# can you change the value inside a list which is contained in set s? 
# s= {8,7,12,"creator",[1,2]}
# we can not include list in any set
#  DAY6
#  conditional expression
# a = int(input("enter your age: "))
# IF elif else  ladder
# if(a>18):
#     print("you are above the age of consent")
#     print("Good for you")
# elif(a<0):
#     print("you are entering an invalid age")
# elif(a==0):
#     print("you are netring 0 which is not valid")
# else:
#     print("you are below the age of consent")
  
# print("end of program")
# if else statement
# if(a>18):
#     print("you are above the age of consent ")
# else:
#     print("you are below the age of consent")
# RELATIONAL OPERATORS/ Comparison operator
#  multiple if statement
#  if statement no 1
# if(a%2 == 0):
    # print("a is even")

# end of staement no 1 
# if statement no 2
# if(a>18):
#     print("you are above the age of consent")
#     print("Good for you")
# elif(a<0):
#     print("you are entering an invalid age")
# elif(a==0):
#     print("you are netring 0 which is not valid")
# else:
#     print("you are below the age of consent")
#  end of statement no 2 
# print("end of program")
#  PRACTICE SET
#  write a program to find the greates of four numbers entered by the user.
# a1=int(input("enter number1: "))
# a2=int(input("enter number2: "))
# a3=int(input("enter number3: "))
# a4=int(input("enter number4: "))
# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1:", a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2:", a2)
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greatest number is a3:", a3)
# else:
#     print("Greatest number is a4:",a4) 
# write a program to find out whether a student has passed or failed if it requires a total of 40% at least 33% in each subject to pass. assume 3 subjects and take marks as an input from the user
# m1=int(input("Enter marks of sub1: "))
# m2=int(input("Enter marks of sub2: "))
# m3=int(input("Enter marks of sub3: "))
# check for total percentage
# total_percentage = (100*(m1+m2+m3))/300
# if(total_percentage>= 40 and m1>=33 and m2>=33 and m3>=33):
#     print("You are pass")

# else:
#     print("You are failed, try again next year!") 
# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
# comment = input("Enter your comment text: ")
# comment = comment.lower()
# if("make a lot of money " in comment) or ("buy now" in comment) or ("subscribe this"in comment) or ("click this" in comment):
#     print("Alert: This comment is SPAM!")
# else:
#     print("Safe: This comment is NOT spam.")

#  Write a program to find whether a given username contains less than 10 characters or not.
# username=input("Enter your username: ")
# if len(username)<10:
#     print("The username has less than 10 characters")  
# else:
#     print("The username has 10 or more characters")  
# Write a program which finds out whether a given name is present in a list or not.
# names_list = ["rahul","reena","priya","amit","sneha"]
# search_name = input("Enter a name to search: ")
# search_name= search_name.lower()
# if search_name in names_list:
#     print("Yes, the name is present in the list")
# else:
    # print("No, the name is not in the list") 
# Write a program to calculate the grade of a student from his marks from the following scheme:

# 90 - 100 => Ex

# 80 - 90 => A

# 70 - 80 => B

# 60 - 70 => C

# 50 - 60 => D

# <50 => F      
# marks = float(input("Enter student's marks: "))
# if marks>= 90 and marks<=100:
#     grade= "Ex"
# elif marks>=80 and marks< 90:
#     grade ="A"
# elif marks>= 70 and marks<80:
#     grade="B"
# elif marks>= 60 and marks<70:
#     grade="C"
# elif marks>=50 and marks<60:
#     grade="D"
# elif marks<50 and marks >= 0:
#     grade="F"
# else:
#     grade="Invalid Marks Entered!"  
# print("The final grade is:", grade)
# Write a program to find out whether a given post is talking about "Harry" or not.
# post=input("Enter the post text: ")
# if "harry" in post.lower():
#     print("Yes , this post is talking about harry")
# else:
#     print("No, this post does not mention harry")
# DAY 7   
# PRACTICE SET
# Write a program to print multiplication table of a given number using for loop.
# n=int(input("enter a number: "))
 
# for i in range(1,11):
#     print(f"{n} x {i} ={n*i}")
# Write a program to greet all the person names stored in a list 'l' and which starts with S.
# l=["Harry","Soham","Sachin","Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello{name}")
#  Attempt problem 1 using while loop.
# n= int(input("enter a number: "))
# i=1
# while(i<11):
#     print(f"{n}x{i}={n*i}")
#     i+=1
# Write a program to find whether a given number is prime or not.
# n= int(input("enter a number: "))
# for i in range(2,n):
#     if(n%i)==0:
#         print("number is not prime")
#         break
# else:
    # print("number is prime")
# Write a program to find the sum of first n natural numbers using while loop
# n= int(input("enter a number: "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1

# print(sum)
# Write a program to calculate the factorial of a given number using for loop.
# n = int(input("Enter a number: "))
# 5!=1x2x3x4x5
# for i in range (1,n+1):
#     product=product*1
# print(f" the factorial of {n} is {product} ")
# Write a program to print the following star pattern for n = 3.
'''
*
***
*****'''
# n= int(input("enter a number: "))
# for i in range(1,n+1):
#  print(" "*(n-i),end="")
#  print("*"* (2*i-1), end="")
#  print("\n")
# Write a program to print the following star pattern for n = 3.

# *
# **
# ***
# n= int(input("enter a number: "))
# for i in range(1,n+1):
#  print(" "*(n-i),end="")
#  print("*"* i, end="")
#  print("\n")
#  Write a program to print the following star pattern for n = 3.
# ***
# * *
# ***
# n= int(input("enter a number: "))
# for i in range(1,n+1):
#    if(i==1 or i==n):
#       print("*"* n)
# else:
#       print("*", end="")
#       print(" "* (n-2), end="")
#       print("*", end="")  
# print("")
# Write a program to print multiplication table of n using for loops in reversed order.
# n= int(input("enter a number: "))
# for  i in range(1,11):
#     print(f"{n}x{11-i}={n*(11-i)}")
# Day 9
# project
'''
1 for snake
-1 for water
0 for gun


'''
'''import random




computer = random.choice([-1,0,1])
youstr = input("Enter your choice(1 for snake , -1 for water,0 for gun): ")
youDict ={"1": 1, "-1": -1, "0": 0}
reverseDict={1:"snake", -1:"water", 0:"gun"}
you=youDict[youstr]
print(f"you choose{reverseDict[you]}\ncomputer choose{reverseDict[computer]}")

if(computer==you):
    print("Its draw")
if(computer == -1 and you==1):
    print("You win!")
elif(computer == -1 and you ==0):
    print("You lose!")
elif(computer == 1 and you==-1):
    print("You lose!")
elif(computer ==1 and you==0):
    print("You win!")
elif(computer == 0 and you==-1):
    print("You win!")
elif(computer ==0 and you==1):
    print("You lose!")
else:
    print("Something wrong")'''
# day 10
# OOP(OBJECT ORIENTED PROGRAM)
# example: data of a student
'''class Student:
    def __init__(self , name,branch):
        self.name=name
        self.branch = branch
        
    def introduce(self):
        print(f"Hi, mera naam {self.name} hai aur meri branch {self.branch} hai.")
    

student1=Student("Naina","CS(AI&ML)")
student2=Student("Rohan","ME")

student1.introduce()
student2.introduce()'''
# bank account data
'''class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def check_balance(self):
        print(f"{self.owner} ka current balance: {self.balance} Rs")
    def deposit(self,amount):
        self.balance = self.balance +amount
        print(f"{amount} Rs deposit ho gyr!")
ccount = BankAccount("Amit",50000)

ccount.check_balance()
ccount.deposit(22000)
ccount.check_balance()'''
# day11
# phone brand 
'''class Phone:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.is_charged = False
    def charge_phone(self):
        self.is_charged = True
        print(f"{self.brand} {self.model} ab full charge hai!")
my_phone=Phone("Apple","iphone 15") 
print(my_phone.is_charged) 

my_phone.charge_phone()
print(my_phone.is_charged)
'''
'''class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def show_details(self):
        print(f"book ka title { self.title} unique  title hai and {self.author} Great  author hai")
my_book = Book("travelling","Robert hook" )
my_book.show_details()           
        '''
'''class Calculator:
    def __init__(self, a,b ):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def multiply(self):
        return self.a*self.b
my_calc=Calculator(34,67)
print(f"Rhe addition is : {my_calc.add()}")
print(f"The multiplication is: {my_calc.multiply()}")    
'''
# day 13
# practice from basic to advance
# swapping concept
'''a=10
b=20
temp=a
a=b
b=temp
print(b)
print(a)'''
# Type Caster
'''a=int(input("Enter your age: "))
new_age= a+5
print("After five year your age will become:", {new_age})
'''
# if else condition
'''year=int(input("Enter any year: "))
if(year%4== 0 and year%100!=0) or (year%400==0):
    print("year is leap year")
else:
    print("year is not leap year")'''
# ticket pricing
'''age=int(input("Enter your age: "))
if(age<=5):
    print("there is no ticket rule at this age")
elif(5<=age<=18):
    print("Ticket price is 100 rupees")
else:
    print("ticket price is 200 rupees")'''

# loops 
# table of any number
'''num= int(input("Enter any number for table: "))
for i in range(1,11):
    result=num*i
    print(f"{num}x {i} = {result}")'''

# odd number
'''
print("__odd numbers from 1 to 20__")
i=1
while i<=20:
    print(i)
    i=i+2'''
# DAY 15
# Object oriented program
'''class Employee:
    # name="creator"
    language="Py" #this is class attribute
    salary=10000000


creator=Employee() 
creator.name = "Creator"
print(creator.name,creator.language)

rohan = Employee()
rohan.name="Rohan"# this is an object attribut/instance attribute
print(rohan.salary,rohan.language)
# Here name is object attribute and salary and language are class attribute as they directly belong to the class
# instance vs class attribute

class Employee:
    
    language="Py" #this is class attribute
    salary=10000000


creator=Employee()
creator.language="javascript" #this is an instance attribute

print(creator.language,creator.salary)

rohan = Employee()
rohan.name="Rohan"# this is an object attribut/instance attribute
print(rohan.salary,rohan.language)
# self parameter
class Employee:
    
    language="Py" #this is class attribute
    salary=10000000
    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")
    @staticmethod   
    def Greet(self):
        print("Good morning")
creator=Employee()
# creator.language="javascript" #this is an instance attribute
creator.getInfo()
creator.Greet()
# Employee.getInfo(creator)
# __INIT__{} CONSTRUCTOR

class Employee:
    
    language="Py" #this is class attribute
    salary=10000000

    def __init__(self,name,salary,language):
         #dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. the salary is {self.salary}")


    @staticmethod   
    def Greet(self):
        print("Good morning")


creator = Employee("Creator",2000000,"Javascript")
# creator=Employee()
# creator.name="creator"
print(creator.name,creator.salary,creator.language)
'''
# Practice set
# question 1
'''class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode

p=Programmer("creator",1000000,209856)
print(p.name,p.salary,p.company,p.pincode) 
 
#  question 2
class Claculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

    
a=Claculator(4)
a.square() 
a.cube()
a.squareroot()
# question 3
class Demo:
    a=4
o=Demo()
print(o.a) # prints the class attribute becuase instance attribute is not present
o.a=0 # instance attribute is set
print(o.a) #prints the instance attribute because instance attribute is present
print(Demo.a) #prints the class attribute

# question 4
class Claculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
@staticmethod
def hello():
    print("Hello There!")
    
a=Claculator(4)
a.square() 
a.cube()
a.squareroot()
# a.hello()
# question 5
from random import randint
class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def book(self,fro,to):

        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    def getstatus(self,):
        print(f"Train no: {self.trainNo} is running on time")
    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
t=Train(23453)
t.book("Ayodhya","Varanasi")
t.getstatus()
t.getFare("Ayodhya","Varanasi") 
#   question 6
from random import randint
class Train:

    def __init__(slf,trainNo):
        slf.trainNo=trainNo
        
    def book(slf,fro,to):

        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
    def getstatus(slf,):
        print(f"Train no: {slf.trainNo} is running on time")
    def getFare(slf,fro,to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222,5555)}")
t=Train(23453)
t.book("Ayodhya","Varanasi")
t.getstatus()
t.getFare("Ayodhya","Varanasi")
# day 16
# INHERITANCE
class Employee:
    company="ITC"
    def shoe(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")

# class Programmer:
#     company="ITC infotech"
#     def show(self):
#         print(f"the name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good in {self.language} language")
class Programmer(Employee):
   company="ITC Infotech" 
   def showLanguage(self):
       print(f"Te name is {self.name} and he is good with {self.Lamguage}")
a=Employee()    
b=Programmer()

print(a.company,b.company)
# multiple inheritence
class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")

class Coder:
    language="python"
    def printLanguages(self):
        print(f"Out of all languages here is your language: {self.language}")





class Programmer(Employee,Coder):
   company="ITC Infotech" 
   def showLanguage(self):
       print(f"The name is {self.company} and he is good with {self.language}")
a=Employee()    
b=Programmer()
b.showLanguage()
b.showLanguage()'''
# multilevel inheritence
'''class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=4
o=Employee()
print(o.a) # prints the a attribute
# print(o.b) # shows an error as there is no attribute in employee class

o=Programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)'''
# super.py
'''class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        
        print("Constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c=4
# o=Employee()
# print(o.a) 

# o=Programmer()
# print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)
# Class Mehods
class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class value a is {cls.a}")
e=Employee()
e.a=45
e.show()
# property decorators
class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class value a is {cls.a}")
    @property
    def name(self):
        return "{self.fname}"
    

    @name.setter
    def name (self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=Employee()
e.a=45
e.name="creator singhaniya"
print(e.fname,e.lname)
e.show()
# operator overloading
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self, num):
        return self.n+num.n


n=Number(1)
m=Number(2)
print(n+m)'''
# practice set
# question 1
'''class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j +{self.k}k")

a=TwoDVector(1,2)
a.show()
b=ThreeDVector(1,2,3)
b.show()
# question 2
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")


d=Dog()
d.bark()
# question 3
class Employee:
    salary = 234
    increment=20
    @property
    def salaryAfterIncrement(self):
        return (self.salary+self.salary*(self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterincrement(self,salary):
        self.increment = ((salary/self. salary)-1)*100
e=Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterincrement = 280
print(e.increment)
# question 4
class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return Complex(self.r +c2.r, self.i +c2.i)
    
    def __mul__(self, c2):
        real_part =self.r*c2.r-self.i*c2.i
        imag_part =self.r *c2.i+self.i*c2.r
        return Complex(real_part,imag_part)
    
    def __str__(self):
        return f"{self.r} +{self.i}i"
    

c1=Complex(1,3)
c2=Complex(5,6)
print(c1+c2)
print(c1*c2)

# question 5
class Vector:
    def __init__(self ,x,y,z):
        self.x=x
        self.y=y
        self.z=z

def __add__(self,other):
    result= Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    return result

def __mul__(self,other):
    result = self.x*other.x+self.y*other.y+self.z*other.z
    return result

def __str__(self):
    return f"Vector({self.x}+{self.y}+{self.z})"
#  Test the implementation
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)

print(v1+v2)
print(v1*v2)

print(v1 + v3)
print(v1*v3)

# question 6
class Vector:
    def __init__(self ,x,y,z):
        self.x=x
        self.y=y
        self.z=z

def __add__(self,other):
    result= Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    return result

def __mul__(self,other):
    result = self.x*other.x+self.y*other.y+self.z*other.z
    return result

def __str__(self):
    return f"{self.x}i,{self.y}j,{self.z}k"
#  Test the implementation
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)

print(v1 + v2)
print(v1*v2)

print(v1 + v3)
print(v1*v3)
# Question 7
class Vector:
    def __init__(self ,l):
        self.l


def __len__(self):
    return len(self.l)
#  Test the implementation
v1=Vector(1,2,3)
print(len(v1))'''
"""# PROJECT 2= THE PERFECT GUESS
import random
n= random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses += 1
    a=int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1
print(f"You have guesed the number {n} correctly in {guesses} attempts")
# NEWLY ADDED FEAATURES IN PYTHON
#  using Wlarus operator
if (n:= len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n}) elements, expected <=3 ") # ouput list is too long (5 element, expected<=3)

# TYPE DEFINITIONS

from typing import List,Union,Tuple
n : int = 5
name: str ="creator"

def sum(a: int,b: int) -> int:
    return a+b

# Match case
def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "Internal Server Error"
        case _:
            "Unknown status" #usage print(http_status(200)) #output : ok
           # print(http_status (404)) #output: not found print(http_status(500)) # output:internal server

# Dictionary merge & update operators
# exception handling

try:
  a= int(input("Hey , Enter a number: "))
  print(a)

except ValueError as v:
    print("heyyy")
    print(v)
except Exception as e:
  print(e)

print("Thankyou")


# Raising exception
a=int(input("enter a number: "))
b=int(input("enter a number: "))
if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"the division a/b is {a/b}")

print(f"The division a/b is {a/b}")

# try with else & finally
a=int(input("enter a number: "))
b=int(input("enter a number: "))
if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"the division a/b is {a/b}")

print(f"The division a/b is {a/b}")"""
# try_finally
def main():
 try:
  a= int(input("Hey , Enter a number: "))
  print(a)
  return

 except Exception as e:
    print(e)
    return

 finally:
    print("Hey I am inside of finally")    

main()
# main
def myFunc():
   print("hello world")

myFunc()
print(__name__)

# ek new file banani padegi main.py then usme code myfunc ka then module.py file bnakar import karenge


# from module import myFunc
if __name__=="__main__":
#   if this code is directly executed by runnig the files its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)


# global

a=89
def fun():
   #golbal a
   a=3
   print(a)

fun() 
print(a)

# Enumerate 
index=0
l=[3,53,53,535]
for item  in l:
   print(f"the item number {index} is {item}") 
   index+=1 

#this can be simplified using enumerate function

for item in enumerate(l):
   print(f"the item number {index} is {item}") 

#  list compherension
myList =[1,2,9,5,3,5] 
# squaredList = []
# for item in myList:
#    squaredList.append(item*item)
squaredList=[i*i for i in myList] 

print(squaredList)
# chapter 12 practice set






       










        
        


    

















       


