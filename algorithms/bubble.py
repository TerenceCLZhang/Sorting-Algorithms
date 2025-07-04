from algorithms.misc import finished_animation


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            yield arr, [j, j + 1], []

            # Swap if out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr, [j, j + 1], []

    yield from finished_animation(arr)
