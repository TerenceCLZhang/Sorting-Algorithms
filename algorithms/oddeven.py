from misc import finished_animation


def odd_even_sort(arr):
    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        # Odd indexes
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

            yield arr, [i, i + 1], []

        # Even indexes
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

            yield arr, [i, i + 1], []

    yield from finished_animation(arr)
