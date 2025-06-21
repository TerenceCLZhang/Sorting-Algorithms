from misc import finished_animation


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Update largest if left child exists and is larger than largest
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Update largest if the right child exists and is larger than largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Swap if different
        if largest != i:
            yield arr, [largest, i], []
            arr[i], arr[largest] = arr[largest], arr[i]
            yield from heapify(arr, n, largest)

    def build_max_heap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            yield from heapify(arr, n, i)

    n = len(arr)
    yield from build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap first and last elements
        yield from heapify(arr, i, 0)  # Update max heap

    yield from finished_animation(arr)
