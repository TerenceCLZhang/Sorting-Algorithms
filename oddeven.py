def odd_even_sort(arr):
    """
    Sorts a list in ascending order using the Odd-Even Sort algorithm.

    Odd-Even Sort (Brick Sort) works by repeatedly performing two phases:
    - In the odd phase, it compares and swaps elements at odd-even indexed pairs (1-2, 3-4, etc.).
    - In the even phase, it compares and swaps elements at even-odd indexed pairs (0-1, 2-3, etc.).
    This process continues until the list is sorted.

    Time Complexities:
    - Best: Ω(n)
    - Average: Θ(n²)
    - Worst: O(n²)
    """

    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True # Assume array is sorted

        # Odd indexes
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
            yield arr, [i, i + 1], [], []
        
        # Even indexes
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
            yield arr, [], [i, i + 1], []