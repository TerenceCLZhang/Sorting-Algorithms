from algorithms.misc import finished_animation


def tim_sort(arr):
    MIN_MERGE = 32  # Minimum run size for merging (standard value in TimSort)

    def calculate_min_run(n):
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1
            n >>= 1
        return n + r

    def insertion_sort(left, right):
        for i in range(left + 1, right + 1):
            j = i
            # Shift elements to sort in place
            while j > left and arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
                yield arr, [j, j - 1], []

    def merge_runs(l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]

        i = j = 0
        k = l

        # Merge elements back into arr[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                yield arr, [k], []
                i += 1
            else:
                arr[k] = right[j]
                yield arr, [k], []
                j += 1
            k += 1

         # Copy remaining elements from left[]
        while i < len(left):
            arr[k] = left[i]
            yield arr, [k], []
            i += 1
            k += 1

        # Copy remaining elements from right[]
        while j < len(right):
            arr[k] = right[j]
            yield arr, [k], []
            j += 1
            k += 1

    n = len(arr)
    min_run = calculate_min_run(n)

    # Sort small chunks (runs) using insertion sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        yield from insertion_sort(start, end)

    # Merge runs in size-doubling manner
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, left + 2 * size - 1)

            # Only merge if right half exists
            if mid < right:
                yield from merge_runs(left, mid, right)
        size *= 2

    yield from finished_animation(arr)
