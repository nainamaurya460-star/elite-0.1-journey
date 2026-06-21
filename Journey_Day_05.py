# Question 1: Dictionary of Hindi words with English translation. Option to look it up.
words = { 
    "madad": "help",
    "kursi": "chair",
    "billi": "cat"
}
word = input("Enter the word you want meaning of: ")
# Fixed: Dictionary values are accessed using square brackets [], not parentheses ()
print("Meaning:", words[word])


# Question 2: Input eight numbers from the user and display all the unique numbers.
# Fixed: Initialized an empty set 's' before adding elements
s = set()
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 2: ")
s.add(int(n))
n = input("Enter number 3: ")
s.add(int(n))
n = input("Enter number 4: ")
s.add(int(n))
n = input("Enter number 5: ")
s.add(int(n))
n = input("Enter number 6: ")
s.add(int(n))
n = input("Enter number 7: ")
s.add(int(n))
n = input("Enter number 8: ")
s.add(int(n))
print("Unique numbers are:", s)


# Question 3: Can we have a set with 18 (int) and '18' (str) as a value in it?
s = set()
s.add(18)
s.add("18")
print("Set with int and str:", s) # Yes, because their data types are different.


# Question 4: What will be the length of following set 's'?
s = set()
s.add(20)
s.add(20.0) # In Python, 20 and 20.0 are considered equal in a set, so it won't be duplicated.
s.add('20') 
print("Length of set:", len(s)) # Output will be 2


# Question 5: What is the type of s = {}?
s = {} 
print("Type of s = {}:", type(s)) # Output will be <class 'dict'> because {} creates an empty dictionary.


# Question 6: Empty dictionary. Allow 4 friends to enter their favorite language (Keys = Names, Values = Languages).
d = {}
name = input("Enter friend's name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend's name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend's name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend's name: ")
lang = input("Enter language name: ")
d.update({name: lang})
print("Friends and languages:", d)


# Question 7: If the names of 2 friends are same, what will happen to the program in problem 6?
# Answer: The later entry will overwrite the previous entry because dictionary keys must be unique.


# Question 8: If languages of two friends are same, what will happen to the program in problem 6?
# Answer: Nothing will happen. Multiple keys can have the same values.


# Question 9: Can you change the value inside a list which is contained in set s?
# Answer: No, because we cannot include a list inside a set. Lists are unhashable/mutable.
# The code below will deliberately throw a TypeError: unhashable type: 'list'
# s = {8, 7, 12, "creator",}
