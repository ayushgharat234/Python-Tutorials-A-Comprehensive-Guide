"""
Attributes and Methods in Python:

Attributes are variables associated with a class or an object.
Methods are functions defined inside a class to describe the behavior of an object.
"""

# Example 1: Attributes
class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age  # Attribute

person1 = Person("John", 25)
print(f"Name: {person1.name}, Age: {person1.age}")

# Example 2: Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

person2 = Person("Alice", 30)
person2.introduce()  # Method call