def selection_sort(arr: list[int]) -> list[int]:
    """
    Selection Sort Algorithm:

    Selection Sort is an in-place comparison-based sorting algorithm that repeatedly selects the smallest element
    from the unsorted portion of the array and swaps it with the first unsorted element. This process continues until 
    the array is completely sorted.

    **How Selection Sort Works:**
    1. Start by assuming the first element in the array is the smallest.
    2. Traverse the remaining unsorted portion of the array to find the actual smallest element.
    3. Swap the smallest element with the first element of the unsorted portion.
    4. Move the boundary of the sorted and unsorted portions of the array by one position to the right.
    5. Repeat this process until all elements are sorted.

    **Time Complexity:**
    - **Best Case:** O(n^2), as Selection Sort always performs the same number of comparisons regardless of the array’s initial order.
    - **Worst Case:** O(n^2), as the algorithm still requires O(n^2) comparisons even if the array is sorted in reverse order.

    **Space Complexity:**
    - O(1), as Selection Sort is an in-place sorting algorithm, meaning it does not require additional memory apart from the array being sorted.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Example Usage:
    ```python
    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
    ```

    Output:
    ```
    Sorted array: [11, 12, 22, 25, 64]
    ```

    **Edge Cases:**
    1. **Empty Array:** If the input array is empty, the function will return the empty array.
    2. **Single Element Array:** If the input array has only one element, no sorting is needed, and the function will return the array as is.
    3. **Array with All Equal Elements:** If all elements are equal, the algorithm will perform the comparisons but no swaps, efficiently returning the input array as the sorted one.
    4. **Reverse Sorted Array:** The worst-case scenario occurs when the array is sorted in reverse order. In this case, the algorithm will still perform O(n^2) comparisons and swaps.

    **Algorithm Efficiency Considerations:**
    While Selection Sort has O(n^2) time complexity in all cases, it is less efficient than algorithms like Quick Sort or Merge Sort for large datasets. However, it has the advantage of a constant O(1) space complexity and is easy to implement.
    """

    # Traverse through the entire array
    for i in range(len(arr)):
        min_idx = i  # Assume the current element is the smallest
        
        # Find the smallest element in the remaining unsorted portion
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the index of the smallest element
        
        # Swap the found smallest element with the first element of the unsorted portion
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr