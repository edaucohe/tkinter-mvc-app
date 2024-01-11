import tkinter as tk
from tkinter import ttk

from tkinter_mvc_app.books.views.views import BookFrame
from tkinter_mvc_app.root.const import APP_NAME, WIDTH, HEIGHT


class Root(tk.Tk):
    def __init__(self, app_name, width, height):
        super().__init__()
        min_width = int(width / 2)
        min_height = int(height / 2)

        # Window setup
        self.title(app_name)
        self.geometry(f"{width}x{height}")
        self.minsize(min_width, min_height)

        # Frames
        self.book_frame = BookFrame(self)
        self.book_frame.grid(row=0, column=0, sticky="nsew")


class MainView:
    def __init__(self):
        self.root = Root(APP_NAME, WIDTH, HEIGHT)

    def run_mainloop(self):
        self.root.mainloop()
