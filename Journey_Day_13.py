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
