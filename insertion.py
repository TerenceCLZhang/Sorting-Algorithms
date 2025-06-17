def insertion_sort(arr):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Insertion Sort builds the sorted list one element at a time by repeatedly 
    taking the next unsorted element and inserting it into its correct position 
    within the already sorted portion of the list.

    Time Complexities:
    - Best: Ω(n)
    - Average: Θ(n^2)
    - Worst: O(n^2)
    """
    for i in range(1, len(arr)):
        j = i
        # If previous element greater than current element swap
        while j > 0 and arr[j - 1] > arr[j]:
            yield arr, [i], [j], []
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        yield arr, [i], [], [j]
        i += 1


def binary_insertion_sort(arr):
    """
    Sorts a list in ascending order using the Binary Insertion Sort algorithm.

    Binary Insertion Sort improves upon standard Insertion Sort by using binary search 
    to find the correct location to insert the current element, reducing the number 
    of comparisons. However, the number of shifts (data movements) remains the same 
    as in regular Insertion Sort.

    Time Complexities:
    - Best: Ω(n log n)
    - Average: Θ(n^2)
    - Worst: O(n^2)
    """
    def binary_search(arr, key):
        """
        Returns index of where key should be in an array.
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr[:i], key)
        yield arr, list(range(i)), [j], [i]
        arr[:len(arr)] = arr[:j] + [key] + arr[j:i] + arr[i + 1:]