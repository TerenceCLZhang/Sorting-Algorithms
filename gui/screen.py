import tkinter as tk
from gui.constants import WIDTH, HEIGHT, COLORS, TITLE


class Screen:
    def __init__(self):
        self.window = tk.Tk()

        self.window.title(TITLE)
        self.window.configure(background=COLORS["background"])
        self.window.resizable(False, False)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width // 2) - (WIDTH // 2)
        y = (screen_height // 2) - (HEIGHT // 2)

        self.window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

    def run(self):
        pass
