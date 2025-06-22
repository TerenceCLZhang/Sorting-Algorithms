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

ALGORITHMS = {
    "bogo": ("Bogo Sort", bogo_sort),
    "bozo": ("Bozo Sort", bozo_sort),
    "exchange": ("Exchange Sort", exchange_sort),
    "bubble": ("Bubble Sort", bubble_sort),
    "oddeven": ("Odd Even Sort", odd_even_sort),
    "comb": ("Comb Sort", comb_sort),
    "cocktail": ("Cocktail Shaker Sort", cocktail_shaker_sort),
    "gnome": ("Gnome Sort", gnome_sort),
    "insertion": ("Insertion Sort", insertion_sort),
    "shell": ("Shell Sort", shell_sort),
    "selection": ("Selection Sort", selection_sort),
    "heap": ("Heap Sort", heap_sort),
    "radix": ("Radix Sort", radix_sort),
    "quick": ("Quick Sort", quick_sort),
    "stooge": ("Stooge Sort", stooge_sort),
    "pancake": ("Pancake Sort", pancake_sort),
}
