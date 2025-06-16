import pygame
import random

from bogo import bogosort
from exchange import exchange_sort
from bubble import bubble_sort, optimized_bubble_sort
from oddeven import odd_even_sort
from comb import comb_sort
from cocktail import cocktail_shaker_sort
from gnome import gnome_sort
from insertion import insertion_sort, binary_insertion_sort
from shell import shell_sort

COLORS = {
    "bg": (0, 0, 0),
    "reg": (255, 255, 255),
    "h1": (255, 100, 100),
    "h2": (255, 165, 0),
    "h3": (100, 100, 255),
    "sorted": (0, 255, 100)
}
ALGORITHMS = {
    "Bogosort": bogosort,
    "Exchange Sort": exchange_sort,
    "Bubble Sort": bubble_sort,
    "Optimized Bubble Sort": optimized_bubble_sort,
    "Odd Even Sort": odd_even_sort,
    "Comb Sort": comb_sort,
    "Cocktail Shaker Sort": cocktail_shaker_sort,
    "Gnome Sort": gnome_sort,
    "Insertion Sort": insertion_sort,
    "Shell Sort": shell_sort,
    "Binary Insertion Sort": binary_insertion_sort
}
MIN_SPEED = 10
MAX_SPEED = 1000


def draw_bar(arr, screen, i, color, screen_h, bar_w):
    bar_h = screen_h * (arr[i] / len(arr))
    x = i * bar_w
    y = screen_h - bar_h
    bar = pygame.Rect(round(x), round(y), max(1, round(bar_w)), round(bar_h))
    pygame.draw.rect(screen, color, bar)

def draw_bars(arr, screen, h1=[], h2=[], h3=[], sorted=False):
    n = len(arr)
    screen.fill(COLORS["bg"])
    screen_w, screen_h = screen.get_size()
    bar_w = screen_w / n

    if sorted:
        for i in range(n):
            draw_bar(arr, screen, i, COLORS["sorted"], screen_h, bar_w)
    else:
        for i in range(n):
            draw_bar(arr, screen, i, COLORS["reg"], screen_h, bar_w)

        for i in h1:
            draw_bar(arr, screen, i, COLORS["h1"], screen_h, bar_w)

        for i in h2:
            draw_bar(arr, screen, i, COLORS["h2"], screen_h, bar_w)

        for i in h3:
            draw_bar(arr, screen, i, COLORS["h3"], screen_h, bar_w)


def visualize(algorithm, n=50, speed=30, width=800, height=600, **kwargs):
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sorting Algorithm Visualizations")

    # Font setup
    font_name = pygame.font.match_font("Courier New") or pygame.font.get_default_font()
    font = pygame.font.Font(font_name, 20)
    font.set_bold(True)

    # Text setup
    text = font.render(algorithm, True, COLORS["reg"], COLORS["bg"])
    textbox = text.get_rect(topleft=(10,10))

    # Initialize array
    arr = random.sample(range(1, n + 1), n)
    original_arr = arr

    # Get algorithm
    algorithm = ALGORITHMS[algorithm]
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
                    current_speed += 10
                    if current_speed > MIN_SPEED:
                        paused = False
                
                if event.key in [pygame.K_KP_MINUS, pygame.K_MINUS] and current_speed > MIN_SPEED:
                    current_speed -= 10
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
            arr, h1, h2, h3 = next(sorting_process, (None, None, None, None))
            
            # Draw the array
            if arr:
                draw_bars(arr, screen, h1=h1, h2=h2, h3=h3)
            else:
                arr = list(range(1, n + 1))
                draw_bars(arr, screen,h1=h1, h2=h2, h3=h3, sorted=True)

            screen.blit(text, textbox)

            # Update display
            pygame.display.flip()
            pygame.time.wait(1000 // current_speed)


    pygame.quit()
