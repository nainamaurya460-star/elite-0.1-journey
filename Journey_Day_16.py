# Object oriented program
class Employee:
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

# Practice set
# question 1
class Programmer:
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
