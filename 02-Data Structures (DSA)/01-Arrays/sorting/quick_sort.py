def partition(arr, low, high):
    """
    Partition the array for the Quick Sort algorithm.

    The partition function selects a pivot element from the array and rearranges the elements so that 
    all elements smaller than the pivot are on the left and all elements greater than the pivot are on the right.

    Parameters:
        arr (list): The list to be partitioned.
        low (int): The starting index of the array portion to be partitioned.
        high (int): The ending index of the array portion to be partitioned.

    Returns:
        int: The index of the pivot element after partitioning.

    **Time Complexity:**
    - O(n) for partitioning, where n is the number of elements being partitioned.

    **Space Complexity:**
    - O(1) as the partitioning is done in-place without using additional memory.
    """
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1  # Initialize the index of the smaller element

    for j in range(low, high):
        # If the current element is smaller or equal to the pivot, swap it to the left side
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at the index i + 1 to place it in its correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i + 1  # Return the partition index


def quick_sort_helper(arr, low, high):
    """
    Helper function to implement Quick Sort recursively.

    The function calls itself recursively to sort the elements in the left and right partitions after partitioning.

    Parameters:
        arr (list): The list to be sorted.
        low (int): The starting index of the array portion to be sorted.
        high (int): The ending index of the array portion to be sorted.

    **Time Complexity:**
    - Best and Average Case: O(n log n) if the pivot divides the array into nearly equal halves.
    - Worst Case: O(n^2) if the pivot is the smallest or largest element and the partitioning is unbalanced.

    **Space Complexity:**
    - O(log n) for the recursion stack in the best and average cases, due to the recursive calls.
    - O(n) in the worst case for recursion stack, if the array is already sorted or reverse sorted.
    """
    if low < high:
        # Find the partition index
        pi = partition(arr, low, high)
        
        # Recursively sort the left and right sub-arrays
        quick_sort_helper(arr, low, pi - 1)  # Sort the left part
        quick_sort_helper(arr, pi + 1, high)  # Sort the right part


def quick_sort(arr):
    """
    Quick Sort Algorithm:
    
    Quick Sort is a divide-and-conquer sorting algorithm. It works by selecting a pivot element from the 
    array and partitioning the array into two sub-arrays, one with elements smaller than the pivot and one with elements 
    larger than the pivot. These sub-arrays are then sorted recursively.

    **How Quick Sort Works:**
    1. Choose a pivot element (in this case, the last element in the array).
    2. Partition the array by rearranging elements so that elements smaller than the pivot are to the left, 
       and elements greater than the pivot are to the right.
    3. Recursively apply the above steps to the left and right partitions.

    **Time Complexity:**
    - Best Case: O(n log n), when the pivot divides the array into two nearly equal halves.
    - Worst Case: O(n^2), when the pivot is the smallest or largest element and the partitioning is unbalanced.
    - Average Case: O(n log n), the typical case for Quick Sort.

    **Space Complexity:**
    - O(log n) for the recursion stack in the best and average cases.
    - O(n) in the worst case due to recursion stack for very unbalanced partitions.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Example Usage:
    ```python
    arr = [64, 25, 12, 22, 11]
    quick_sort(arr)
    print("Sorted array:", arr)
    ```

    Output:
    ```
    Sorted array: [11, 12, 22, 25, 64]
    ```

    **Edge Cases:**
    1. **Empty Array:** If the input array is empty, the function will return the empty array.
    2. **Single Element Array:** If the array has only one element, no sorting is needed, and the array is returned as is.
    3. **Array with All Equal Elements:** The algorithm will perform the partitioning but won't make swaps. The array will remain unchanged.
    4. **Already Sorted Array:** The algorithm will still proceed with the partitioning, but the number of swaps will be minimal.

    **Algorithm Efficiency Considerations:**
    Quick Sort is efficient on large datasets, with an average time complexity of O(n log n). However, in the worst case, it can degrade to O(n^2), which is why it's important to choose a good pivot (e.g., using randomized pivot selection or the median-of-three rule) to minimize the chances of encountering the worst case.
    """
    quick_sort_helper(arr, 0, len(arr) - 1)