"""
Inheritance in Python:

Inheritance allows one class to inherit attributes and methods from another class. It is one of the fundamental concepts in object-oriented programming (OOP). 
Inheritance enables the creation of a new class (child class) from an existing class (parent class), allowing the child class to reuse code from the parent class.

Key Concepts:
- **Single Inheritance**: A class inherits from a single parent class.
- **Multiple Inheritance**: A class inherits from more than one parent class.
- **Multilevel Inheritance**: A class inherits from a class that is itself derived from another class.
- **Hierarchical Inheritance**: Multiple classes inherit from a single parent class.
- **Method Overriding**: A child class can provide its own implementation of a method that is already defined in its parent class.
- **Method Resolution Order (MRO)**: In case of multiple inheritance, the order in which methods are resolved is defined by Python’s MRO.

Let’s explore these concepts with detailed examples.
"""

# Example 1: Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inheriting from Animal class
class Dog(Animal):
    def speak(self):
        print("Dog barks")  # Method overriding in the child class

# Creating an instance of Dog
dog1 = Dog()
dog1.speak()  # Output: Dog barks (method overriding)

# Example 2: Multiple Inheritance
class Bird:
    def fly(self):
        print("Bird flies")

class Fish:
    def swim(self):
        print("Fish swims")

# Child class inheriting from both Bird and Fish
class FlyingFish(Bird, Fish):
    def jump(self):
        print("Flying Fish jumps out of the water")

# Creating an instance of FlyingFish
flying_fish = FlyingFish()
flying_fish.fly()  # Output: Bird flies (inherited from Bird class)
flying_fish.swim()  # Output: Fish swims (inherited from Fish class)
flying_fish.jump()  # Output: Flying Fish jumps out of the water

# Example 3: Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def move(self):
        print("Mammal moves")

class Dog(Mammal):  # Inheriting from Mammal, which inherits from Animal
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
dog2 = Dog()
dog2.speak()  # Output: Animal speaks (inherited from Animal class)
dog2.move()   # Output: Mammal moves (inherited from Mammal class)
dog2.bark()   # Output: Dog barks (defined in Dog class)

# Example 4: Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Creating instances of Dog and Cat
dog3 = Dog()
dog3.eat()  # Output: Animal eats (inherited from Animal class)
dog3.bark()  # Output: Dog barks (defined in Dog class)

cat1 = Cat()
cat1.eat()  # Output: Animal eats (inherited from Animal class)
cat1.meow()  # Output: Cat meows (defined in Cat class)

# Example 5: Method Overriding
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):  # Overriding the start method of the parent class
        print("Car starts with a key")

class ElectricCar(Car):
    def start(self):  # Overriding again in the subclass
        print("Electric Car starts with a button press")

# Creating instances and calling the start method
vehicle = Vehicle()
vehicle.start()  # Output: Vehicle starts

car = Car()
car.start()  # Output: Car starts with a key

electric_car = ElectricCar()
electric_car.start()  # Output: Electric Car starts with a button press

# Example 6: Super() Function for Accessing Parent Class Methods
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()  # Calling the parent class method

# Creating an instance of Dog
dog4 = Dog()
dog4.speak()  # Output: Dog barks, Animal speaks (calling the parent class method using super())

# Example 7: Method Resolution Order (MRO) in Multiple Inheritance
class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")

class C(A):
    def method(self):
        print("Method from class C")

class D(B, C):  # Multiple inheritance
    pass

# Creating an instance of D
d = D()
d.method()  # Output: Method from class B (MRO follows the order of inheritance)

# Printing the MRO of class D
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]