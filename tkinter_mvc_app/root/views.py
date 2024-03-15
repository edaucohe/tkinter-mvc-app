import tkinter as tk
from tkinter import ttk

from tkinter_mvc_app.books.views.tabs \
    import BookSavedTab, BookUpdatedTab, BookRetrievedTab, BookDeletedTab
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

        # Saved book tab
        self.saved_book_tab = BookSavedTab(self)
        self.saved_book_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.saved_book_tab, text="Save book")

        # Updated book tab
        self.updated_book_tab = BookUpdatedTab(self)
        self.updated_book_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.updated_book_tab, text="Update book")

        # Retrieved book tab
        self.retrieved_book_tab = BookRetrievedTab(self)
        self.retrieved_book_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.retrieved_book_tab, text="Retrieve book")

        # Deleted book tab
        self.deleted_book_tab = BookDeletedTab(self)
        self.deleted_book_tab.grid(row=0, column=0, sticky="nsew")
        self.add(self.deleted_book_tab, text="Delete book")


class MainView:
    def __init__(self):
        self.gui_setup = GUISetup(APP_NAME, WIDTH, HEIGHT)

        # Tabs
        self.gui_setup.tabs = Tabs(self.gui_setup)
        self.gui_setup.tabs.pack(side="top", fill="x")

    def run_mainloop(self):
        self.gui_setup.mainloop()
