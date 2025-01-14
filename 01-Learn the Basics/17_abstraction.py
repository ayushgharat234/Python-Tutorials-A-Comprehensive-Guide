"""
Abstraction in Python:

Abstraction is the concept of hiding the implementation details and showing only the essential features of an object. 
In Python, abstraction is typically achieved using abstract classes and abstract methods, which provide a blueprint for other classes to follow.

Key Concepts:
- **Abstract Classes**: Classes that cannot be instantiated and are meant to be inherited by other classes. They contain abstract methods that must be implemented by their subclasses.
- **Abstract Methods**: Methods defined in an abstract class that have no implementation. Subclasses are required to implement these methods.
- **Encapsulation vs Abstraction**: While encapsulation hides the internal workings of an object, abstraction hides unnecessary implementation details and exposes only what is necessary.

Let's dive into these concepts with detailed examples.
"""

from abc import ABC, abstractmethod

# Example 1: Basic Abstract Class Example
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass  # No implementation, subclass must provide it

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating objects of subclasses and invoking the abstract method
dog = Dog()
dog.speak()  # Output: Dog barks

cat = Cat()
cat.speak()  # Output: Cat meows

# Example 2: Abstract Class with Concrete Methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclasses must implement this method
    
    def description(self):
        return "This is a shape."  # Concrete method, can be used as-is by subclasses

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

# Creating objects of subclasses and invoking abstract and concrete methods
rectangle = Rectangle(4, 5)
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 20
print(rectangle.description())  # Output: This is a shape.

circle = Circle(3)
print(f"Circle Area: {circle.area()}")  # Output: Circle Area: 28.274333882308138
print(circle.description())  # Output: This is a shape.

# Example 3: Using Abstract Methods in a Real-World Scenario
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, query_string):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL database...")
    
    def query(self, query_string):
        print(f"Executing MySQL query: {query_string}")

class MongoDBDatabase(Database):
    def connect(self):
        print("Connecting to MongoDB database...")
    
    def query(self, query_string):
        print(f"Executing MongoDB query: {query_string}")

# Creating objects of the concrete subclasses and using their methods
mysql_db = MySQLDatabase()
mysql_db.connect()  # Output: Connecting to MySQL database...
mysql_db.query("SELECT * FROM users")  # Output: Executing MySQL query: SELECT * FROM users

mongo_db = MongoDBDatabase()
mongo_db.connect()  # Output: Connecting to MongoDB database...
mongo_db.query("db.users.find()")  # Output: Executing MongoDB query: db.users.find()

# Example 4: Abstract Classes for Plug-in Systems
class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass  # Subclasses must implement this method

class PluginA(Plugin):
    def execute(self):
        print("Executing Plugin A")

class PluginB(Plugin):
    def execute(self):
        print("Executing Plugin B")

# List of plugins, simulating a plug-in system
plugins = [PluginA(), PluginB()]

for plugin in plugins:
    plugin.execute()  # Output: 
    # Executing Plugin A
    # Executing Plugin B

# Example 5: Enforcing Method Implementation with Abstract Classes
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass  # Abstract method, subclasses must implement it

    def display_area(self):
        print(f"Area of shape: {self.calculate_area()}")  # Concrete method, usable by subclasses

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# Creating object of Square and using inherited methods
square = Square(4)
square.display_area()  # Output: Area of shape: 16