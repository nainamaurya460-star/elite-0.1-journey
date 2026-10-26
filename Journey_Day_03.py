# DAY 3 - Python Strings

## 1. Basics & Slicing Techniques
```python
# String Definitions
name = "creator" 
a = 'crator'
b = '''creator'''

# String Slicing
# Start from index 0 all the way till 3 (excluding 3)
nameshort = name[0:3] 
print(nameshort)
print(name[0:3])

# Slicing with negative indices
print(name[-4:-1])

# Slicing techniques examples
print(name[0:4]) # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:7]) 
print(name[1:5])
name = "creator"
# string function
print(len(name))
print(name.endswith("tor"))
print(name.startswith("cr"))
#  escape sequence characters
a = "Reena is a good girl\nbut not\t a bad \"girl\""
print(a)
# PRACTICE SET
# Write a python program to display user entered name followed by good afternoon using input function
name = input("enter your name: ")
print(f"Good Afternoon, {name}")
# Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name_input = input("Enter Name: ")
date_input = input("Enter Date: ")

letter = letter.replace("<|Name|>", name_input)
letter = letter.replace("<|Date|>", date_input)

print(letter)
# Write a program to detect double space in string.
sentence = "Reena is very beautiful   girl"
print(sentence.find("  "))
# Replace the double space from problem 3 with single space.
sentence = "Reena is very beautiful  girl"
# Replacing double space with single space and printing
print(sentence.replace("  ", " "))
# Write a program to format the following letter using escape sequence characters. letter = "Dear creator, this pyhton course is nice. Thanks!"
Letter = "Dear Creator,\nthis python course is nice.\nThanks!"
print(Letter)
