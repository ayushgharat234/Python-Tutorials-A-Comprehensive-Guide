"""
Input and Output in Python:

Python provides built-in functions to handle input and output operations.
- `input()` is used to take input from the user.
- `print()` is used to display output on the console.
"""

# Example 1: Taking Input
name = input("Enter your name: ")  # Takes input from the user
age = int(input("Enter your age: "))  # Converts input to integer

print(f"Hello, {name}! You are {age} years old.")  # Prints a message with user input

# Explanation:
# The `input()` function reads a line from the input (keyboard) and returns it as a string.
# The first `input()` prompts the user to enter their name.
# The second `input()` asks for the age, and we use `int()` to convert the input (which is string by default) to an integer.
# The `print()` function outputs the formatted message using f-string formatting.

# Example 2: Output formatting using f-string
height = 5.9
print(f"Your height is: {height} feet.")  # f-string for formatting

# Explanation:
# `f-string` is a concise way to format strings in Python. The variables inside `{}` are replaced with their values.
# In this case, the value of `height` is embedded into the string and displayed.

# Example 3: Printing multiple values
print("Name:", name, "Age:", age)  # Prints multiple values

# Explanation:
# You can pass multiple arguments to `print()`, and Python will separate them by a space.
# This allows you to print multiple values in a single line.

# Example 4: String formatting using % operator
print("Name: %s, Age: %d" % (name, age))  # % formatting for strings and integers

# Explanation:
# The `%` operator can also be used to format strings in Python.
# `%s` is used for strings, and `%d` is used for integers.
# This example shows how to embed values in a string using the older formatting method (though `f-string` is preferred for readability and flexibility).