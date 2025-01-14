def insertion_sort(arr: list[int]) -> list[int]:
    """
    Insertion Sort Algorithm:

    Insertion Sort builds a sorted array one element at a time by inserting each element into its correct position.
    It iterates through the array from the second element to the last, comparing the current element with the 
    elements before it and shifting the larger elements to the right to make space for the current element.

    **How Insertion Sort Works:**
    1. Start from the second element in the array (the element at index 1).
    2. Compare this element with the element before it.
    3. If the current element is smaller, shift the larger elements to the right to make space.
    4. Insert the current element into its correct position.
    5. Move to the next element and repeat the process until the entire array is sorted.

    **Time Complexity:**
    - Best Case: O(n), when the array is already sorted. Only one comparison is needed for each element, so the algorithm runs in linear time.
    - Worst Case: O(n^2), when the array is sorted in reverse order. This results in the maximum number of comparisons and shifts.

    **Space Complexity:**
    - O(1), as Insertion Sort is an in-place sorting algorithm, meaning it only uses a constant amount of extra memory.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Example Usage:
    ```python
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)
    ```

    Output:
    ```
    Sorted array: [11, 12, 22, 25, 34, 64, 90]
    ```

    **Edge Cases:**
    1. **Empty Array:** If the input array is empty, the function will return the empty array.
    2. **Single Element Array:** If the input array has only one element, no sorting is needed, 
       and the function will return the array as is.
    3. **Array with All Equal Elements:** If all the elements in the array are the same, 
       the algorithm will run efficiently and only make the necessary comparisons.
    4. **Reverse Sorted Array:** The worst-case scenario occurs when the array is sorted in reverse order. 
       In this case, the algorithm will perform the maximum number of shifts.

    **Algorithm Efficiency Considerations:**
    While Insertion Sort is more efficient than Bubble Sort for small datasets, its worst-case time complexity of O(n^2) makes it inefficient 
    for large datasets compared to more advanced sorting algorithms such as Merge Sort or Quick Sort, which have average 
    time complexities of O(n log n).
    """

    # Iterate through each element of the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i - 1  # The index of the previous element
        
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Shift the larger element to the right
            j -= 1  # Move to the previous element
        
        # Insert the current element (key) into its correct position
        arr[j + 1] = key

    return arr