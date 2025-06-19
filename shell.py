from shell_gap_sequences import sequences
from misc import finished_animation

def shell_sort(arr, sequence="shell"):
    n = len(arr)
    gaps = sequences[sequence](n)

    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                yield arr, [i, j - gap], []
                j -= gap
                    
            if arr[j] != temp:
                arr[j] = temp
                yield arr, [i, j], []

    yield from finished_animation(arr)
