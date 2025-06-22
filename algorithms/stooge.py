from algorithms.misc import finished_animation


def stooge_sort(arr):
    def stooge_sort_recursive(i, j):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, [i, j], []
        if j - i + 1 > 2:
            t = (j - i + 1) // 3
            yield from stooge_sort_recursive(i, j - t)
            yield from stooge_sort_recursive(i + t, j)
            yield from stooge_sort_recursive(i, j - t)

    yield from stooge_sort_recursive(0, len(arr) - 1)
    yield from finished_animation(arr)
