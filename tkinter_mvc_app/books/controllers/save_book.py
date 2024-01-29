from tkinter_mvc_app.books.views.frames import BookFrame
from tkinter_mvc_app.books.views.inputs import BookInputs
from tkinter_mvc_app.books.views.tabs import BookTab
from tkinter_mvc_app.root.views import MainView


class SaveBookController:
    def __init__(self, view: MainView):
        self.view = view
        self.save_button = view.root.book_tab.book_frame.save_button
        self.widgets = view.root.book_tab.book_frame.widgets
        self.bind()
        self.get_book_info = BookInputs.get_book_info

    def bind(self):
        self.save_button.config(command=self.save_book)

    def save_book(self):
        self.get_book_info(self.widgets)

        # title_label = self.view.root.book_tab.book_frame.widgets[0][0]
        # title_entry = self.view.root.book_tab.book_frame.widgets[0][1]
        # print("title_label: ", title_label["text"])
        # print("title_entry: ", title_entry.get())
        #
        # already_read_label = self.view.root.book_tab.book_frame.widgets[13][0]
        # already_read_checkbutton = self.view.root.book_tab.book_frame.widgets[13][1]
        # print("already_read_label: ", already_read_label["text"])
        # print("already_read_checkbutton: ", already_read_checkbutton.get())
