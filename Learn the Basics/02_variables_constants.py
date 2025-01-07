"""
Variables and Constants in Python:
In Python, variables are used to store data, and constants are used to represent fixed values.
"""

# Example 1: Declaring Variables
# Variables are created when you assign a value to them.
x = 10  # `x` is an integer variable
y = 20.5  # `y` is a float variable
name = "Python"  # `name` is a string variable
print(f"x: {x}, y: {y}, name: {name}")

# Explanation:
# - Variables are containers that store data. The data type is inferred from the assigned value.

# Example 2: Changing Variable Values
x = 42  # Assign a new value to `x`
print(f"Updated x: {x}")

# Explanation:
# - Variables can be reassigned with new values, and the type will automatically adjust.

# Example 3: Constants in Python
"""
Python does not have built-in constant types. By convention, constants are defined
using uppercase letters and underscores to indicate they should not be changed.
"""
PI = 3.14159  # Define a constant for the value of pi
GRAVITY = 9.8  # Define a constant for the acceleration due to gravity
print(f"PI: {PI}, GRAVITY: {GRAVITY}")

# Note: While constants can technically be reassigned, it is discouraged.
# Uncomment the next line to reassign a constant (not recommended):
# PI = 3.14

# Explanation:
# - Constants are conventionally written in uppercase letters with underscores, but Python does not enforce immutability.

# Example 4: Dynamic Typing in Python
"""
Python is dynamically typed, meaning you don't need to declare the type of a variable.
A variable can change its type during the program's execution.
"""
variable = 10  # Initially an integer
print(f"variable (int): {variable}")
variable = "Now a string"  # Change to a string
print(f"variable (str): {variable}")

# Explanation:
# - Python is dynamically typed, meaning the type of a variable is determined at runtime and can change.

# Example 5: Multiple Assignments
"""
You can assign multiple variables in one line.
"""
a, b, c = 1, 2, 3  # Assign values to `a`, `b`, and `c` in a single line
print(f"a: {a}, b: {b}, c: {c}")

# Explanation:
# - Python allows you to assign multiple variables in a single line, making the code more concise.

# Example 6: Using `type()` Function
"""
The `type()` function is used to check the type of a variable.
"""
print(f"Type of x: {type(x)}")
print(f"Type of name: {type(name)}")
print(f"Type of y: {type(y)}")

# Explanation:
# - The `type()` function returns the type of an object, which helps understand the data type.

# Example 7: Deleting Variables
"""
The `del` keyword is used to delete a variable.
"""
del x  # Delete the variable `x`
# Uncomment the next line to see a NameError:
# print(x)  # This will raise an error because `x` has been deleted

# Explanation:
# - The `del` keyword deletes the variable and its reference from memory, causing a NameError if accessed afterward.

# Example 8: Global vs Local Variables
"""
Variables declared inside a function are local, whereas those declared outside
are global. Use the `global` keyword to modify a global variable inside a function.
"""
global_var = "I am global"

def example_function():
    local_var = "I am local"  # Local variable
    print(local_var)
    global global_var  # Access the global variable
    global_var = "Modified global variable"

example_function()
print(global_var)

# Explanation:
# - Global variables are declared outside functions and can be accessed anywhere in the program.
# - Local variables are declared inside functions and can only be used within those functions.
# - The `global` keyword is used to modify a global variable from within a function.