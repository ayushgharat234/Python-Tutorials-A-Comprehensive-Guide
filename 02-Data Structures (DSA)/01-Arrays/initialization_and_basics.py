"""
# Overview
An array is a data structure consisting of a collection of elements, each identified by an index or key. 
Arrays store elements in contiguous memory locations, making access to any element extremely efficient. 
Arrays are ideal for scenarios where random access and efficient traversal are essential.

## Key Characterisitics 
1. Linear Collection: The elements are stored in a sequential manner.
2. Indexed Acess: Each element is associated with an index, starting from 0 in most programming languages.
3. Fixed Size V/S Dynamic Size:
    - Static Array: Fixed size, determined during initialization (e.g., arrays in C)
    - Dynamic Array: Can grow or shrink in size (e.g., Python's list, Java's ArrayList)
 """

## Array Operations in Python

### 1. Initialization: "Declaring sn array (or list) and populating it with elements"

arr = [10, 20, 30, 40, 50]  # Initializing an array with predefined elements

empty_Arr = []  # Initializing an empty array

# Initializing an array with default values
n = 5  # Length of the array
default_Arr = [0]*n  # [0, 0, 0, 0, 0]

# Printing the array
print("Array:", arr)


### 2. Traversal: "Accessing each element of the array sequentially."
# Traversing the array and printing elements
arr = [10, 20, 30, 40, 50]
print("Array elements:")
for element in arr:  # Time Complexity of Traversal is O(n) or Linear Time Complexity
    print(element, end=" ")


### 3. Accessing Elements in an array: "etrieving an element at a specific index."
# Accesing elements using indices
arr =[10, 20, 30, 40, 50]   # Time Complexity of accessing is O(1)
print("Element at index 2:", arr[2])  # 30


### 4. Insertion: "Adding elements to the array at specific positions"
# Time Complexity of insertion is O(n) (due to shifting elements).

# Inserting an element at a specific index
arr = [10, 20, 30, 40, 50]
arr.insert(2, 25)  # Insert 25 at index 2
print("Array after insertion:", arr)   # [10, 20, 25, 30, 40, 50]

# Appending an element at the end
arr.append(60)
print("Array after appending:", arr)   # [10, 20, 25, 30, 40, 50, 60]


### 5. Deletion: Removing the elements from the array 
# Time Complexity: O(n) (due to shifting elements)

# Deleting an element at a specific index
arr = [10, 20, 30, 40, 50]  
arr.pop(2)  # Removes the element at index 2 (30)
print("Array after the deletion:", arr)  # [10, 20, 40, 50]

# Removing a specific element by value
arr.remove(40)  # Renoves the first occurence of 40
print("Array after rmeoving 40:", arr)  # [10, 20, 50]