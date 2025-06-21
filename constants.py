from algorithms import *

WIDTH = 800
HEIGHT = 600

CAPTION = "Sorting Algorithm Visualizer"

FPS = 60

COLORS = {
    "background": (0, 0, 0),
    "regular": (255, 255, 255),
    "highlight": (255, 100, 100),
    "sorted": (0, 255, 100)
}

SCENE_MAIN_MENU = "main_menu"
SCENE_SHELL_SORT_SEQUENCE = "shell_sequence"
SCENE_QUICK_SORT_SCHEME = "quick_scheme"

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
