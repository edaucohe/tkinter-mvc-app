from tkinter_mvc_app.books.views.frames import BookFrame
from tkinter_mvc_app.books.views.tabs import BookTab
from tkinter_mvc_app.root.views import MainView


class SaveBookController:
    def __init__(self, view: MainView):
        self.view = view
        self.bind()

    def bind(self):
        self.view.root.book_tab.book_frame.save_button.config(command=self.save_book)

    def save_book(self):
        title_label = self.view.root.book_tab.book_frame.widgets[0][0]
        title_entry = self.view.root.book_tab.book_frame.widgets[0][1]
        print("title_label: ", title_label["text"])
        print("title_entry: ", title_entry.get())

        already_read_label = self.view.root.book_tab.book_frame.widgets[13][0]
        already_read_checkbutton = self.view.root.book_tab.book_frame.widgets[13][1]
        print("already_read_label: ", already_read_label["text"])
        print("already_read_checkbutton: ", already_read_checkbutton.get())