def selection_sort(arr):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Selection Sort works by dividing the list into a sorted and an unsorted region. 
    It repeatedly selects the smallest (or largest, depending on sorting order) element 
    from the unsorted region and swaps it with the first unsorted element, thereby expanding 
    the sorted region by one and shrinking the unsorted region.

    Time Complexities:
    - Best: Ω(n^2)
    - Average: Θ(n^2)
    - Worst: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            yield arr, list(range(i)), [min_idx], [j] 
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != 1:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

