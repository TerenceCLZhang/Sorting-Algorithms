from misc import finished_animation


def pancake_sort(arr):
    def flip(k):
        left = 0
        while left < k:
            arr[left], arr[k] = arr[k], arr[left]
            yield arr, [left, k], []
            k -= 1
            left += 1

    n = len(arr)
    while n > 1:
        max_index = max(range(n), key=lambda i: arr[i])
        if max_index != n - 1:
            if max_index != 0:
                yield from flip(max_index)
            yield from flip(n - 1)
        n -= 1

    yield from finished_animation(arr)
