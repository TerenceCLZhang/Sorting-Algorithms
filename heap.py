
def heap_sort(arr):
    """
    Sorts a list in ascending order using the Heap Sort algorithm.

    Heap Sort works by first building a max-heap from the input list. It then repeatedly swaps the first element 
    (the largest) with the last unsorted element and reduces the heap size, maintaining the max-heap property 
    after each swap.

    Time Complexities:
    - Best: Ω(n log n)
    - Average: Θ(n log n)
    - Worst: O(n log n)
    """
    def heapify(arr, n, i):
        """
        Maintains the max-heap property for the subtree rooted at index i.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Update largest if left child exists and is larger than largest
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Update largest if the right child exists and is larger than largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Swap if different
        if largest != i:
            yield arr, list(range(n)), [largest], [i]
            arr[i], arr[largest] = arr[largest], arr[i]
            yield from heapify(arr, n, largest)


    def build_max_heap(arr):
        """
        Builds a max-heap from an unordered array.
        """
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(arr, n, i)


    n = len(arr)
    yield from build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # Swap first and last elements
        yield from heapify(arr, i, 0) # Update max heap