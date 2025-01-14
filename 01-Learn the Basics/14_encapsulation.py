"""
Encapsulation in Python:

Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data 
within a single unit or class. It restricts direct access to some of an object's components, which 
is a fundamental aspect of object-oriented programming (OOP). In Python, encapsulation is achieved 
through the use of public, protected, and private attributes and methods.

Key concepts:
- Public: Accessible from anywhere.
- Protected: Intended for internal use (by convention, with a single underscore `_`).
- Private: Not accessible directly from outside the class (indicated by double underscores `__`).

This example demonstrates how encapsulation works in Python.
"""

# Example 1: Encapsulation with private attributes
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (cannot be accessed directly outside the class)
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    # Public method to get the balance
    def get_balance(self):
        return self.__balance
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

# Creating an instance of Account with an initial balance of 1000
account1 = Account(1000)

# Deposit money
account1.deposit(500)

# Attempt to access private attribute (will result in an error)
# print(account1.__balance)  # This will raise an AttributeError

# Get balance using public method
print(f"Account Balance: {account1.get_balance()}")  # Output: Account Balance: 1500

# Withdraw money using public method
account1.withdraw(200)
print(f"Account Balance after withdrawal: {account1.get_balance()}")  # Output: 1300

# Attempting to withdraw more money than the balance
account1.withdraw(2000)  # Output: Invalid withdrawal amount.

# Example 2: Encapsulation with protected attributes
class Employee:
    def __init__(self, name, salary):
        self._name = name  # Protected attribute (should be accessed within the class or subclasses)
        self._salary = salary
    
    # Public method to get employee details
    def get_details(self):
        return f"Name: {self._name}, Salary: {self._salary}"

# Creating an instance of Employee
emp1 = Employee("John Doe", 50000)

# Accessing the protected attribute directly (discouraged, but still possible)
print(f"Employee Name (Accessed Directly): {emp1._name}")  # Output: John Doe

# Example 3: Encapsulation with class methods and class-level encapsulation
class Bank:
    interest_rate = 0.05  # Class-level attribute
    
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
    
    # Public method to apply interest to balance
    def apply_interest(self):
        self.__balance += self.__balance * Bank.interest_rate
    
    # Public method to get the account details
    def get_account_details(self):
        return f"Account Number: {self.__account_number}, Balance: {self.__balance}"

# Creating an instance of Bank
bank_account = Bank("123456789", 10000)

# Applying interest
bank_account.apply_interest()

# Printing account details
print(bank_account.get_account_details())  # Output: Account Number: 123456789, Balance: 10500.0

# Example 4: Encapsulation with method hiding (private methods)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Private method to check engine health
    def __check_engine(self):
        print("Engine is in good condition.")
    
    # Public method to start the car, which calls the private method
    def start_car(self):
        print(f"Starting the {self.year} {self.make} {self.model}...")
        self.__check_engine()

# Creating an instance of Car
car1 = Car("Tesla", "Model S", 2023)

# Starting the car (this will invoke the private method __check_engine)
car1.start_car()

# Attempt to call the private method directly (will raise an AttributeError)
# car1.__check_engine()  # Uncommenting this will raise an error

# Example 5: Property Decorators for Controlled Access
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    # Getter for name
    @property
    def name(self):
        return self.__name
    
    # Setter for name (allows controlled modification)
    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            print("Invalid name.")
    
    # Getter for age
    @property
    def age(self):
        return self.__age
    
    # Setter for age (only allows setting age greater than 0)
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age.")

# Creating an instance of Student
student1 = Student("Alice", 20)

# Accessing name and age via getter methods
print(f"Student Name: {student1.name}")  # Output: Alice
print(f"Student Age: {student1.age}")  # Output: 20

# Modifying name and age using setter methods
student1.name = "Bob"
student1.age = 25

# Attempting to set invalid values for name and age
student1.name = "   "  # Invalid name
student1.age = -5  # Invalid age

# Display updated details
print(f"Updated Student Name: {student1.name}")  # Output: Bob
print(f"Updated Student Age: {student1.age}")  # Output: 25