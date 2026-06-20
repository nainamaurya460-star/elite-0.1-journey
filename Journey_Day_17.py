
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
b.showLanguage()
# multilevel inheritence
class Employee:
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
print(o.a,o.b,o.c)
# super.py
class Employee:
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
print(n+m)
# practice set
# question 1
class TwoDVector:
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
print(len(v1))
# PROJECT 2= THE PERFECT GUESS
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
