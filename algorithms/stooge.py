from algorithms.misc import finished_animation


def stooge_sort(arr):
    def stooge_sort_recursive(i, j):
        # If the first element is greater than the last, swap them
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, [i, j], []

        # If there are at least 3 elements, apply Stooge Sort recursively
        if j - i + 1 > 2:
            t = (j - i + 1) // 3

            # Recursively sort first 2/3
            yield from stooge_sort_recursive(i, j - t)

            # Recursively sort last 2/3
            yield from stooge_sort_recursive(i + t, j)

            # Recursively sort first 2/3 again
            yield from stooge_sort_recursive(i, j - t)

    yield from stooge_sort_recursive(0, len(arr) - 1)
    yield from finished_animation(arr)
