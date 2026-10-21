#  PRACTICE SET
#  write a program to find the greates of four numbers entered by the user.
a1=int(input("enter number1: "))
a2=int(input("enter number2: "))
a3=int(input("enter number3: "))
a4=int(input("enter number4: "))
if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)
else:
    print("Greatest number is a4:",a4) 
# write a program to find out whether a student has passed or failed if it requires a total of 40% at least 33% in each subject to pass. assume 3 subjects and take marks as an input from the user
m1=int(input("Enter marks of sub1: "))
m2=int(input("Enter marks of sub2: "))
m3=int(input("Enter marks of sub3: "))
# check for total percentage
total_percentage = (100*(m1+m2+m3))/300
if(total_percentage>= 40 and m1>=33 and m2>=33 and m3>=33):
    print("You are pass")

else:
    print("You are failed, try again next year!") 
# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
comment = input("Enter your comment text: ")
comment = comment.lower()
if("make a lot of money " in comment) or ("buy now" in comment) or ("subscribe this"in comment) or ("click this" in comment):
    print("Alert: This comment is SPAM!")
else:
    print("Safe: This comment is NOT spam.")

#  Write a program to find whether a given username contains less than 10 characters or not.
username=input("Enter your username: ")
if len(username)<10:
    print("The username has less than 10 characters")  
else:
    print("The username has 10 or more characters")  
# Write a program which finds out whether a given name is present in a list or not.
names_list = ["rahul","reena","priya","amit","sneha"]
search_name = input("Enter a name to search: ")
search_name= search_name.lower()
if search_name in names_list:
    print("Yes, the name is present in the list")
else:
    print("No, the name is not in the list") 
# Write a program to calculate the grade of a student from his marks from the following scheme:

# 90 - 100 => Ex

# 80 - 90 => A

# 70 - 80 => B

# 60 - 70 => C

# 50 - 60 => D

# <50 => F      
marks = float(input("Enter student's marks: "))
if marks>= 90 and marks<=100:
    grade= "Ex"
elif marks>=80 and marks< 90:
    grade ="A"
elif marks>= 70 and marks<80:
    grade="B"
elif marks>= 60 and marks<70:
    grade="C"
elif marks>=50 and marks<60:
    grade="D"
elif marks<50 and marks >= 0:
    grade="F"
else:
    grade="Invalid Marks Entered!"  
print("The final grade is:", grade)
# Write a program to find out whether a given post is talking about "Harry" or not.
post=input("Enter the post text: ")
if "harry" in post.lower():
    print("Yes , this post is talking about harry")
else:
    print("No, this post does not mention harry")   
