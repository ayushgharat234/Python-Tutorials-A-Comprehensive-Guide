"""
Classes and Objects in Python:

In Python, classes are blueprints for creating objects (instances). 
An object is an instance of a class, and it is created by calling the class as if it were a function. 
Classes allow you to bundle data and functionality together. 
They provide a way to model real-world entities with attributes (data) and methods (functions).
"""

# Example 1: Creating an Object from a Class
class Car:
    # Constructor (__init__) method to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Instance method to display car details
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Creating objects (instances of the Car class)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing instance attributes and calling methods
car1.display_info()  # Output: Car Make: Toyota, Model: Corolla, Year: 2020
car2.display_info()  # Output: Car Make: Honda, Model: Civic, Year: 2022


# Example 2: Adding Methods to Classes
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # Method to simulate starting the car
    def start(self):
        print(f"{self.make} {self.model} is starting!")

    # Method to simulate stopping the car
    def stop(self):
        print(f"{self.make} {self.model} is stopping!")

# Creating another car object
car3 = Car("Ford", "Mustang")
car3.start()  # Output: Ford Mustang is starting!
car3.stop()   # Output: Ford Mustang is stopping!


# Example 3: Using Class Variables (Shared among all instances)
class Car:
    wheels = 4  # Class variable
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating car objects
car4 = Car("Chevrolet", "Malibu")
car5 = Car("BMW", "X5")

# Accessing class variable through instances
print(f"{car4.make} {car4.model} has {car4.wheels} wheels.")  # Output: Chevrolet Malibu has 4 wheels.
print(f"{car5.make} {car5.model} has {car5.wheels} wheels.")  # Output: BMW X5 has 4 wheels.


# Example 4: Modifying Class Variables
class Car:
    wheels = 4  # Class variable
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Creating car objects
car6 = Car("Tesla", "Model S")
car7 = Car("Nissan", "Leaf")

# Changing the class variable value
Car.wheels = 5

print(f"{car6.make} {car6.model} has {car6.wheels} wheels.")  # Output: Tesla Model S has 5 wheels.
print(f"{car7.make} {car7.model} has {car7.wheels} wheels.")  # Output: Nissan Leaf has 5 wheels.


# Example 5: Instance Variables (Unique to each object)
class Car:
    def __init__(self, make, model, year):
        self.make = make        # Instance variable
        self.model = model      # Instance variable
        self.year = year        # Instance variable
    
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Creating instances with different values
car8 = Car("Audi", "A4", 2023)
car9 = Car("Mercedes", "C-Class", 2022)

# Accessing instance variables
car8.display_info()  # Output: Car: 2023 Audi A4
car9.display_info()  # Output: Car: 2022 Mercedes C-Class


# Example 6: Class Methods and Static Methods

class Car:
    wheels = 4  # Class variable
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # Class method (can modify class state)
    @classmethod
    def change_wheels(cls, new_wheel_count):
        cls.wheels = new_wheel_count
    
    # Static method (does not depend on the class or instance)
    @staticmethod
    def car_info():
        print("This is a car.")

# Creating car objects
car10 = Car("Toyota", "Camry")
car11 = Car("Honda", "Accord")

# Calling class method to change class variable
Car.change_wheels(6)

# Calling static method (no need to create an instance)
Car.car_info()  # Output: This is a car.

# Checking the updated wheels for all cars
print(f"Car 1 has {car10.wheels} wheels.")  # Output: Car 1 has 6 wheels.
print(f"Car 2 has {car11.wheels} wheels.")  # Output: Car 2 has 6 wheels.


# Example 7: Inheritance and Overriding Methods
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)  # Call the constructor of the parent class
        self.year = year
    
    # Overriding the display_info method
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Creating objects of the Car class (inheriting from Vehicle)
car12 = Car("Tesla", "Model 3", 2023)
car12.display_info()  # Output: Car: 2023 Tesla Model 3


# Example 8: Encapsulation in Classes (Private attributes)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    # Public method to access private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
    
    def get_balance(self):
        return self.__balance

# Creating object
account = BankAccount(1000)
account.deposit(500)  # Output: Deposited 500. New balance: 1500
print(f"Balance: {account.get_balance()}")  # Output: Balance: 1500

# Trying to access private attribute directly will raise an error
# print(account.__balance)  # Uncommenting this line will raise an AttributeError


# Example 9: Deleting Objects (Garbage Collection)
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}")

# Creating an object
car13 = Car("Ford", "Explorer")
car13.display_info()  # Output: Car Make: Ford, Model: Explorer

# Deleting the object
del car13

# Trying to access the object after deletion will raise an error
# car13.display_info()  # Uncommenting this line will raise a NameError