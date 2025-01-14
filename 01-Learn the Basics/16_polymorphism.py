"""
Polymorphism in Python:

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is one of the core concepts in object-oriented programming (OOP). 
Polymorphism enables the use of a single interface to represent different underlying forms (data types).

Key Concepts:
- **Method Overriding**: Subclasses override methods of the parent class to provide their own implementation.
- **Duck Typing**: In Python, if an object implements a method with the correct signature, it can be used as if it were of the expected type, even if it doesn't explicitly inherit from the expected class.
- **Operator Overloading**: Polymorphism can also involve overloading operators, where operators are given new behavior depending on the operands' types.

Let's dive into these concepts with detailed examples.
"""

# Example 1: Polymorphism with Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# List of animals containing objects of different classes
animals = [Dog(), Cat()]

# Polymorphism in action: Different behavior depending on the object type
for animal in animals:
    animal.speak()  # Output will vary based on the object's class
    # Output: 
    # Dog barks
    # Cat meows

# Example 2: Polymorphism with Duck Typing
class Bird:
    def speak(self):
        print("Bird chirps")

class Duck:
    def speak(self):
        print("Duck quacks")

# Function that expects objects with a 'speak' method
def animal_speak(animal):
    animal.speak()  # Calling the 'speak' method on any object that has it

bird = Bird()
duck = Duck()

# Using Duck Typing: It doesn't matter whether the object is from Bird or Duck class, as long as it has the 'speak' method
animal_speak(bird)  # Output: Bird chirps
animal_speak(duck)  # Output: Duck quacks

# Example 3: Operator Overloading in Polymorphism
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Creating Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Using the overloaded '+' operator to add two Point objects
result = point1 + point2  # This calls the __add__ method
print(result)  # Output: Point(6, 8)

# Example 4: Polymorphism in Inheritance with Method Overriding
class Shape:
    def area(self):
        pass  # Base method does nothing, to be overridden in subclasses

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * (self.radius ** 2)

# List of different shapes
shapes = [Rectangle(4, 5), Circle(3)]

# Calculating area for different shapes using polymorphism
for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 20
# Area: 28.274333882308138

# Example 5: Polymorphism with Method Overloading (using default arguments)
class Printer:
    def print_message(self, message, times=1):  # Default argument for times
        for _ in range(times):
            print(message)

printer = Printer()
printer.print_message("Hello")  # Default behavior, prints once
printer.print_message("Hello", 3)  # Overloaded behavior, prints three times

# Example 6: Polymorphism with Abstract Classes
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating instances and invoking the overridden method
dog = Dog()
cat = Cat()

dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows

# Example 7: Polymorphism in a Real-World Example (Different Devices)
class Device:
    def power_on(self):
        pass  # Base method to be overridden by subclasses

class Phone(Device):
    def power_on(self):
        print("Phone is turning on...")

class Laptop(Device):
    def power_on(self):
        print("Laptop is starting...")

# A function that works with any Device object
def device_power_on(device: Device):
    device.power_on()

# Using polymorphism with different device types
phone = Phone()
laptop = Laptop()

device_power_on(phone)  # Output: Phone is turning on...
device_power_on(laptop)  # Output: Laptop is starting...