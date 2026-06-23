#Topic 1: Variables, Data Types, and Type Casting
# 01_variables_data_types.py

# 1. Variables and Basic Data Types
age = 25                  # Integer (int)
price = 19.99             # Floating point (float)
name = "Alice"            # String (str)
is_active = True          # Boolean (bool)

print("--- Basic Data Types ---")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")

# 2. String Methods (Crucial built-in methods)
message = "  python programming is fun!  "
print("\n--- String Methods ---")
print(f"Original: '{message}'")
print(f"Strip whitespace: '{message.strip()}'")
print(f"Uppercase: '{message.upper().strip()}'")
print(f"Replace: '{message.replace('fun', 'awesome').strip()}'")
print(f"Split into list: {message.split()}")

# 3. Type Casting (Conversion)
x = "100"
y = int(x)  # Converting string to integer
z = float(x) # Converting string to float

print("\n--- Type Casting ---")
print(f"String to Int: {y} ({type(y)})")
print(f"String to Float: {z} ({type(z)})")
#Topic 2: Control Flow (If, Elif, Else)
# 02_control_flow.py

# 1. Conditional Logic
score = 85

print("--- Grading System ---")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 2. Logical Operators (and, or, not)
has_ticket = True
is_adult = False

print("\n--- Gate Check ---")
if has_ticket and (is_adult or score > 80):
    print("Access Granted!")
else:
    print("Access Denied!")
  #Topic 3: Loops (For and While)
  # 03_loops.py

# 1. For Loop with range()
print("--- For Loop (0 to 4) ---")
for i in range(5):
    print(f"Iteration {i}")

# 2. Looping through a String
print("\n--- Looping through Characters ---")
word = "Python"
for letter in word:
    print(letter, end="-")
print() # New line

# 3. While Loop with Break and Continue
print("\n--- While Loop with Conditions ---")
count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # Skip the rest of this loop iteration
    if count == 6:
        break     # Exit the loop entirely
    print(f"Count is: {count}")
  #Topic 4: Functions & Scope
  # 04_functions.py

# 1. Basic Function with Default Parameters
def greet_user(name="Guest"):
    """Greets a user with a default fallback."""
    return f"Hello, {name}!"

# 2. Function with Multiple Return Values
def calculate_rectangle(length, width):
    """Calculates both area and perimeter."""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returns a tuple

# Testing the functions
print("--- Testing Functions ---")
print(greet_user("Bob"))
print(greet_user()) # Uses default parameter

# Unpacking multiple return values
rect_area, rect_perm = calculate_rectangle(5, 4)
print(f"\nArea: {rect_area}, Perimeter: {rect_perm}")
#Topic 5: Lists and Tuples
# 05_lists_tuples.py

# 1. Lists (Mutable / Changeable)
fruits = ["apple", "banana", "cherry"]
print("--- List Basics ---")
print(f"Original List: {fruits}")

# List Methods
fruits.append("orange")      # Add to end
fruits.insert(1, "mango")    # Insert at index 1
fruits.remove("banana")      # Remove by value
popped_item = fruits.pop()   # Removes and returns last item

print(f"Modified List: {fruits}")
print(f"Popped Item: {popped_item}")
print(f"List Slicing (first two): {fruits[0:2]}")

# 2. Tuples (Immutable / Cannot be changed)
# Used for data that shouldn't change (e.g., coordinates)
coordinates = (10.0, 20.0)
print("\n--- Tuple Basics ---")
print(f"Coordinates: {coordinates}")
print(f"X Coordinate: {coordinates}")

# Trying to change a tuple will throw an error:
# coordinates = 15.0  # TypeError: 'tuple' object does not support item assignment
#Topic 6: Dictionaries and Sets
# 06_dictionaries_sets.py

# 1. Dictionaries (Key-Value Pairs)
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "CompSci"]
}

print("--- Dictionary Methods ---")
print(f"Student Name: {student.get('name')}")
print(f"Safe Fetch (Non-existent key): {student.get('grade', 'Not Found')}")

# Adding/Updating
student["grade"] = "A"
student["age"] = 22

# Iterating keys and values
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")

# 2. Sets (Unique items, Unordered)
print("\n--- Set Operations ---")
numbers_list =
unique_numbers = set(numbers_list) # Removes duplicates automatically
print(f"Original List: {numbers_list}")
print(f"Unique Set: {unique_numbers}")

# Set math
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Intersection (Common): {set_a.intersection(set_b)}")
print(f"Union (All unique): {set_a.union(set_b)}")
