import tkinter as tk
import random
from gui.screen import Screen
from gui.constants import WIDTH, HEIGHT, COLORS, ALGORITHMS


class Visualizer(Screen):
    def __init__(self, algorithm_name="Bogo Sort", n=50, fps=60, on_exit=None):
        super().__init__()

        self.algorithm = ALGORITHMS[algorithm_name]
        self.n = n
        self.fps = fps
        self.on_exit_callback = on_exit

        self.MIN_FPS = 1
        self.MAX_FPS = 100

        self.paused = False

        self.after_id = None  # Cancel scheduled after callback

        self.arr, self.original_arr = self.initialize_arr()
        self.sorting_process = self.algorithm(self.arr)

        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT,
                                bg=COLORS["background"], highlightthickness=0)
        self.canvas.pack()

        title_label = tk.Label(
            self.window,
            text=algorithm_name,
            fg=COLORS["regular"],
            bg=COLORS["background"],
            font=("Courier", 15)
        )
        title_label.place(x=10, y=10)

        self.fps_label = tk.Label(
            self.window,
            text=f"FPS: {self.fps}",
            fg=COLORS["regular"],
            bg=COLORS["background"],
            font=("Courier", 15)
        )
        self.fps_label.place(x=10, y=50)

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
            # Back to main menu
            if event.keysym == "Escape":
                if self.after_id is not None:
                    self.window.after_cancel(self.after_id)
                    self.after_id = None

                self.window.destroy()
                if self.on_exit_callback:
                    self.on_exit_callback()

            # Pause / unpause
            if event.keysym == "space":
                self.paused = not self.paused

            # Restart
            if event.keysym == "r":
                self.arr = self.original_arr.copy()
                self.sorting_process = self.algorithm(self.arr)
                self.paused = False

            # New array
            if event.keysym == "n":
                self.arr, self.original_arr = self.initialize_arr()
                self.sorting_process = self.algorithm(self.arr)
                self.paused = False

            # Increase FPS
            if event.keysym == "plus":
                if self.fps < self.MAX_FPS:
                    self.fps = min(self.fps + 1, self.MAX_FPS)

            # Decrease FPS
            if event.keysym == "minus":
                if self.fps > self.MIN_FPS:
                    self.fps = max(self.fps - 1, self.MIN_FPS)

        def window_loop():
            self.fps_label.config(text=f"FPS: {self.fps}")

            if not self.paused:
                self.canvas.delete("all")

                self.arr, h1, h2 = next(
                    self.sorting_process, (None, None, None))

                if self.arr:
                    self.draw_bars(h1, h2)
                else:
                    self.arr = list(range(1, self.n + 1))
                    self.draw_bars(h1, h2, sorted=True)

            self.after_id = self.window.after(1000 // self.fps, window_loop)

        self.window.bind("<Key>", on_key)
        self.window.after(1000, window_loop)
        self.window.mainloop()
