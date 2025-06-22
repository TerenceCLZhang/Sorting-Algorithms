import tkinter as tk
import random
from constants import WIDTH, HEIGHT, COLORS, ALGORITHMS, TITLE


class Visualizer:
    def __init__(self, algo="bogo", n=100, fps=60):
        self.algorithm_name = ALGORITHMS[algo][0]
        self.algorithm = ALGORITHMS[algo][1]
        self.n = n
        self.fps = fps

        self.arr, self.original_arr = self.initialize_arr()

        self.sorting_process = self.algorithm(self.arr)

        self.window = tk.Tk()

        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.configure(background=COLORS["background"])
        self.window.resizable(False, False)

        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT,
                                bg=COLORS["background"], highlightthickness=0)
        self.canvas.pack()

        title_label = tk.Label(
            self.window,
            text=self.algorithm_name,
            fg=COLORS["regular"],
            bg=COLORS["background"],
            font=("Courier", 15)
        )
        title_label.place(x=10, y=10)

        self.paused = False

    def initialize_arr(self):
        arr = random.sample(range(1, self.n + 1), self.n)
        original_arr = arr
        return arr, original_arr

    def draw_bar(self, i, color, bar_w):
        bar_h = HEIGHT * (self.arr[i] / len(self.arr))
        x = int(i * bar_w)
        y = int(HEIGHT - bar_h)

        if bar_w >= 1:
            self.canvas.create_rectangle(
                x, y, x + bar_w, HEIGHT,
                outline=COLORS["background"],
                fill=color,
                width=1,
            )
        else:
            self.canvas.create_line(
                x, y, x, HEIGHT,
                fill=color
            )

    def draw_bars(self, h1=[], h2=[], sorted=False):
        n = len(self.arr)
        bar_w = WIDTH / n

        if sorted:
            for i in range(n):
                self.draw_bar(i, COLORS["sorted"], bar_w)
        else:
            for i in range(n):
                self.draw_bar(i, COLORS["regular"], bar_w)

            for i in h1:
                self.draw_bar(i, COLORS["highlight"], bar_w)

            for i in h2:
                self.draw_bar(i, COLORS["sorted"], bar_w)

    def run(self):
        def on_key(event):
            if event.keysym == "Escape":
                self.window.destroy()
            if event.keysym == "space":
                self.paused = not self.paused
            if event.keysym == "r":
                self.arr = self.original_arr.copy()
                self.sorting_process = self.algorithm(self.arr)
                self.paused = False
            if event.keysym == "n":
                self.arr, self.original_arr = self.initialize_arr()
                self.sorting_process = self.algorithm(self.arr)
                self.paused = False

        def game_loop():
            if not self.paused:
                self.canvas.delete("all")

                self.arr, h1, h2 = next(
                    self.sorting_process, (None, None, None))

                if self.arr:
                    self.draw_bars(h1, h2)
                else:
                    self.arr = list(range(1, self.n + 1))
                    self.draw_bars(h1, h2, sorted=True)

            self.window.after(1000 // self.fps, game_loop)

        self.window.bind("<Key>", on_key)

        game_loop()

        self.window.mainloop()
