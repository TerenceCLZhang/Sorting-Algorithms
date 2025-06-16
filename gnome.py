def gnome_sort(arr):
    """
    Sorts a list in ascending order using the Gnome Sort algorithm.

    Gnome Sort works by comparing adjacent elements, similar to Insertion Sort.
    If elements are in the correct order, it moves forward; if not, it swaps them and steps back.
    This process continues until the list is sorted.

    Time Complexities:
    - Best: Ω(n)
    - Average: Θ(n^2)
    - Worst: O(n^2)
    """
    i = 0
    while i < len(arr):
        # If current element is larger or equal than previous element move to next element
        if i == 0 or arr[i] >= arr[i - 1]:
            yield arr, [i], [], []
            i += 1
        # Otherwise, swap elements and go back one element
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            yield arr, [], [i], []
            i -= 1