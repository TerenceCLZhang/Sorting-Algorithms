from misc import finished_animation


def radix_sort(arr):
    num_digits = len(str(max(arr)))  # Find length of largest number

    for digit in range(num_digits):
        buckets = [[] for _ in range(10)]

        # Place numbers into buckets
        for i, num in enumerate(arr):
            idx = (num // 10 ** digit) % 10
            buckets[idx].append(num)
            yield arr, [i], []

        flat = [num for bucket in buckets for num in bucket]

        # Re-order array
        for i in range(len(arr)):
            arr[i] = flat[i]
            yield arr, [i], []

    yield from finished_animation(arr)
