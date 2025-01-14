"""
File Handling in Python:

File handling is used to read and write data to files.
- The `open()` function is used to open a file and returns a file object.
- The `read()`, `write()`, `close()` methods are used to manipulate the content of the file.
- The `with` statement is used to open a file and ensure proper resource management, automatically closing the file when done.
"""

# Example 1: Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")  # Writing text to the file

# Explanation:
# The 'w' mode opens the file in write mode. If the file doesn't exist, it is created. If the file exists, its content is overwritten.
# Here, we write a string into the file.

# Example 2: Reading from a file
with open("example.txt", "r") as file:
    content = file.read()  # Reading the entire content of the file
    print(content)  # Output: Hello, this is a test file.

# Explanation:
# The 'r' mode opens the file in read mode. If the file doesn't exist, a FileNotFoundError is raised.
# We read the content of the file using the read() method, which returns the content as a string.

# Example 3: Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAdding more content.")  # Appending text to the file

# Explanation:
# The 'a' mode opens the file in append mode. If the file doesn't exist, it is created.
# If the file exists, the new content is added at the end without overwriting the existing data.

# Example 4: File not found exception handling
try:
    with open("non_existing_file.txt", "r") as file:
        print(file.read())  # Trying to read from a non-existing file
except FileNotFoundError:
    print("File not found!")  # Handling the exception if the file doesn't exist

# Explanation:
# The try-except block is used to handle errors like FileNotFoundError when trying to open a file that does not exist.
# If the file is not found, the program catches the exception and prints an error message.

# Example 5: Reading file line by line
with open("example.txt", "r") as file:
    lines = file.readlines()  # Reading all lines in the file as a list
    for line in lines:
        print(line.strip())  # Printing each line without extra newline characters

# Explanation:
# The readlines() method reads the file line by line and stores each line in a list.
# We use strip() to remove leading and trailing whitespaces (like newlines) from each line before printing.

# Example 6: Writing multiple lines to a file
lines_to_write = ["Line 1: This is the first line.\n", "Line 2: This is the second line.\n", "Line 3: This is the third line.\n"]
with open("example.txt", "w") as file:
    file.writelines(lines_to_write)  # Writing multiple lines to the file

# Explanation:
# The writelines() method writes a list of strings to the file. Each string is written as a separate line in the file.
# Each item in the list must already contain a newline character ('\n') if you want separate lines.

# Example 7: File pointer manipulation (seek and tell)
with open("example.txt", "r") as file:
    file.seek(5)  # Move the file pointer to position 5
    content = file.read(10)  # Read the next 10 characters
    print(content)  # Output: ', this is'

    file.seek(0)  # Move the file pointer back to the beginning
    print(file.tell())  # Output: 0 (Current file pointer position)

# Explanation:
# The seek() method moves the file pointer to a specified position. It is useful when you want to read a specific part of the file.
# The tell() method returns the current position of the file pointer.

# Example 8: Context Manager for File Handling
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Explanation:
# Using the `with` statement to open a file ensures that the file is properly closed even if an error occurs during reading.
# It's a more efficient and reliable way to handle file operations compared to manually opening and closing the file.

# Example 9: Writing Binary Data to a File
with open("example_binary.bin", "wb") as file:
    file.write(b"Binary data: \x01\x02\x03\x04")  # Writing binary data to the file

# Explanation:
# The 'wb' mode opens the file in binary write mode. Data is written as bytes (using a byte string with a leading 'b').
# This is useful for working with non-text files such as images, audio files, or other binary data.

# Example 10: Reading Binary Data from a File
with open("example_binary.bin", "rb") as file:
    content = file.read()
    print(content)  # Output: b'Binary data: \x01\x02\x03\x04'

# Explanation:
# The 'rb' mode opens the file in binary read mode. The read() method reads the binary data, which is returned as bytes.
# This is useful when you need to process binary files like images or compressed files.

# Example 11: File Handling with CSV Files
import csv

# Writing to a CSV file
data = [["Name", "Age", "City"], ["John", 28, "New York"], ["Jane", 22, "London"]]
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Writing rows of data to the CSV file

# Reading from a CSV file
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Explanation:
# The `csv` module is used for reading and writing CSV (Comma-Separated Values) files.
# The writerow() method is used to write a single row, and writerows() writes multiple rows to the file.
# The reader() method is used to read data from a CSV file, where each row is returned as a list.