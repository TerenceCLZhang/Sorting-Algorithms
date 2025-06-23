from algorithms.misc import finished_animation


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume current index is the minimum

        # Find the actual minimum element in the unsorted part
        for j in range(i + 1, n):
            yield arr, [i, min_idx, j], []
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update min index if a smaller element is found

        # Swap if a new minimum was found
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    yield from finished_animation(arr)
