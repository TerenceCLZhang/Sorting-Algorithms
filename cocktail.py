def cocktail_shaker_sort(arr):
    """
    Sorts a list in ascending order using the Cocktail Shaker Sort algorithm.

    Cocktail Shaker Sort (also known as Cocktail Sort, Bidirectional Bubble Sort or Shaker Sort) is a variation of Bubble Sort.
    It works by passing through the list in both directions:
    - In the forward pass, it bubbles the largest element to the end.
    - In the backward pass, it bubbles the smallest element to the beginning.
    This process continues until no swaps are made in a complete pass.

    Time Complexities:
    - Best: Ω(n)
    - Average: Θ(n²)
    - Worst: O(n²)
    """
    n = len(arr)
    is_sorted = False
    start, end = 0, n - 1

    while not is_sorted:
        is_sorted = True

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
            yield arr, [i, i + 1], [], list(range(start)) + list(range(end + 1, n))

        # Update end
        end -= 1

        # Check if sorted
        if is_sorted:
            break

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
            yield arr, [i, i + 1], [], list(range(start)) + list(range(end + 1, n))
        
        # Update start
        start += 1