from algorithms.misc import finished_animation


def cycle_sort(arr):
    n = len(arr)

    for cycle_start in range(n - 1):
        item = arr[cycle_start]

        # Find the correct position for the item
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            yield arr, [cycle_start, i], []
            if arr[i] < item:
                pos += 1

        # If the item is already in the correct position, continue
        if pos == cycle_start:
            continue

        # Skip duplicates
        while item == arr[pos]:
            pos += 1

        # Place the item at its correct position
        yield arr, [pos, cycle_start], []
        arr[pos], item = item, arr[pos]
        yield arr, [pos, cycle_start], []
        
        # Rotate the rest of the cycle
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                yield arr, [cycle_start, i], []
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            yield arr, [pos, cycle_start], []
            arr[pos], item = item, arr[pos]
            yield arr, [pos, cycle_start], []

    yield from finished_animation(arr)
