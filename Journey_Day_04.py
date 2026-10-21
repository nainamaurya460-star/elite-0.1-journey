# Question 1: Write a program to store seven fruits in a list entered by the user.
fruit1 = input("Enter fruit 1 name: ")
fruit2 = input("Enter fruit 2 name: ")
fruit3 = input("Enter fruit 3 name: ")
fruit4 = input("Enter fruit 4 name: ")
fruit5 = input("Enter fruit 5 name: ")
fruit6 = input("Enter fruit 6 name: ")
fruit7 = input("Enter fruit 7 name: ")

fruits_list = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
print("Fruit list is:", fruits_list)


# Question 2: Write a program to accept marks of 6 students and display them in a sorted manner.
marks1 = int(input("Enter marks for student 1: "))
marks2 = int(input("Enter marks for student 2: "))
marks3 = int(input("Enter marks for student 3: "))
marks4 = int(input("Enter marks for student 4: "))
marks5 = int(input("Enter marks for student 5: "))
marks6 = int(input("Enter marks for student 6: "))

marks_list = [marks1, marks2, marks3, marks4, marks5, marks6]
marks_list.sort()
print("Sorted marks:", marks_list)


# Question 3: Check that a type cannot be changed in Python (Tuple Immutability)
my_tuple = (20, 40, 60)
# The following line will deliberately throw a TypeError because tuples are immutable
my_tuple = 99 


# Question 4: Write a program to sum a list with 4 numbers.
numbers =
total_sum = sum(numbers)
print("The sum of the list is:", total_sum)


# Question 5: Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)
zero_count = a.count(0)
print("The number of zeros in the tuple is:", zero_count)
