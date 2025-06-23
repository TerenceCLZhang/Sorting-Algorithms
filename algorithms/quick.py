from algorithms.misc import finished_animation


def quick_sort(arr):
    # Hoare's partitioning
    def partition(low, high):
        pivot = arr[low]  # Pivot is the first element
        i = low - 1
        j = high + 1

        while True:
            # Move i forward to find an element ≥ pivot
            i += 1
            while arr[i] < pivot:
                i += 1

            # Move j backward to find an element ≤ pivot
            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j  # Return pivot index (partition point)

            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, [i, j], []

    def quick_sort_recursive(low, high):
        if low < high:
            # Perform partition and get generator
            gen = partition(low, high)
            try:
                while True:
                    yield next(gen)
            except StopIteration as e:
                pivot = e.value

            # Recursively sort the two halves
            yield from quick_sort_recursive(low, pivot)
            yield from quick_sort_recursive(pivot + 1, high)

    yield from quick_sort_recursive(0, len(arr) - 1)
    yield from finished_animation(arr)
