import random

def bogosort(arr):
    """
    Sorts a list in ascending order using the Bogosort algorithm.
    
    Bogosort repeatedly shuffles the list until it happens to be sorted.

    Time Complexities:
    - Best: Ω(n)
    - Average: Θ(n × n!)
    - Worst: O(∞)
    """

    is_sorted = False
    while not is_sorted:
        # Check if sorted
        is_sorted = all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))
        if is_sorted:
            yield arr, [], [], list(range(len(arr)))
            break

        random.shuffle(arr)
        yield arr,  [i for i in range(1, len(arr)) if arr[i] < arr[i - 1]], [], []  # Show bad positions after shuffling
