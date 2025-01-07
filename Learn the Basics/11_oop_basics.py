"""
Object-Oriented Programming (OOP) Basics:

OOP is a programming paradigm that uses objects and classes. In OOP:
- Classes define the structure and behavior of objects. A class acts as a blueprint for creating instances (objects).
- Objects are instances of classes and contain data (attributes) and methods (functions) that operate on that data.
"""

# Example 1: Basic Class Definition
class Dog:
    pass  # Empty class with no methods or attributes

# Creating an instance (object) of the Dog class
dog1 = Dog()

# Printing the object
print(dog1)  # Output: <__main__.Dog object at 0x7f9f68c54fd0>

# In this example, the Dog class does not have any attributes or methods, 
# but we can still create objects from it.
# The printed output shows the default memory address of the object.


# Example 2: Class with Constructor (__init__)
class Dog:
    def __init__(self, name, breed):
        # The __init__ method is a special method (constructor) that initializes object attributes
        self.name = name  # Instance attribute for dog's name
        self.breed = breed  # Instance attribute for dog's breed

# Creating an instance of Dog class with specific attributes
dog1 = Dog("Max", "Golden Retriever")

# Accessing object attributes
print(f"Dog's Name: {dog1.name}, Breed: {dog1.breed}")
# Output: Dog's Name: Max, Breed: Golden Retriever

# Explanation: 
# The __init__ method initializes the attributes (name and breed) when a new object is created.
# Here, we create a Dog object named 'dog1' with the name "Max" and breed "Golden Retriever."


# Example 3: Adding Methods to Classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    # Instance method to display dog's information
    def display_info(self):
        print(f"Dog's Name: {self.name}, Breed: {self.breed}")

# Creating an object of Dog
dog2 = Dog("Buddy", "Labrador")

# Calling the method to display information about the dog
dog2.display_info()  # Output: Dog's Name: Buddy, Breed: Labrador

# Explanation:
# The 'display_info' method prints the information about the dog.
# The 'self' parameter refers to the instance of the object calling the method.


# Example 4: Adding More Methods with Parameters
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def display_info(self):
        print(f"Dog's Name: {self.name}, Breed: {self.breed}")
    
    # Method with parameter to make the dog bark
    def bark(self, sound):
        print(f"{self.name} says: {sound}")

# Creating an object of Dog
dog3 = Dog("Charlie", "Beagle")

# Calling methods with parameters
dog3.display_info()  # Output: Dog's Name: Charlie, Breed: Beagle
dog3.bark("Woof Woof")  # Output: Charlie says: Woof Woof

# Explanation:
# The 'bark' method takes a parameter 'sound' and prints a message.
# The 'bark' method allows the dog to "speak" by printing a sound.


# Example 5: Object with Multiple Methods and Attributes
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def display_info(self):
        print(f"Dog's Name: {self.name}, Breed: {self.breed}, Age: {self.age}")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Creating a Dog object
dog4 = Dog("Bella", "Poodle", 3)

# Calling multiple methods on the dog object
dog4.display_info()  # Output: Dog's Name: Bella, Breed: Poodle, Age: 3
dog4.celebrate_birthday()  # Output: Happy Birthday, Bella! You are now 4 years old.
dog4.display_info()  # Output: Dog's Name: Bella, Breed: Poodle, Age: 4

# Explanation:
# We created a Dog object with three attributes: name, breed, and age.
# The 'celebrate_birthday' method increases the age of the dog by 1 year.


# Example 6: Using Class Variables (Shared among all instances)
class Dog:
    species = "Canis familiaris"  # Class variable shared by all instances
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Creating multiple Dog objects
dog5 = Dog("Rocky", "Bulldog")
dog6 = Dog("Luna", "German Shepherd")

# Accessing class variable through instances
print(f"{dog5.name} is a {dog5.species}.")  # Output: Rocky is a Canis familiaris.
print(f"{dog6.name} is a {dog6.species}.")  # Output: Luna is a Canis familiaris.

# Explanation:
# The class variable 'species' is shared by all instances of the class.
# It is accessed using the instance, but can also be accessed directly using the class name.