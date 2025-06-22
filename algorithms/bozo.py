import random
from algorithms.misc import finished_animation


def bozo_sort(arr):
    def is_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    while not is_sorted(arr):
        i, j = random.sample(range(len(arr)), 2)
        arr[i], arr[j] = arr[j], arr[i]
        yield arr, [i, j], []

    yield from finished_animation(arr)
