import pygame
import random

from bogo import bogo_sort
from bozo import bozo_sort
from exchange import exchange_sort
from bubble import bubble_sort
from oddeven import odd_even_sort
from comb import comb_sort
from cocktail import cocktail_shaker_sort
from gnome import gnome_sort
from insertion import insertion_sort
from shell import shell_sort
from selection import selection_sort
from heap import heap_sort
from radix import radix_sort
from quick import quick_sort
from stooge import stooge_sort
from pancake import pancake_sort

COLORS = {
    "background": (0, 0, 0),
    "regular": (255, 255, 255),
    "highlight": (255, 100, 100),
    "sorted": (0, 255, 100)
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

MIN_SPEED = 2
MAX_SPEED = 1000


def draw_bar(arr, screen, i, color, screen_h, bar_w):
    bar_h = screen_h * (arr[i] / len(arr))
    x = i * bar_w
    y = screen_h - bar_h
    bar = pygame.Rect(round(x), round(y), max(1, round(bar_w)), round(bar_h))
    pygame.draw.rect(screen, color, bar)

def draw_bars(arr, screen, h1=[], h2=[], sorted=False):
    n = len(arr)
    screen.fill(COLORS["background"])
    screen_w, screen_h = screen.get_size()
    bar_w = screen_w / n

    if sorted:
        for i in range(n):
            draw_bar(arr, screen, i, COLORS["sorted"], screen_h, bar_w)
    else:
        for i in range(n):
            draw_bar(arr, screen, i, COLORS["regular"], screen_h, bar_w)

        for i in h1:
            draw_bar(arr, screen, i, COLORS["highlight"], screen_h, bar_w)
        
        for i in h2:
            draw_bar(arr, screen, i, COLORS["sorted"], screen_h, bar_w)


def visualize(algo, n=100, speed=50, width=800, height=600, **kwargs):
    if algo not in ALGORITHMS:
        raise ValueError(f"Unknown algorithm key: '{algo}'. Valid options are: {', '.join(ALGORITHMS.keys())}") 
    
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sorting Algorithm Visualizations")

    # Font setup
    font_name = pygame.font.match_font("Courier New") or pygame.font.get_default_font()
    font_algo_name = pygame.font.Font(font_name, 20)
    font_algo_name.set_bold(True)

    # Text setup
    text_algo_name = font_algo_name.render(ALGORITHMS[algo][0], True, COLORS["regular"], COLORS["background"])
    textbox_algo_name = text_algo_name.get_rect(topleft=(10,10))

    # Initialize array
    arr = random.sample(range(1, n + 1), n)
    original_arr = arr

    # Get algorithm
    algorithm = ALGORITHMS[algo][1]
    sorting_process = algorithm(arr, **kwargs)

    # Variables
    current_speed = speed
    paused = False

    running = True
    while running:
        # User interactions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_KP_PLUS, pygame.K_PLUS] and current_speed < MAX_SPEED:
                    current_speed += 2
                    if current_speed > MIN_SPEED:
                        paused = False
                
                if event.key in [pygame.K_KP_MINUS, pygame.K_MINUS] and current_speed > MIN_SPEED:
                    current_speed -= 2
                    if current_speed == MIN_SPEED:
                        paused = True
                
                if event.key == pygame.K_SPACE:
                    paused = not paused

                if event.key == pygame.K_r:
                    arr = original_arr
                    sorting_process = algorithm(arr, **kwargs)
                    paused = False
            
                if event.key == pygame.K_n:
                    arr = random.sample(range(1, n + 1), n)
                    sorting_process = algorithm(arr, **kwargs)
                    paused = False
                
                if event.key == pygame.K_ESCAPE:
                    running = False

        if not paused:
            arr, h1, h2 = next(sorting_process, (None, None, None))
            
            # Draw the array
            if arr:
                draw_bars(arr, screen, h1, h2)
            else:
                arr = list(range(1, n + 1))
                draw_bars(arr, screen, h1, h2, sorted=True)

            screen.blit(text_algo_name, textbox_algo_name)

            # Update display
            pygame.display.flip()
            pygame.time.wait(1000 // current_speed)


    pygame.quit()
