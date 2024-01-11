from tkinter import ttk


class BookFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Setup book grid
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)

        # Label widgets
        self.title_label = ttk.Label(self, text="Título", background="red")
        self.title_label.grid(row=0, column=0, sticky="nsew")
