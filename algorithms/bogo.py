import random
from misc import finished_animation


def bogo_sort(arr):
    def is_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    while not is_sorted(arr):
        random.shuffle(arr)
        bad_indices = [i for i in range(1, len(arr)) if arr[i] < arr[i - 1]]

        yield arr, bad_indices, []

    yield from finished_animation(arr)
