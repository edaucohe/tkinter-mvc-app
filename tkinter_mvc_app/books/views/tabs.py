import tkinter as tk
from datetime import date

from tkcalendar import Calendar, DateEntry
from tkinter import ttk

from tkinter_mvc_app.books.models.models import Book
from tkinter_mvc_app.books.models.my_enums import Genre, Language
from tkinter_mvc_app.helpers.get_attribut_names import book_attributs
from tkinter_mvc_app.helpers.widgets_creation import create_widgets


class BookSavedTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Setup book grid
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=2)
        # self.grid_rowconfigure(index=(0, 1, 2, 3, 4, 5), weight=1)

        # Create labels and entries
        # self.widgets = create_widgets(ttk=ttk,
        #                               frame=self,
        #                               model_attribut_names=Book.get_attribut_names)

        # print(self.widgets)

        # Title widget
        self.title_label = ttk.Label(self,
                                     text=book_attributs["formatted_name"][0],
                                     background="red")
        self.title_label.grid(row=0, column=0, sticky="nsew")
        self.title_input = ttk.Entry(self)
        self.title_input.grid(row=0, column=1, sticky="nsew")

        # Author widget
        self.author_label = ttk.Label(self,
                                      text=book_attributs["formatted_name"][1],
                                      background="yellow")
        self.author_label.grid(row=1, column=0, sticky="nsew")
        self.author_input = ttk.Entry(self)
        self.author_input.grid(row=1, column=1, sticky="nsew")

        # Synopsis widget
        self.synopsis_label = ttk.Label(self,
                                        text=book_attributs["formatted_name"][2],
                                        background="red")
        self.synopsis_label.grid(row=2, column=0, sticky="nsew")
        self.synopsis_input = ttk.Entry(self)
        self.synopsis_input.grid(row=2, column=1, sticky="nsew")

        # Genre widget
        self.genre_label = ttk.Label(self,
                                     text=book_attributs["formatted_name"][3],
                                     background="yellow")
        self.genre_label.grid(row=3, column=0, sticky="nsew")
        self.genre_input = ttk.Combobox(self,
                                        values=[Genre.FICTION.value, Genre.NO_FICTION.value])
        self.genre_input.grid(row=3, column=1, sticky="nsew")

        # Publisher widget
        self.publisher_label = ttk.Label(self,
                                         text=book_attributs["formatted_name"][4],
                                         background="red")
        self.publisher_label.grid(row=4, column=0, sticky="nsew")
        self.publisher_input = ttk.Entry(self)
        self.publisher_input.grid(row=4, column=1, sticky="nsew")

        # Original language widget
        self.original_language_label = ttk.Label(self,
                                      text=book_attributs["formatted_name"][5],
                                      background="yellow")
        self.original_language_label.grid(row=5, column=0, sticky="nsew")
        self.original_language_input = ttk.Combobox(self,
                                                values=[Language.SPANISH.value, Language.FRENCH.value, Language.ENGLISH.value])
        self.original_language_input.grid(row=5, column=1, sticky="nsew")

        # Book language widget
        self.book_language_label = ttk.Label(self,
                                             text=book_attributs["formatted_name"][6],
                                             background="red")
        self.book_language_label.grid(row=6, column=0, sticky="nsew")
        self.book_language_input = ttk.Combobox(self,
                                                values=[Language.SPANISH.value, Language.FRENCH.value, Language.ENGLISH.value])
        self.book_language_input.grid(row=6, column=1, sticky="nsew")

        # Number of pages widget
        self.number_of_pages_label = ttk.Label(self,
                                               text=book_attributs["formatted_name"][7],
                                               background="yellow")
        self.number_of_pages_label.grid(row=7, column=0, sticky="nsew")
        self.number_of_pages_input = ttk.Entry(self)
        self.number_of_pages_input.grid(row=7, column=1, sticky="nsew")

        # Current page widget
        self.current_page_label = ttk.Label(self,
                                            text=book_attributs["formatted_name"][8],
                                            background="red")
        self.current_page_label.grid(row=8, column=0, sticky="nsew")
        self.current_page_input = ttk.Entry(self)
        self.current_page_input.grid(row=8, column=1, sticky="nsew")

        # Purchase date widget
        self.purchase_date_label = ttk.Label(self,
                                             text=book_attributs["formatted_name"][10],
                                            background="yellow")
        self.purchase_date_label.grid(row=9, column=0, sticky="nsew")
        self.purchase_date_input = DateEntry(self, selectmode="day", date_pattern="dd-mm-yyyy")  # Calendar mode
        self.purchase_date_input.grid(row=9, column=1, sticky="nsew")
        # self.purchase_date_input = ttk.Entry(self)
        # self.purchase_date_input.grid(row=9, column=1, sticky="nsew")

        # Publication date widget
        self.publication_date_label = ttk.Label(self,
                                                text=book_attributs["formatted_name"][11],
                                                background="red")
        self.publication_date_label.grid(row=10, column=0, sticky="nsew")
        self.publication_date_input = DateEntry(self, selectmode="day", date_pattern="dd-mm-yyyy")  # Calendar mode
        self.publication_date_input.grid(row=10, column=1, sticky="nsew")
        # self.publication_date_input = ttk.Entry(self)
        # self.publication_date_input.grid(row=10, column=1, sticky="nsew")

        # Reading date widget
        self.reading_date_label = ttk.Label(self,
                                            text=book_attributs["formatted_name"][12],
                                            background="yellow")
        self.reading_date_label.grid(row=11, column=0, sticky="nsew")
        self.reading_date_input = DateEntry(self, selectmode="day", date_pattern="dd-mm-yyyy")  # Calendar mode
        self.reading_date_input.grid(row=11, column=1, sticky="nsew")
        # self.reading_date_input = ttk.Entry(self)
        # self.reading_date_input.grid(row=11, column=1, sticky="nsew")

        # Already read widget
        self.already_read_label = ttk.Label(self,
                                            text=book_attributs["formatted_name"][13],
                                            background="red")
        self.already_read_label.grid(row=12, column=0, sticky="nsew")

        self.already_read_value = tk.BooleanVar()
        self.already_read_check_button = ttk.Checkbutton(self, variable=self.already_read_value)
        self.already_read_check_button.grid(row=12, column=1, sticky="nsew")
        # Is current book widget
        self.is_current_book_label = ttk.Label(self,
                                               text=book_attributs["formatted_name"][14],
                                               background="yellow")
        self.is_current_book_label.grid(row=13, column=0, sticky="nsew")

        self.is_current_book_value = tk.BooleanVar()
        self.is_current_book_check_button = ttk.Checkbutton(self, variable=self.is_current_book_value)
        self.is_current_book_check_button.grid(row=13, column=1, sticky="nsew")

        # Create button
        self.save_button = ttk.Button(master=self, text="Save book")
        self.button_row_idx = len(book_attributs["formatted_name"])
        self.save_button.grid(row=self.button_row_idx, column=0, sticky="nsew")


class BookUpdatedTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Setup book grid
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=2)

        # Title widget
        self.title_label = ttk.Label(self, text="Title", background="cyan")
        self.title_label.grid(row=0, column=0, sticky="nsew")
        self.title_input = ttk.Entry(self)
        self.title_input.grid(row=0, column=1, sticky="nsew")

        # Update button
        self.save_button = ttk.Button(master=self, text="Update book")
        self.button_row_idx = len(book_attributs["formatted_name"])
        self.save_button.grid(row=self.button_row_idx, column=0, sticky="nsew")


class BookRetrievedTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Setup book grid
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=2)

        # Title widget
        self.title_label = ttk.Label(self, text="Title", background="white")
        self.title_label.grid(row=0, column=0, sticky="nsew")
        self.title_input = ttk.Entry(self)
        self.title_input.grid(row=0, column=1, sticky="nsew")

        # Retrieve button
        self.save_button = ttk.Button(master=self, text="Retrieve book")
        self.button_row_idx = len(book_attributs["formatted_name"])
        self.save_button.grid(row=self.button_row_idx, column=0, sticky="nsew")


class BookDeletedTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Setup book grid
        self.grid_columnconfigure(index=0, weight=0)
        self.grid_columnconfigure(index=1, weight=1)
        self.grid_columnconfigure(index=2, weight=2)

        # Title widget
        self.title_label = ttk.Label(self, text="Title", background="yellow")
        self.title_label.grid(row=0, column=0, sticky="nsew")
        self.title_input = ttk.Entry(self)
        self.title_input.grid(row=0, column=1, sticky="nsew")

        # Delete button
        self.save_button = ttk.Button(master=self, text="Delete book")
        self.button_row_idx = len(book_attributs["formatted_name"])
        self.save_button.grid(row=self.button_row_idx, column=0, sticky="nsew")
