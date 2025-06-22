import tkinter as tk
from gui.screen import Screen
from gui.constants import COLORS, ALGORITHMS, FONT


class MainMenu(Screen):
    def __init__(self, on_start=None):
        super().__init__()

        self.on_start_callback = on_start

        # Initialize variables
        self.algorithms = list(ALGORITHMS.keys())
        self.selected_algorithm = tk.StringVar(
            value=self.algorithms[0])
        self.n_value = tk.IntVar(value=50)
        self.fps_value = tk.IntVar(value=60)

        self.pady_label = (15, 0)

        # Title
        title_label = tk.Label(
            self.window,
            text="Sorting Algorithms Visualizer",
            fg=COLORS["regular"],
            bg=COLORS["background"],
            font=(FONT, 30, "bold")
        )
        title_label.pack(pady=20)

        # Display variable adjustors
        self.algorithms_display()
        self.slider_display("Number of Elements:", self.n_value, 1, 500)
        self.slider_display("FPS:", self.fps_value, 1, 100)

        # Start button
        start_button = tk.Button(self.window, text="Start", font=(
            FONT, 15, "bold"), relief="flat", cursor="hand2", command=self.on_start)
        start_button.pack(pady=(30, 10))

    def algorithms_display(self):
        sorting_algorithm_label = tk.Label(
            self.window,
            text="Sorting Algorithm:",
            fg=COLORS["regular"],
            bg=COLORS["background"],
            font=(FONT, 20),
            relief="flat",
            highlightthickness=0,
            bd=1,
        )
        sorting_algorithm_label.pack(pady=self.pady_label)

        self.algorithms_selector = tk.OptionMenu(
            self.window, self.selected_algorithm, *self.algorithms)
        self.algorithms_selector.config(font=(FONT, 10), cursor="hand2",)
        self.algorithms_selector["menu"].config(
            font=(FONT, 10), cursor="hand2",)
        self.algorithms_selector.pack()

    def slider_display(self, text, var, from_, to):
        def validate_input(new_value):
            try:
                value = int(new_value)
                if from_ <= value <= to:
                    return True
            except ValueError:
                pass
            # Revert to the last valid value
            self.window.after_idle(lambda: var.set(prev_value.get()))
            return False

        def on_var_change(*args):
            prev_value.set(var.get())

        prev_value = tk.IntVar(value=var.get())
        var.trace_add("write", on_var_change)

        vcmd = (self.window.register(validate_input), "%P")

        label = tk.Label(
            self.window,
            text=text,
            fg=COLORS["regular"],
            bg=COLORS["background"],
            font=(FONT, 20)
        )
        label.pack(pady=self.pady_label)

        scale = tk.Scale(
            self.window,
            variable=var,
            from_=from_,
            to=to,
            orient=tk.HORIZONTAL,
            length=250,
            resolution=1,
            font=(FONT, 10),
            highlightthickness=0,
            cursor="hand2",
        )
        scale.pack()

        entry = tk.Entry(self.window, textvariable=var, width=5,
                         validate="focusout", validatecommand=vcmd)
        entry.pack(pady=(5, 0))

    def on_start(self):
        config = {
            "algo": self.selected_algorithm.get(),
            "n": self.n_value.get(),
            "fps": self.fps_value.get(),
        }
        self.window.destroy()
        if self.on_start_callback:
            self.on_start_callback(config)

    def run(self):
        self.window.mainloop()
