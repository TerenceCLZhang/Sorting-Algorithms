def bubble_sort(arr):
    """
    Sorts a list in ascending order using the Bubble Sort algorithm.

    Bubble Sort works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if 
    they are in the wrong order, causing larger elements to "bubble" to the end with each pass.

    Time Complexities:
    - Best: Ω(n²)
    - Average: Θ(n²)
    - Worst: O(n²)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            # Swap if current element is larger than next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr, [j, j + 1], [], list(range(n - i, n))

def optimized_bubble_sort(arr):
    """
    Sorts a list in ascending order using an optimized Bubble Sort algorithm.

    This version of Bubble Sort includes an optimisation that stops the algorithm 
    early if no swaps are made during a full pass, indicating that the list is already sorted.

    Time Complexities:
    - Best: Ω(n)
    - Average: Θ(n²)
    - Worst: O(n²)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            # Swap if current element is larger than next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            yield arr, [j, j + 1], [], list(range(n - i, n))
        
        if not swapped:
            break