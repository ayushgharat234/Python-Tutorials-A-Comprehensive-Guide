def binary_search_recursive(arr, target, low, high):
    """
    Performs a recursive binary search to find the target in a sorted array.

    Binary Search is a divide-and-conquer algorithm that locates the position 
    of a target element within a sorted array. The recursive version repeatedly 
    divides the search space in half, narrowing down the potential position of the target 
    by calling the function on smaller and smaller sub-arrays until the target is found or 
    the search space is exhausted.

    Parameters:
        arr (list): A sorted list (or array) of elements in which the search is performed.
        target (int or float): The element to search for within the array.
        low (int): The starting index of the current search space.
        high (int): The ending index of the current search space.

    Returns:
        int: The index of the target element if found, otherwise returns -1.

    Time Complexity:
        - Best Case: O(1), if the target is the middle element of the current search space.
        - Worst Case: O(log n), where n is the number of elements in the array, 
          when the target is not found or lies at the end of the search space.

    Space Complexity:
        - O(log n): Since the algorithm uses recursion, each recursive call adds a new frame 
          to the call stack, leading to a space complexity of O(log n) due to the depth of the recursive calls.

    Algorithm Explanation:
    1. Base Case: If the `low` index is greater than the `high` index, the search space is empty, 
       and the target is not found, so return -1.
    2. Calculate the middle index: `mid = (low + high) // 2`.
    3. If the middle element equals the target, return the middle index.
    4. If the target is greater than the middle element, search the right half by recursively 
       calling the function with the new range: `low = mid + 1`.
    5. If the target is smaller than the middle element, search the left half by recursively 
       calling the function with the new range: `high = mid - 1`.
    6. The process repeats recursively until the target is found or the search space is exhausted.

    Edge Cases:
    1. **Target in the First or Last Element**: If the target is at the first or last position, 
       the recursive calls will eventually narrow down to that index.
    2. **Target Not Present**: If the target element does not exist in the array, the recursion 
       will eventually hit the base case and return -1.
    3. **Empty Array**: If the input array is empty, the first recursive call will immediately 
       return -1 as there is no element to search.
    4. **Array with Duplicate Elements**: Binary search returns the index of the first occurrence 
       of the target. If duplicates exist, it will find the first one due to the nature of the search.

    Example Usage:
    ```python
    arr = [10, 20, 30, 40, 50]
    target = 30
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found.")
    ```

    Output:
    ```
    Element 30 found at index 2.
    ```

    # Alternative Search Algorithms:
    - **Iterative Binary Search**: The iterative version of binary search uses a loop instead of recursion.
      While both algorithms have the same time and space complexity, the recursive version may use more space 
      due to the function call stack, making it less space-efficient.
    - **Linear Search**: Linear search does not require the array to be sorted and checks each element one by one.
      Its time complexity is O(n), making it slower for large arrays compared to binary search.
    - **Exponential Search**: Efficient for infinite or very large arrays, combining binary search with exponential growing intervals.
    - **Ternary Search**: Similar to binary search but splits the array into three parts instead of two.

    """

    if low > high:
        return -1  # Base case: target not found
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)  # Search in right half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)  # Search in left half