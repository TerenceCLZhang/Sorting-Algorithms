from algorithms.misc import finished_animation


def pancake_sort(arr):
    # Flip the subarray arr[0..k] in place
    def flip(k):
        left = 0
        while left < k:
            arr[left], arr[k] = arr[k], arr[left]
            yield arr, [left, k], []
            k -= 1
            left += 1

    n = len(arr)
    while n > 1:
        # Find the index of the maximum element in arr[0..n-1]
        max_index = max(range(n), key=lambda i: arr[i])

        # Bring the max element to front if it's not already there
        if max_index != n - 1:
            if max_index != 0:
                yield from flip(max_index)

             # Flip it to its correct position at the end of unsorted part
            yield from flip(n - 1)

        n -= 1  # Reduce the size of the unsorted part

    yield from finished_animation(arr)
