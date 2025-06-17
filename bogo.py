import random

def bogo_sort(arr):
    """
    Sorts a list in ascending order using the Bogo Sort algorithm.
    
    Bogo Sort repeatedly shuffles the list until it happens to be sorted.

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
            break

        random.shuffle(arr)
        yield arr,  [i for i in range(1, len(arr)) if arr[i] < arr[i - 1]], [], []  # Show bad positions after shuffling


def bozo_sort(arr):
    """
    Sorts a list in ascending order using the Bozo Sort algorithm.
    
    Bozo Sort repeatedly swaps two randomly chosen elements in the list 
    and checks if the list is sorted. It continues until the list is sorted.

    Time Complexities:
    - Best: Ω(n)
    - Average: Θ(n!)
    - Worst: O(∞)
    """

    is_sorted = False
    while not is_sorted:
        # Check if sorted
        is_sorted = all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))
        if is_sorted:
            break

        # Find the two random indexes
        i, j = random.sample(range(len(arr)), 2)
        arr[i], arr[j] = arr[j], arr[i]
        yield arr, [i], [j], []