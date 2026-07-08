try:
    with open("1.txt", "r") as f:
     print(f.read())
except Exception as e:
   print(e)
try:
    with open("2.txt", "r") as f:
     print(f.read())
except Exception as e:
   print(e)
try:
    with open("3.txt", "r") as f:
     print(f.read())    
except Exception as e:
   print(e)


print("Thankyou!")
l=[1,2,3,4,5,6,7,8]

for i , item in enumerate(l):
    if i==2 or i==4 or i==6:
        print(item)
        # Hi I am 2.txt 
        n=5
table=[n*i for i in range (1,11)]
print(table)
try:
    a=int(input("Enter a: "))
    b= int(input("Enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")  
      n=5
table=[n*i for i in range (1,11)]
print(table)
with open("tables.txt", "w") as f:
    f.write(f" table of {n} {str(table)} + \n")
    # table of 5 [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] + 

        
