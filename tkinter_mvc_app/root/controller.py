from tkinter_mvc_app.books.controllers.book_controller import BookController
from tkinter_mvc_app.books.models.models import Book
from tkinter_mvc_app.books.views.tabs import BookSavedTab
from tkinter_mvc_app.root.views import MainView


class Controller:
    def __init__(self, view: MainView):
        self.view = view
        # self.model = model
        self.book_controller = BookController(view)

    def run(self):
        self.view.run_mainloop()
