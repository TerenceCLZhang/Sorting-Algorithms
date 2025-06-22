from algorithms import *

WIDTH = 800
HEIGHT = 600

TITLE = "Sorting Algorithms Visualizer"

COLORS = {
    "background": "#000000",  # Black
    "regular": "#FFFFFF",     # White
    "highlight": "#FF6464",   # Light Red
    "sorted": "#00FF64"       # Greenish
}

FONT = "Courier"

ALGORITHMS = {
    "Bogo Sort": bogo_sort,
    "Bozo Sort": bozo_sort,
    "Exchange Sort": exchange_sort,
    "Bubble Sort": bubble_sort,
    "Odd Even Sort": odd_even_sort,
    "Comb Sort": comb_sort,
    "Cocktail Shaker Sort": cocktail_shaker_sort,
    "Gnome Sort": gnome_sort,
    "Insertion Sort": insertion_sort,
    "Shell Sort": shell_sort,
    "Selection Sort": selection_sort,
    "Heap Sort": heap_sort,
    "Radix Sort": radix_sort,
    "Quick Sort": quick_sort,
    "Stooge Sort": stooge_sort,
    "Pancake Sort": pancake_sort,
}
