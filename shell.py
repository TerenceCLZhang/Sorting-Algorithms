from shell_gap_sequences import sequences

def shell_sort(arr, sequence="shell"):
    """
    Sorts a list in ascending order using the Shell Sort algorithm.

    Shell Sort is an optimisation of Insertion Sort that allows the exchange of items that are far apart. 
    It starts by sorting elements far apart from each other and progressively reduces the gap between elements to be compared. 
    This improves efficiency by moving elements closer to their correct position faster than standard Insertion Sort.

    Time Complexities:
    - Best: Ω(n log n)
    - Average: Θ(n log n)
    - Worst: O(n^2)
    """
    n = len(arr)
    gaps = sequences[sequence](n)

    for gap in gaps:
        # Perform a gapped insertion sort for this gap
        for i in range(gap, n):
            temp = arr[i] # Store current element

            j = i
            # Shift elements that are gap positions apart and greater than temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap] # Shift element rightward
                yield arr, [j - gap], [], [i]
                j -= gap
            
            arr[j] = temp # Place temp in its correct sorted position
            yield arr, [j], [], [i]
