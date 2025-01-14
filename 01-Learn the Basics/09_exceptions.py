"""
Exceptions in Python:

Exceptions are errors that occur during the execution of the program.
- Use `try`, `except`, `else`, and `finally` for handling exceptions.
- Exceptions allow programs to handle runtime errors gracefully without crashing.
"""

# Example 1: Basic Exception Handling
try:
    num = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Handling division by zero error

# Explanation:
# The code inside the try block may raise an exception. In this case, dividing by zero raises a ZeroDivisionError.
# The except block catches this specific exception and handles it, preventing the program from crashing.

# Example 2: Handling Multiple Exceptions
try:
    num = int("hello")  # This will raise a ValueError
except ValueError:
    print("Invalid input! Please enter a valid number.")  # Handling ValueError
except Exception as e:
    print(f"An unexpected error occurred: {e}")  # Catching any other unexpected exceptions

# Explanation:
# You can handle multiple types of exceptions using different except blocks.
# ValueError occurs when attempting to convert a non-numeric string into an integer.
# The generic Exception block catches any other exceptions not specifically handled.

# Example 3: Using `finally` Block
try:
    file = open("test.txt", "r")
    print(file.read())  # Trying to read from a file
except FileNotFoundError:
    print("File not found!")  # Handling FileNotFoundError
finally:
    print("Execution completed.")  # Always executed, whether an exception occurred or not

# Explanation:
# The finally block is always executed, whether an exception occurred or not.
# It is useful for releasing resources like closing a file or network connection, regardless of success or failure.

# Example 4: Using `else` Block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")  # This will execute only if no exception was raised

# Explanation:
# The else block is executed only if no exceptions occur in the try block.
# It is useful for code that should only run if the try block is successful.

# Example 5: Catching Multiple Exceptions with a Single `except`
try:
    x = [1, 2, 3]
    print(x[5])  # IndexError will occur
except (IndexError, KeyError) as e:
    print(f"Caught an exception: {e}")  # Handling multiple exceptions

# Explanation:
# You can catch multiple exceptions in a single `except` block by passing a tuple of exception types.
# This helps when you want to handle different types of errors in the same way.

# Example 6: Raising Custom Exceptions
class CustomError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise CustomError("Negative numbers are not allowed.")  # Raising a custom exception

try:
    check_positive(-5)
except CustomError as e:
    print(f"Error: {e}")

# Explanation:
# You can create custom exception classes by inheriting from the built-in `Exception` class.
# This allows you to define your own exception types and raise them when needed.

# Example 7: Handling Specific Exception Types
try:
    number = int("hello")  # ValueError will occur
except ValueError as e:
    print(f"ValueError: {e}")
except Exception as e:
    print(f"General Error: {e}")

# Explanation:
# Specific exceptions should be handled before the general `Exception` block to catch known error types first.
# This allows for more precise handling and better debugging.

# Example 8: AssertionError
try:
    assert 2 + 2 == 5, "Math is broken!"  # This will raise an AssertionError
except AssertionError as e:
    print(f"AssertionError: {e}")

# Explanation:
# An `AssertionError` is raised when an `assert` statement fails.
# The assert statement is used to test a condition, and if the condition is false, an exception is raised.

# Example 9: Handling KeyboardInterrupt
try:
    while True:
        print("Press Ctrl+C to exit.")
except KeyboardInterrupt:
    print("Program interrupted by user.")  # Handling manual interruption (Ctrl+C)

# Explanation:
# The `KeyboardInterrupt` exception is raised when the user interrupts the program, typically by pressing Ctrl+C.
# This can be caught to prevent abrupt program termination.

# Example 10: FileNotFoundError and Handling Missing Files
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found! Please check the file path.")  # Handling file not found error
except IOError:
    print("General I/O error occurred.")
finally:
    print("File operation attempted.")

# Explanation:
# `FileNotFoundError` is raised when trying to open a file that doesn't exist.
# You can handle specific file-related errors such as `FileNotFoundError` and `IOError`.
# The `finally` block is useful for ensuring that the program continues even if an exception occurs.