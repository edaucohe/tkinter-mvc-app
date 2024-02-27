import tkinter as tk

from tkinter_mvc_app.root.tabs import Tab
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


class MainView:
    def __init__(self):
        self.gui_setup = GUISetup(APP_NAME, WIDTH, HEIGHT)

        # Tabs
        self.gui_setup.tabs = Tab(self.gui_setup)
        self.gui_setup.tabs.pack(side="top", fill="x")

    def run_mainloop(self):
        self.gui_setup.mainloop()
