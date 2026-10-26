# 🚀 Python OOPs Basics: Class & Object Explanation

Welcome to this beginner-friendly guide on Object-Oriented Programming (OOP) in Python! This repository explains the core concepts of **Classes**, **Objects**, `__init__`, and `self` with real-world analogies.

---

## 📌 Concept Breakdown

### 1. What is a Class and an Object?
* **Class (The Blueprint):** Think of a class as a blueprint or a map. It defines the structure, properties, and actions, but doesn't contain real data by itself.
* **Object (The Reality):** An object is the actual instance created from that blueprint.



### 2. Why do we use `__init__` and `self`?
* **`__init__` (The Constructor):** This is a special method that runs automatically whenever a new object is created. It initializes (loads) the initial data into the object.
* **`self` (The Identity):** It represents the specific object you are currently working with. It acts like a pointer saying, *"This is MY name"* or *"This is MY data"*.



---

## 💻 Code Example: The Student System

Here is a practical script demonstrating how a single `Student` class can be used to create multiple distinct student profiles dynamically.

```python
# Defining the Blueprint (Class)
class Student:
    def __init__(self, name, branch):
        self.name = name       # Object's property (Attribute)
        self.branch = branch   # Object's property (Attribute)

    # Object's Action (Method)
    def introduce(self):
        print(f"Hi, mera naam {self.name} hai aur meri branch {self.branch} hai.")

# Creating Real-World Instances (Objects)
student1 = Student("Naina", "CSE")
student2 = Student("Harsh", "ECE")

# Executing Actions
student1.introduce()  # Output: Hi, mera naam Naina hai aur meri branch CSE hai.
student2.introduce()  # Output: Hi, mera naam Harsh hai aur meri branch ECE hai.
