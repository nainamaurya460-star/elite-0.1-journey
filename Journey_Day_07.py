 # DAY 7   
# PRACTICE SET
# Write a program to print multiplication table of a given number using for loop.
n=int(input("enter a number: "))
 
for i in range(1,11):
    print(f"{n} x {i} ={n*i}")
# Write a program to greet all the person names stored in a list 'l' and which starts with S.
l=["Harry","Soham","Sachin","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello{name}")
#  Attempt problem 1 using while loop.
n= int(input("enter a number: "))
i=1
while(i<11):
    print(f"{n}x{i}={n*i}")
    i+=1
# Write a program to find whether a given number is prime or not.
n= int(input("enter a number: "))
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
else:
    print("number is prime")
# Write a program to find the sum of first n natural numbers using while loop
n= int(input("enter a number: "))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1

print(sum)
# Write a program to calculate the factorial of a given number using for loop.
n = int(input("Enter a number: "))
# 5!=1x2x3x4x5
for i in range (1,n+1):
    product=product*1
print(f" the factorial of {n} is {product} ")
# Write a program to print the following star pattern for n = 3.
'''
*
***
*****'''
n= int(input("enter a number: "))
for i in range(1,n+1):
 print(" "*(n-i),end="")
 print("*"* (2*i-1), end="")
 print("\n")
# Write a program to print the following star pattern for n = 3.

# *
# **
# ***
n= int(input("enter a number: "))
for i in range(1,n+1):
 print(" "*(n-i),end="")
 print("*"* i, end="")
 print("\n")
#  Write a program to print the following star pattern for n = 3.
# ***
# * *
# ***
n= int(input("enter a number: "))
for i in range(1,n+1):
   if(i==1 or i==n):
      print("*"* n)
else:
      print("*", end="")
      print(" "* (n-2), end="")
      print("*", end="")  
print("")
# Write a program to print multiplication table of n using for loops in reversed order.
n= int(input("enter a number: "))
for  i in range(1,11):
    print(f"{n}x{11-i}={n*(11-i)}")
