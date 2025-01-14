"""
Functions in Python:

Functions are used to organize code into reusable blocks.
- Functions are defined using the `def` keyword.
- They can accept arguments, return values, and include default values.
"""

# Example 1: Simple Function
def greet(name):
    return f"Hello, {name}!"  # Return a greeting message

print(greet("Alice"))  # Calling the function with the argument "Alice"

# Explanation:
# A function named `greet` is defined, which takes one parameter `name`.
# The function returns a greeting message, which is then printed when the function is called.

# Example 2: Function with Default Argument
def greet(name="Guest"):
    return f"Hello, {name}!"  # If no argument is passed, "Guest" is used by default

print(greet())  # Calling the function without any argument (uses default)
print(greet("Bob"))  # Calling the function with the argument "Bob"

# Explanation:
# The function `greet` has a default argument `name="Guest"`, which means if no argument is provided, it uses "Guest" as the default value.
# If an argument is passed, it overrides the default value.

# Example 3: Function with Multiple Arguments
def add(a, b):
    return a + b  # Return the sum of a and b

print(add(10, 20))  # Calling the function with arguments 10 and 20

# Explanation:
# The function `add` takes two parameters `a` and `b` and returns their sum.
# We call the function with two numbers, and it returns their sum, which is printed.

# Example 4: Function with Arbitrary Number of Arguments (*args)
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4)  # Function call with arbitrary number of arguments

# Explanation:
# The `*args` syntax allows the function to accept an arbitrary number of positional arguments.
# `args` is treated as a tuple, and we can iterate over it to print each value.

# Example 5: Function with Arbitrary Keyword Arguments (**kwargs)
def print_person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_details(name="Alice", age=30, job="Engineer")  # Function call with keyword arguments

# Explanation:
# The `**kwargs` syntax allows the function to accept an arbitrary number of keyword arguments (key-value pairs).
# `kwargs` is treated as a dictionary, and we can iterate over the dictionary to print the key-value pairs.

# Example 6: Function Returning Multiple Values
def get_min_max(numbers):
    return min(numbers), max(numbers)  # Return the minimum and maximum values

min_val, max_val = get_min_max([1, 2, 3, 4, 5])  # Unpacking the returned tuple
print(f"Min: {min_val}, Max: {max_val}")

# Explanation:
# The function `get_min_max` returns two values (the minimum and maximum of a list).
# We unpack the returned tuple into two variables (`min_val` and `max_val`) and print them.

# Example 7: Lambda Function (Anonymous Function)
multiply = lambda x, y: x * y  # Lambda function to multiply two numbers
print(multiply(5, 3))  # Calling the lambda function

# Explanation:
# A lambda function is an anonymous function defined using the `lambda` keyword.
# It takes parameters `x` and `y` and returns their product. The function is assigned to the variable `multiply`, which can then be used to call the function.

# Example 8: Recursion - Function Calling Itself
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Calling the recursive function to calculate the factorial

# Explanation:
# The `factorial` function is defined recursively. It calls itself with a smaller value of `n` until it reaches the base case (`n == 0`).
# The result of each recursive call is multiplied to compute the factorial.

"""
Key Concepts:
1. **Function Definition**:
   - Use `def` to define a function in Python. Functions can take parameters and return values.

2. **Default Arguments**:
   - Functions can have default arguments. If an argument is not passed, the default value is used.

3. **Arbitrary Arguments**:
   - `*args`: Allows the function to accept any number of positional arguments (packed as a tuple).
   - `**kwargs`: Allows the function to accept any number of keyword arguments (packed as a dictionary).

4. **Returning Multiple Values**:
   - Functions can return multiple values using tuples. You can unpack them into separate variables.

5. **Lambda Functions**:
   - Lambda functions are anonymous functions that are defined in a single line using the `lambda` keyword. They are often used for short, throwaway functions.

6. **Recursion**:
   - A function can call itself (recursive function). This is often used in problems like calculating factorials or Fibonacci numbers.
"""