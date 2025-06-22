from algorithms.misc import finished_animation


def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        # Find next gap
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            is_sorted = True
        elif gap == 9 or gap == 10:
            gap = 11

        # Single comb over the list
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                is_sorted = False

            yield arr, [i, i + gap], []
            i += 1

    yield from finished_animation(arr)
