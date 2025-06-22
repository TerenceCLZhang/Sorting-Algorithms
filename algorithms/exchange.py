from algorithms.misc import finished_animation


def exchange_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
            yield arr, [i, j], []

    yield from finished_animation(arr)
