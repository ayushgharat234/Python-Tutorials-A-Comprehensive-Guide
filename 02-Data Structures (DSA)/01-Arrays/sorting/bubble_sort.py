def bubble_sort(arr: list[int]) -> list[int]:
    """
    Bubble Sort Algorithm:

    Bubble Sort is a simple sorting algorithm that repeatedly steps through the array,
    compares adjacent elements, and swaps them if they are in the wrong order. 
    The pass through the array is repeated until the array is sorted.

    **How Bubble Sort Works:**
    1. Start from the beginning of the array.
    2. Compare the current element with the next element.
    3. If the current element is larger than the next element, swap them.
    4. Continue this process for each adjacent pair in the array.
    5. After one full pass through the array, the largest element will have "bubbled" up to the correct position at the end.
    6. Repeat this process for the rest of the array (ignoring the last element that is already in place).
    7. The process continues until no swaps are needed, indicating that the array is sorted.

    **Time Complexity:**
    - Best Case: O(n), when the array is already sorted. In this case, only one pass is required and no swaps will be made, 
      so the algorithm will exit early after detecting no swaps.
    - Worst Case: O(n^2), when the array is sorted in reverse order. This results in the maximum number of comparisons and swaps.

    **Space Complexity:**
    - O(1), as Bubble Sort is an in-place sorting algorithm, meaning it only uses a constant amount of extra memory.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Example Usage:
    ```python
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
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
       the algorithm will terminate after the first pass, as no swaps will occur.
    4. **Reverse Sorted Array:** The worst-case scenario occurs when the array is sorted in reverse order. 
       In this case, the algorithm will perform the maximum number of swaps in each pass.

    **Algorithm Efficiency Considerations:**
    While Bubble Sort is easy to understand and implement, its worst-case time complexity of O(n^2) makes it inefficient 
    for large datasets compared to more advanced sorting algorithms such as Merge Sort or Quick Sort, which have average 
    time complexities of O(n log n).
    """

    # Get the length of the array
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Flag to check if any swapping occurred in this pass
        swapped = False

        # Last i elements are already in place, so no need to check them
        for j in range(0, n-i-1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swapping occurred, the array is already sorted, so break out of the loop
        if not swapped:
            break

    return arr