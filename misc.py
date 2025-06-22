def finished_animation(arr):
    for i in range(len(arr)):
        yield arr, [], list(range(i + 1))
