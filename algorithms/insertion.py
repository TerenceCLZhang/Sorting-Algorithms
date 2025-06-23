from algorithms.misc import finished_animation


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i

        # Move arr[i] leftward to its correct sorted position
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            yield arr, [i, j - 1, j], []
            j -= 1

        yield arr, [i], []

    yield from finished_animation(arr)
