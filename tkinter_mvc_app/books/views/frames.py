from tkinter import ttk


class BookFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Setup book grid
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=2)
        self.grid_rowconfigure(index=(0, 1, 2, 3, 4, 5), weight=1)

        # Title widget
        self.title_label = ttk.Label(self, text="Título", background="red")
        self.title_label.grid(row=0, column=0, sticky="nsew")
        self.title_input = ttk.Entry(self)
        self.title_input.grid(row=0, column=1, sticky="nsew")

        # Author widget
        self.author_label = ttk.Label(self, text="Autor", background="yellow")
        self.author_label.grid(row=1, column=0, sticky="nsew")
        self.author_input = ttk.Entry(self)
        self.author_input.grid(row=1, column=1, sticky="nsew")
