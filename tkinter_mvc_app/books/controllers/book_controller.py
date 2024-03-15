from tkinter_mvc_app.books.models.models import Book
from tkinter_mvc_app.books.views.inputs import BookInputs
from tkinter_mvc_app.helpers.get_attribut_names import book_attributs
from tkinter_mvc_app.root.views import MainView


class BookController:
    def __init__(self, view: MainView):
        self.view = view
        self.saved_book_button = view.gui_setup.tabs.saved_book_tab.save_button
        # self.widgets = view.gui_setup.tabs.saved_book_tab.widgets
        self.saved_book_tab = view.gui_setup.tabs.saved_book_tab
        self.bind()
        self.get_book_info = BookInputs.get_book_info

    def bind(self):
        # self.save_button.config(command=self.save_book)
        self.saved_book_button.config(command=self.save_book_info)

    def save_book_info(self):
        # book_attr_name = list(book_attributs.keys())

        book_data = {
            book_attributs["original_name"][0]: self.saved_book_tab.title_input.get(),
            book_attributs["original_name"][1]: self.saved_book_tab.author_input.get(),
            book_attributs["original_name"][2]: self.saved_book_tab.synopsis_input.get(),
            book_attributs["original_name"][3]: self.saved_book_tab.genre_input.get(),
            book_attributs["original_name"][4]: self.saved_book_tab.publisher_input.get(),
            book_attributs["original_name"][5]: self.saved_book_tab.original_language_input.get(),
            book_attributs["original_name"][6]: self.saved_book_tab.book_language_input.get(),
            book_attributs["original_name"][7]: self.saved_book_tab.number_of_pages_input.get(),
            book_attributs["original_name"][8]: self.saved_book_tab.current_page_input.get(),
            # book_attributs["original_name"][9]: self.saved_book_tab.created_date_input.get(),
            book_attributs["original_name"][10]: self.saved_book_tab.purchase_date_input.get(),
            book_attributs["original_name"][11]: self.saved_book_tab.publication_date_input.get(),
            book_attributs["original_name"][12]: self.saved_book_tab.reading_date_input.get(),
            book_attributs["original_name"][13]: self.saved_book_tab.already_read_value.get(),
            book_attributs["original_name"][14]: self.saved_book_tab.is_current_book_value.get(),
        }

        print("book data: ", book_data)

        # self.get_book_info(self.widgets)

        # title_label = self.view.root.book_tab.book_frame.widgets[0][0]
        # title_entry = self.view.root.book_tab.book_frame.widgets[0][1]
        # print("title_label: ", title_label["text"])
        # print("title_entry: ", title_entry.get())
        #
        # already_read_label = self.view.root.book_tab.book_frame.widgets[13][0]
        # already_read_checkbutton = self.view.root.book_tab.book_frame.widgets[13][1]
        # print("already_read_label: ", already_read_label["text"])
        # print("already_read_checkbutton: ", already_read_checkbutton.get())
