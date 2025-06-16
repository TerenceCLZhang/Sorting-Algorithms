def exchange_sort(arr):
    """
    Sorts a list in ascending order using the Exchange Sort algorithm.

    Exchange Sort works by repeatedly comparing each pair of elements and swapping them if they are out of order.

    Time Complexities:
    - Best: Ω(n²)
    - Average: Θ(n²)
    - Worst: O(n²)
    """

    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Swap if element after is greater than current element
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
            yield arr, [i], [j], list(range(i))