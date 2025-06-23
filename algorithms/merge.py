from algorithms.misc import finished_animation


def merge_sort(arr):
    def merge(start, mid, end):
        start2 = mid + 1

        # If already in order, no need to merge
        if arr[mid] <= arr[start2]:
            return

        while start <= mid and start2 <= end:
            yield arr, [start, start2], []
            if arr[start] <= arr[start2]:
                start += 1
            else:
                value = arr[start2]
                index = start2

                # Shift elements to the right
                while index != start:
                    arr[index] = arr[index - 1]
                    index -= 1
                    yield arr, [index, index + 1], []

                arr[start] = value
                yield arr, [start], []

                # Update all pointers
                start += 1
                mid += 1
                start2 += 1

    def merge_sort_recursive(start, end):
        if start < end:
            mid = (start + end) // 2
            yield from merge_sort_recursive(start, mid)
            yield from merge_sort_recursive(mid + 1, end)
            yield from merge(start, mid, end)

    yield from merge_sort_recursive(0, len(arr) - 1)
    yield from finished_animation(arr)
