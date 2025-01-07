"""
Modules and Imports in Python:

Modules allow you to organize and reuse code.
- Use `import` to bring in external modules.
- You can import entire modules or specific functions, classes, or variables from a module.
"""

# Example 1: Importing a Built-in Module
import math  # Importing the entire math module

print(f"Square root of 16: {math.sqrt(16)}")  # Using the sqrt function from math module

# Explanation:
# The `import math` statement imports the entire math module, allowing access to various functions and constants.
# In this case, we use `math.sqrt()` to calculate the square root of 16.

# Example 2: Importing a Specific Function from a Module
from math import pi  # Importing only the `pi` constant from the math module

print(f"Value of Pi: {pi}")  # Directly using the pi constant

# Explanation:
# You can import specific functions, classes, or variables from a module using `from <module> import <name>`.
# Here, only the `pi` constant is imported from the math module, which allows you to use it directly without needing to reference `math.pi`.

# Example 3: Renaming a Module on Import
import math as m  # Importing the math module with an alias

print(f"Value of Pi (using alias): {m.pi}")  # Using the pi constant with the alias

# Explanation:
# You can provide an alias to a module using the `as` keyword. This is especially useful for long module names or when avoiding naming conflicts.
# In this case, `math` is imported as `m`, so we use `m.pi` to access the constant.

# Example 4: Importing All Functions from a Module (Not Recommended)
from math import *  # Importing all functions and constants from math

print(f"Value of Pi (using * import): {pi}")  # Using pi directly without specifying the module name

# Explanation:
# The `from <module> import *` syntax imports everything from the module.
# While convenient, it is generally discouraged because it can lead to name conflicts and makes the code less readable, as you don’t know which functions are being imported.

# Example 5: Creating and Importing Your Own Module (Assume mymodule.py exists)
# Suppose we have a module named mymodule.py with a function `greet`:
# mymodule.py
# def greet(name):
#     return f"Hello, {name}!"

# Importing and using a custom module
import mymodule  # Assuming mymodule.py is in the same directory

print(mymodule.greet("Alice"))  # Calling the greet function from the custom module

# Explanation:
# You can create your own modules by writing Python code in a file and importing it using `import <module>`.
# You can call any functions, classes, or variables defined in your module using the `mymodule.<name>` syntax.

# Example 6: Organizing Code with Packages
# A package is a collection of modules in a directory. 
# For example, a directory named `my_package` containing two modules `module1.py` and `module2.py`.
# To import from a package:
# from my_package import module1
# from my_package.module1 import function_name