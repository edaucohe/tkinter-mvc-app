import tkinter as tk
from tkinter import ttk

from tkinter_mvc_app.books.views.frames import BookFrame, BookUpdate, \
    BookRetrieve, BookDelete
from tkinter_mvc_app.helpers.const import APP_NAME, WIDTH, HEIGHT


class GUISetup(tk.Tk):
    def __init__(self, app_name, width, height):
        super().__init__()
        min_width = int(width / 2)
        min_height = int(height / 2)

        # Window setup
        self.title(app_name)
        self.geometry(f"{width}x{height}")
        self.minsize(min_width, min_height)


class Tabs(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        # Create book tab
        self.book_tab = BookFrame(self)
        self.book_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.book_tab, text="Save book")

        # Update book tab
        self.another_tab = BookUpdate(self)
        self.another_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.another_tab, text="Update book")

        # Retrieve book tab
        self.another_tab = BookRetrieve(self)
        self.another_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.another_tab, text="Retrieve book")

        # Delete book tab
        self.another_tab = BookDelete(self)
        self.another_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.another_tab, text="Delete book")


class MainView:
    def __init__(self):
        self.gui_setup = GUISetup(APP_NAME, WIDTH, HEIGHT)

        # Tabs
        self.gui_setup.tabs = Tabs(self.gui_setup)
        self.gui_setup.tabs.pack(side="top", fill="x")

    def run_mainloop(self):
        self.gui_setup.mainloop()
