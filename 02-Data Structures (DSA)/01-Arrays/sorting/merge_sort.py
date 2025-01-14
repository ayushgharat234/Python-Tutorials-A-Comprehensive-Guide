def merge(arr, left, mid, right):
    """
    Merge two sorted sub-arrays into a single sorted array.

    The merge function takes two sorted sub-arrays (left_half and right_half) and combines them into 
    a single sorted array, placing the elements in their correct order.

    Parameters:
        arr (list): The list containing the sub-arrays to be merged.
        left (int): The starting index of the left sub-array.
        mid (int): The midpoint index that divides the array into two halves.
        right (int): The ending index of the right sub-array.

    **Time Complexity:**
    - O(n), where n is the total number of elements being merged (left_half + right_half).

    **Space Complexity:**
    - O(n), as additional space is used to store the left and right halves of the array.
    """
    # Calculate the lengths of the two sub-arrays
    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays for the left and right halves
    left_half = arr[left: left + n1]
    right_half = arr[mid + 1: mid + n2 + 1]

    i = j = 0  # Initial indexes for left_half and right_half
    k = left  # Initial index for the main array

    # Merge the left and right halves in sorted order
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy remaining elements from the left_half, if any
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy remaining elements from the right_half, if any
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1


def merge_sort_helper(arr, left, right):
    """
    Helper function for the Merge Sort algorithm that recursively splits the array.

    The function divides the array into two halves, recursively sorts each half, 
    and merges them back together using the merge function.

    Parameters:
        arr (list): The list to be sorted.
        left (int): The starting index of the array portion to be sorted.
        right (int): The ending index of the array portion to be sorted.

    **Time Complexity:**
    - Best, Worst, and Average Case: O(n log n), where n is the number of elements in the array.

    **Space Complexity:**
    - O(n), as additional space is used for the recursive call stack and temporary sub-arrays.
    """
    if left < right:
        mid = (left + right) // 2  # Find the middle index
        merge_sort_helper(arr, left, mid)  # Recursively sort the left half
        merge_sort_helper(arr, mid + 1, right)  # Recursively sort the right half
        merge(arr, left, mid, right)  # Merge the two sorted halves


def merge_sort(arr):
    """
    Merge Sort Algorithm:

    Merge Sort is a divide-and-conquer sorting algorithm that divides the array into two halves, 
    recursively sorts each half, and then merges the sorted halves back together.

    **How Merge Sort Works:**
    1. Divide the array into two halves.
    2. Recursively sort each half by dividing them further until you have sub-arrays with a single element.
    3. Merge the sorted sub-arrays back together.

    **Time Complexity:**
    - Best, Worst, and Average Case: O(n log n), where n is the number of elements in the array. 
      This is because the array is divided into halves (log n divisions), and merging takes linear time (O(n)).

    **Space Complexity:**
    - O(n), because of the additional space used for the temporary sub-arrays in the merging process.

    Parameters:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Example Usage:
    ```python
    arr = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr)
    print("Sorted array:", arr)
    ```

    Output:
    ```
    Sorted array: [3, 9, 10, 27, 38, 43, 82]
    ```

    **Edge Cases:**
    1. **Empty Array:** If the input array is empty, the function will return the empty array.
    2. **Single Element Array:** If the array has only one element, it is already sorted and will be returned as is.
    3. **Array with All Equal Elements:** The algorithm will perform the merging, but no swaps or rearrangements will occur.

    **Algorithm Efficiency Considerations:**
    Merge Sort is highly efficient with a time complexity of O(n log n) for both the best, worst, and average cases. However, it has a space complexity of O(n), which means it uses additional memory for the temporary arrays during the merging process. Despite this, it is a stable sorting algorithm, making it useful for certain types of data.
    """
    merge_sort_helper(arr, 0, len(arr) - 1)
    return arr