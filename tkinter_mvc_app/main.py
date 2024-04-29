from root.controller import Controller
from root.views import MainView
from tkinter_mvc_app.books.models.models import Book


def main():
    view = MainView()
    book = Book()
    controller = Controller(view=view, book=book)
    controller.run()


if __name__ == '__main__':
    main()
