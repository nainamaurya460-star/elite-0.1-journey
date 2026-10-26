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

print(f"The division a/b is {a/b}")
