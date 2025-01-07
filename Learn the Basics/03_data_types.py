"""
Data Types in Python:
Python provides various data types to store different kinds of data.
Below are the most commonly used data types.
"""

# Example 1: Numeric Data Types
# Integer
int_var = 10  # Integer type
print(f"Integer: {int_var}, Type: {type(int_var)}")  # Type: int

# Float
float_var = 20.5  # Floating-point type
print(f"Float: {float_var}, Type: {type(float_var)}")  # Type: float

# Complex
complex_var = 3 + 4j  # Complex number type
print(f"Complex: {complex_var}, Type: {type(complex_var)}")  # Type: complex

# Explanation:
# - Integer (`int`) represents whole numbers (positive, negative, or zero).
# - Float (`float`) represents real numbers with decimal points.
# - Complex (`complex`) represents complex numbers in the form a + bj, where a and b are real numbers.

# Example 2: String Data Type
string_var = "Python Programming"  # String type
print(f"String: {string_var}, Type: {type(string_var)}")  # Type: str

# Explanation:
# - String (`str`) is a sequence of characters enclosed in quotes (single, double, or triple quotes).

# Example 3: Boolean Data Type
bool_var = True  # Boolean type (can be True or False)
print(f"Boolean: {bool_var}, Type: {type(bool_var)}")  # Type: bool

# Explanation:
# - Boolean (`bool`) represents a value that can either be True or False.

# Example 4: Sequence Data Types
# List
list_var = [1, 2, 3, "Python", True]  # List can store mixed data types
print(f"List: {list_var}, Type: {type(list_var)}")  # Type: list

# Tuple
tuple_var = (1, 2, 3, "Python", True)  # Tuple is immutable
print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")  # Type: tuple

# Range
range_var = range(1, 10, 2)  # A range object
print(f"Range: {list(range_var)}, Type: {type(range_var)}")  # Type: range

# Explanation:
# - List (`list`) is a mutable collection that can store multiple items of different data types.
# - Tuple (`tuple`) is similar to a list but immutable (cannot be changed after creation).
# - Range (`range`) represents a sequence of numbers and is often used in loops.

# Example 5: Dictionary Data Type
# Dictionary stores key-value pairs
dict_var = {"name": "Python", "type": "Programming Language", "version": 3.10}
print(f"Dictionary: {dict_var}, Type: {type(dict_var)}")  # Type: dict

# Explanation:
# - Dictionary (`dict`) stores data in key-value pairs, allowing quick lookups by key.

# Example 6: Set Data Type
# Set stores unique values
set_var = {1, 2, 3, 3, 4}  # Duplicates will be removed
print(f"Set: {set_var}, Type: {type(set_var)}")  # Type: set

# Explanation:
# - Set (`set`) is an unordered collection of unique values (duplicates are automatically removed).

# Example 7: None Data Type
none_var = None  # Represents the absence of a value
print(f"None: {none_var}, Type: {type(none_var)}")  # Type: NoneType

# Explanation:
# - `None` is used to represent the absence of a value or a null value in Python.

# Example 8: Type Conversion
# Convert one data type to another using built-in functions
int_to_float = float(int_var)  # Convert integer to float
print(f"Converted Integer to Float: {int_to_float}, Type: {type(int_to_float)}")  # Type: float

float_to_int = int(float_var)  # Convert float to integer
print(f"Converted Float to Integer: {float_to_int}, Type: {type(float_to_int)}")  # Type: int

string_to_list = list(string_var)  # Convert string to list
print(f"Converted String to List: {string_to_list}, Type: {type(string_to_list)}")  # Type: list

# Explanation:
# - Python provides built-in functions for type conversion, such as `float()`, `int()`, and `list()`.
# - The conversion from one data type to another is common in data processing or mathematical operations.

# Example 9: Mutable vs Immutable Data Types
# Mutable (can be changed after creation)
mutable_list = [1, 2, 3]
mutable_list[0] = 10  # Modify the first element
print(f"Modified List: {mutable_list}")  # List is mutable, modification is allowed

# Immutable (cannot be changed after creation)
immutable_tuple = (1, 2, 3)
# Uncommenting the next line will raise an error:
# immutable_tuple[0] = 10  # Tuples are immutable, raising an error

# Explanation:
# - Mutable data types (e.g., list, dictionary, set) can be changed after creation.
# - Immutable data types (e.g., tuple, string) cannot be modified once created.

# Example 10: Checking Data Types Using `isinstance()`
print(f"Is int_var an int? {isinstance(int_var, int)}")  # Checks if int_var is of type int
print(f"Is string_var a str? {isinstance(string_var, str)}")  # Checks if string_var is of type str