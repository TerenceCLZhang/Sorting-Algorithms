from algorithms.misc import finished_animation


def shell_sort(arr):
    def shell_gaps(n):
        gaps = []
        curr = n // 2
        while curr > 0:
            gaps.append(curr)
            curr //= 2
        return gaps

    n = len(arr)
    gaps = shell_gaps(n)

    # Perform a gapped insertion sort for each gap size
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Shift elements of arr[0..i-gap] that are greater than temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                yield arr, [i, j - gap], []
                j -= gap

            # Insert temp at the correct location if changed
            if arr[j] != temp:
                arr[j] = temp
                yield arr, [i, j], []

    yield from finished_animation(arr)
