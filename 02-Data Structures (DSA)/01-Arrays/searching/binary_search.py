def binary_search(arr, target):
    """
    Performs an iterative binary search to find the target in a sorted array.

    Binary Search is a divide-and-conquer algorithm that efficiently locates 
    the position of a target element within a sorted array by repeatedly 
    dividing the search interval in half. The algorithm compares the target 
    with the middle element of the array and eliminates half of the search 
    space with each comparison.

    Binary search is much faster than linear search, especially for large datasets, 
    as it reduces the search space logarithmically.

    Parameters:
        arr (list): A sorted list (or array) of elements in which the search is performed.
        target (int or float): The element to search for within the array.

    Returns:
        int: The index of the target element if found, otherwise returns -1.

    Time Complexity:
        - Best Case: O(1), if the target is the middle element of the array.
        - Worst Case: O(log n), where n is the number of elements in the array, 
          when the target is not present or lies at the end of the search space.

    Space Complexity:
        - O(1): The algorithm operates in constant space as only a small number 
          of variables are used for tracking the indices (`low`, `high`, `mid`).

    Algorithm Explanation:
    1. Initialize two pointers: `low` (the start of the array) and `high` (the end of the array).
    2. While the `low` pointer is less than or equal to the `high` pointer:
       a. Calculate the middle index: `mid = (low + high) // 2`.
       b. If the middle element equals the target, return the index `mid`.
       c. If the target is greater than the middle element, adjust the `low` pointer to `mid + 1` to search the right half.
       d. If the target is smaller than the middle element, adjust the `high` pointer to `mid - 1` to search the left half.
    3. If the loop terminates without finding the target, return -1 to indicate the target is not in the array.

    Edge Cases:
    1. **Target in the First or Last Element**: If the target is at the first or last position, binary search will still find it in O(log n) time.
    2. **Target Not Present**: If the target element does not exist in the array, the algorithm will return -1 after narrowing down the search space.
    3. **Empty Array**: If the input array is empty, binary search will immediately return -1 since the search space is non-existent.
    4. **Array with Duplicate Elements**: Binary search returns the index of the first occurrence of the target. If duplicates exist, the algorithm does not handle returning all occurrences.

    Example Usage:
    ```python
    arr = [10, 20, 30, 40, 50]
    target = 30
    result = binary_search(arr, target)
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
    - **Linear Search**: Linear search does not require the array to be sorted and checks each element one by one. Its time complexity is O(n), making it slower for large arrays compared to binary search.
    - **Exponential Search**: An efficient search method for infinite or large-sized sorted arrays. It combines binary search with an exponentially growing search space.
    - **Ternary Search**: Similar to binary search but splits the array into three parts rather than two. It can sometimes be faster, but it's not as commonly used.

    """

    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if arr[mid] == target:
            return mid   # Target found 
        elif arr[mid] < target:
            low = mid + 1  # Search in the right-half
        else:
            high = mid - 1 # Search in the left-half

    return -1  # Target not found