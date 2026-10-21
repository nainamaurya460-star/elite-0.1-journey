 # enter value to perform any operation
num1=int(input("Enter your number: "))
num2=int(input("Enter your number: "))
# choose opration
operator=input("Enter any operator('+','-','/','*','%'): ")
if(operator == '+'):
    print(f"result: {num1}+{num2}={num1+num2}")
elif(operator=='-'):
    print(f"result: {num1}-{num2}={num1-num2}")
elif(operator=='/'):
    print(f"result: {num1}/{num2}={num1/num2}")
elif(operator=='*'):
    print(f"result: {num1}*{num2}={num1*num2}")
elif(operator=='%'):
    print(f"result:{num1}%{num2}={num1%num2}")
else:
    print("somthing went wrong! \n Try again")
#  by using eval() function
num1 = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /, %): ").strip()
num2 = input("Enter second number: ")

# Kuch operators check kar lete hain security ke liye
if operator in ['+', '-', '*', '/', '%']:
    # eval() automatically basic math calculation kar dega
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    print(f"Result: {expression} = {result}")
else:
    print("Invalid Operator!")
