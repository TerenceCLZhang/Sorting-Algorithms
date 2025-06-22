import tkinter as tk
from constants import WIDTH, HEIGHT, COLORS, TITLE


class Screen:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.window.configure(background=COLORS["background"])
        self.window.resizable(False, False)

    def run(self):
        pass
