from algorithms.misc import finished_animation


def cycle_sort(arr):
    n = len(arr)

    for cycle_start in range(n - 1):
        item = arr[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, n):
            yield arr, [cycle_start, i], []
            if arr[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1

        yield arr, [pos, cycle_start], []
        arr[pos], item = item, arr[pos]
        yield arr, [pos, cycle_start], []

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
