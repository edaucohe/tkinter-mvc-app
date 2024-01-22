from tkinter_mvc_app.books.controllers.save_book import SaveBookController
from tkinter_mvc_app.books.models.models import Book
from tkinter_mvc_app.books.views.frames import BookFrame
from tkinter_mvc_app.root.views import MainView


class Controller:
    def __init__(self, view: MainView):
        self.view = view
        # self.model = model
        self.save_book_controller = SaveBookController(view)

    def run(self):
        self.view.run_mainloop()
