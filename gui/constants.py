from algorithms import *

WIDTH = 960
HEIGHT = 540

CANVAS_WIDTH = 960
CANVAS_HEIGHT = 500

TITLE = "Sorting Algorithms Visualizer"

COLORS = {
    "background": "#000000",  # Black
    "regular": "#FFFFFF",     # White
    "highlight": "#FF6464",   # Light Red
    "sorted": "#00FF64"       # Greenish
}

FONT = "Courier"

ALGORITHMS = {
    # Optimal (O(n log n)) or better
    "Tim Sort": tim_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Quick Sort": quick_sort,
    "Radix Sort": radix_sort,

    # Simple/Classic Sorts (O(n^2))
    "Shell Sort": shell_sort,
    "Comb Sort": comb_sort,
    "Cocktail Shaker Sort": cocktail_shaker_sort,
    "Odd Even Sort": odd_even_sort,
    "Insertion Sort": insertion_sort,
    "Gnome Sort": gnome_sort,
    "Selection Sort": selection_sort,
    "Exchange Sort": exchange_sort,
    "Cycle Sort": cycle_sort,

    # Inefficient / Educational / Joke Sorts
    "Pancake Sort": pancake_sort,
    "Stooge Sort": stooge_sort,
    "Bozo Sort": bozo_sort,
    "Bogo Sort": bogo_sort,
}
