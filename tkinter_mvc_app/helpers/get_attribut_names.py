from typing import Dict

from tkinter_mvc_app.books.models.models import Book

book_attributs: Dict[str, str] = Book.get_attribut_names()
print(book_attributs)
# book_attr_name = list(book_attributs.keys())
