from tkinter_mvc_app.books.models.models import Book


class BookInputs:
    @staticmethod
    def get_book_info(widgets):
        # title_label = widgets[0][0]
        # title_entry = widgets[0][1]
        # print("title_label: ", title_label["text"])
        # print("title_entry: ", title_entry.get())
        # print("title_entry type: ", type(title_entry.get()))

        new = Book.from_widgets(widgets)
        print("new: ", new)

        # already_read_label = widgets[13][0]
        # already_read_checkbutton = widgets[13][1]
        # print("already_read_label: ", already_read_label["text"])
        # print("already_read_checkbutton: ", already_read_checkbutton.get())
        # print("already_read_checkbutton type: ", type(already_read_checkbutton.get()))
