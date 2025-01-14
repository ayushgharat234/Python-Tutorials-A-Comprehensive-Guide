"""
Basic Syntax in Python:
Python is known for its simplicity and readability, but it has specific syntax rules that must be followed.
Below are some of the fundamental aspects of Python's syntax.
"""

# Example 1: Printing a Message
# The `print()` function is used to display output in Python.
print("Hello, World!")  # Output: Hello, World!
print("\n")  # Adds a newline for better readability in console output

# Explanation:
# - `print()` is a built-in function in Python that outputs data to the console. It can print strings, numbers, or other objects.

# Example 2: Indentation in Python
"""
Python uses indentation to define blocks of code. Unlike other programming 
languages that use braces `{}`, Python relies on proper indentation levels.
"""

# Correct Indentation
if True:  # This condition always evaluates to True
    print("This is indented correctly.")  # This block belongs to the `if` statement
else:
    print("This is also indented correctly.")  # This block belongs to the `else` statement
print("\n")

# Explanation:
# - Python uses indentation instead of curly braces to define code blocks.
# - All statements within an `if`, `for`, or `while` loop should be indented equally.

# Example 3: Syntax Errors Due to Incorrect Indentation
"""
Improper indentation will result in an `IndentationError`. Python does not allow inconsistent 
or missing indentation levels in blocks of code.
"""

# Uncomment the following lines to see an IndentationError:
# if True:
# print("This will raise an error!")  # Missing indentation

# Explanation:
# - Python will raise an `IndentationError` if the code block is not properly indented.

# Example 4: Inline Comments
# Use `#` for single-line comments in Python.
# Inline comments help explain your code:
greeting = "Hello, Python!"  # This variable stores a greeting message
print(greeting)  # Output: Hello, Python!
print("\n")

# Explanation:
# - Inline comments in Python are written using the `#` symbol. They are ignored during execution and are meant to explain parts of the code.

# Example 5: Multiline Comments

# For multiline comments or docstrings, use triple quotes (`'''` or `"""`).
# These are often used to describe the purpose of a function, module, or script.

"""
This is a multiline comment
or docstring. It can span
multiple lines.
"""

# Explanation:
# - Triple quotes (`'''` or `"""`) are used for multiline comments or documentation strings (docstrings).
# - Docstrings are useful for documenting functions, methods, or classes.

# Example 6: Case Sensitivity in Python
"""
Python is a case-sensitive language, meaning that `Variable`, `variable`, 
and `VARIABLE` are treated as three distinct identifiers.
"""
Variable = 10
variable = 20
VARIABLE = 30
print(f"Variable: {Variable}, variable: {variable}, VARIABLE: {VARIABLE}")
print("\n")

# Explanation:
# - Python treats variable names as case-sensitive, so `Variable`, `variable`, and `VARIABLE` would be considered different variables.

# Example 7: Writing Clean and Readable Code
"""
Python encourages writing clean, readable, and consistent code. 
Follow the PEP 8 guidelines for naming conventions and code structure.
"""

# Using snake_case for variables and function names (Recommended by PEP 8)
example_variable = "Python Basics"
print(example_variable)

# Explanation:
# - Following **PEP 8** guidelines for writing clean and readable code is encouraged.
# - For variable names, the **snake_case** convention (lowercase letters with underscores) is preferred.