def comb_sort(arr):
    """
    Sorts a list in ascending order using the Comb Sort algorithm.

    Comb Sort improves on Bubble Sort by eliminating small values near the end of the list early on.
    It works by repeatedly comparing and swapping elements that are a certain 'gap' apart.
    The gap starts as the length of the list and shrinks by a shrink factor (typically 1.3) each pass,
    until it reaches 1. At that point, it behaves like Bubble Sort.

    Time Complexities:
    - Best: Ω(n log n)
    - Average: Θ(n²)
    - Worst: O(n²)
    """
    n = len(arr)
    gap = n
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        # Find next gap
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True
        elif gap == 9 or gap == 10:
            gap = 11
        
        # Single comb over the list
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                is_sorted = False

            yield arr, [i], [i + gap], []
            i += 1