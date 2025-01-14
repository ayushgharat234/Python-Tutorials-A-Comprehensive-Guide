class DynamicArray:
    """
    A class to simulate a dynamic array with memory management features.
    Supports operations like append, remove, resize, and access.

    Key Features and Improvements:
    - Dynamic Resizing: Automatically resizes when capacity is exceeded, using a doubling strategy for efficiency.
    - Element Removal: Allows removal of elements while preserving the order of the remaining elements.
    - Access: Provides safe access to elements with bounds checking.
    - Memory Simulation: Simulates memory allocation with None for unused blocks.
    - Debugging Support: Includes a memory layout print function for visualization.

    Use Cases:
    - Understanding dynamic arrays in Python.
    - Learning memory management concepts.
    - Simulating low-level array behaviors in higher-level languages.
    """

    def __init__(self, initial_capacity: int = 4):
        """
        Initializes the dynamic array with a given capacity.
        
        Args:
            initial_capacity (int): The initial capacity of the dynamic array. Default is 4.
        """
        self.array = [None] * initial_capacity  # Allocating memory blocks
        self._capacity = initial_capacity  # Total memory capacity
        self.size = 0  # Number of elements currently in the array

    def append(self, value: int):
        """
        Adds a new element to the array. Resizes the array if the capacity is exceeded.
        
        Args:
            value (int): The value to append to the array.
        
        Time Complexity:
        - O(1) on average due to amortized resizing cost.
        - O(n) in worst-case when resizing occurs.
        """
        if self.size == self._capacity:
            self._resize(self._capacity * 2)  # Double the capacity when full
        self.array[self.size] = value
        self.size += 1

    def _resize(self, new_capacity: int):
        """
        Resizes the array to a new capacity, preserving existing elements.
        
        Args:
            new_capacity (int): The new capacity for the array.
        
        Time Complexity: O(n), where n is the number of elements in the array.
        """
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self._capacity = new_capacity

    def remove(self, value: int):
        """
        Removes the first occurrence of the specified value from the array.
        Shifts elements to fill the gap.
        
        Args:
            value (int): The value to remove from the array.
        
        Raises:
            ValueError: If the value is not found in the array.
        
        Time Complexity: O(n), where n is the number of elements in the array.
        """
        for i in range(self.size):
            if self.array[i] == value:
                self._shift_left(i)
                return
        raise ValueError(f"Value {value} not found in the array.")

    def _shift_left(self, index: int):
        """
        Shifts elements to the left from the specified index.
        
        Args:
            index (int): The index to start shifting from.
        
        Time Complexity: O(n), where n is the number of elements after the index.
        """
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def access(self, index: int) -> int:
        """
        Accesses the element at the specified index.
        
        Args:
            index (int): The index of the element to access.
        
        Returns:
            int: The value at the specified index.
        
        Raises:
            IndexError: If the index is out of range.
        
        Time Complexity: O(1).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range.")
        return self.array[index]

    def __str__(self):
        """
        Returns a string representation of the array.
        
        Returns:
            str: The string representation of the array's elements.
        
        Example:
            [10, 20, 30]
        """
        return str([self.array[i] for i in range(self.size)])

    def capacity(self) -> int:
        """
        Returns the current capacity of the array.
        
        Returns:
            int: The capacity of the array.
        
        Time Complexity: O(1).
        """
        return self._capacity

    def print_memory(self):
        """
        Prints the memory layout of the array, showing used and unused blocks.
        
        Example:
            Memory Layout: [10] [20] [30] [None]
        """
        grid = [f"[{self.array[i]}]" if i < self.size else "[None]" for i in range(self._capacity)]
        print("Memory Layout:", " ".join(grid))

# Example usage
if __name__ == "__main__":
    # Initialize a dynamic array
    dyn_array = DynamicArray(initial_capacity=4)

    # Append elements
    dyn_array.append(10)
    dyn_array.append(20)
    dyn_array.append(30)
    dyn_array.append(40)

    # Print the array
    print("Array:", dyn_array)  # Output: [10, 20, 30, 40]

    # Access an element
    print("Access index 2:", dyn_array.access(2))  # Output: 30

    # Remove an element
    dyn_array.remove(20)
    print("Array after removal:", dyn_array)  # Output: [10, 30, 40]

    # Append more elements to trigger resize
    dyn_array.append(50)
    dyn_array.append(60)
    print("Array after resize:", dyn_array)  # Output: [10, 30, 40, 50, 60]

    # Check capacity
    print("Current capacity:", dyn_array.capacity())  # Output: 8

    # Printing the memory 
    dyn_array.print_memory()