from algorithms.misc import finished_animation


def gnome_sort(arr):
    i = 0
    while i < len(arr):
        # If current element is larger or equal than previous element move to next element
        if i == 0 or arr[i] >= arr[i - 1]:
            yield arr, [i - 1, i], []
            i += 1
        # Otherwise, swap elements and go back one element
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            yield arr, [i - 1, i], []
            i -= 1

    yield from finished_animation(arr)
