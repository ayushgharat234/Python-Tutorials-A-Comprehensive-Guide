def linear_search(arr: list[int], target: int):
    """
    Performs a linear search to find the target in the array.

    Linear Search is one of the simplest search algorithms. It works by 
    iterating through each element of the array from the beginning to the 
    end, checking if the current element matches the target value.

    This search method does not require the array to be sorted and checks 
    every element in the worst case, making it a versatile but potentially 
    inefficient algorithm for large datasets.

    Parameters:
        arr (list): A list (or array) of elements in which the search is performed.
        target (int or float): The element to search for within the array.

    Returns:
        int: The index of the target element if found, otherwise returns -1.

    Time Complexity:
        - Best Case: O(1), if the target is the first element in the array.
        - Worst Case: O(n), where n is the number of elements in the array, 
          if the target is the last element or not found at all.
    
    Space Complexity:
        - O(1): The space used is constant since no extra data structures 
          are used during the execution of the algorithm. Only a small number 
          of variables are allocated (for iteration and comparison).

    Algorithm Explanation:
    1. Start by iterating through the array from index 0 to n-1 (where n is the length of the array).
    2. Compare each element with the target.
    3. If a match is found, return the current index.
    4. If the loop finishes without finding the target, return -1.

    Edge Cases:
    1. **Target in the First or Last Element**: If the target is at the first 
       index (best case) or last index (worst case), the algorithm will handle 
       it correctly by returning the respective index.
    2. **Target Not Present**: If the target element does not exist in the array, 
       the algorithm will return -1 to signify that the element was not found.
    3. **Empty Array**: If the input array is empty, the algorithm will immediately 
       return -1 since there are no elements to search.
    4. **Array with Duplicate Elements**: The linear search will return the index 
       of the first occurrence of the target. For arrays with multiple instances 
       of the target element, the algorithm doesn't perform any specialized 
       operations like binary search and simply stops at the first match.

    Example Usage:
    ```python
    arr = [10, 20, 30, 40, 50]
    target = 30
    result = linear_search(arr, target)
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
    - **Binary Search**: If the array is sorted, binary search can be a more efficient alternative with a time complexity of O(log n). However, binary search requires the array to be sorted, whereas linear search does not.
    - **Jump Search**: Another alternative for sorted arrays that divides the array into blocks for faster search.
    - **Hashing**: Using hash maps to store elements for constant time lookups.

    """

    for i, element in enumerate(arr):
        if element == target:
            return i  # Target found, return index
    return -1  # Target not found