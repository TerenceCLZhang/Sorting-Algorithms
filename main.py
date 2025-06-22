import tkinter as tk
from main_menu import MainMenu
from visualizer import Visualizer


class App():
    def __init__(self):
        self.show_main_menu()

    def show_main_menu(self):
        self.main_menu = MainMenu(on_start=self.start_visualizer)
        self.main_menu.run()

    def start_visualizer(self, config):
        self.main_menu.window.destroy()

        self.visualizer = Visualizer(
            algorithm_name=config["algo"],
            n=config["n"],
            fps=config["fps"],
            on_exit=self.show_main_menu
        )
        self.visualizer.run()


if __name__ == "__main__":
    App()
