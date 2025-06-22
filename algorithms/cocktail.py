from algorithms.misc import finished_animation


def cocktail_shaker_sort(arr):
    n = len(arr)
    is_sorted = False
    start, end = 0, n - 1

    while not is_sorted:
        is_sorted = True

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

            yield arr, [i, i + 1], []

        # Update end
        end -= 1

        # Check if sorted
        if is_sorted:
            break

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

            yield arr, [i, i + 1], []

        # Update start
        start += 1

    yield from finished_animation(arr)
