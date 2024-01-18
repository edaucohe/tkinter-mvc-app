import dataclasses
import inspect
from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Dict, get_type_hints, get_origin

from tkinter_mvc_app.books.models.my_enums import Language, Genre
from tkinter_mvc_app.helpers.const import FIRST_MEMBER_POS, ATTR_POS


@dataclass
class Book:
    title: str
    authors: List[str]
    synopsis: str
    genre: Genre
    publisher: str = "Desconocido"
    original_language: Optional[Language] = None
    book_language: Optional[Language] = None
    number_of_pages: Optional[int] = None
    current_page: int = 0
    created_date: date = date.today()
    purchase_date: Optional[date] = None
    publication_date: Optional[date] = None
    reading_date: Optional[date] = None
    already_read: bool = False
    is_current_book: bool = False

    def to_dict(self):
        return dataclasses.asdict(self)

    @classmethod
    def get_attribut_names(cls):
        # To get type hints of model
        attribut_types = get_type_hints(cls)
        if "<class 'bool'>" in attribut_types:
            print("OK")

        attributs = dict()
        members: Dict = inspect.getmembers(cls)[FIRST_MEMBER_POS][ATTR_POS]
        for index, attribut_name in enumerate(members.keys()):
            # To place attribut types
            # attribut_type = attribut_types[attribut_name]

            try:
                attribut_value = getattr(cls, attribut_name)
            except AttributeError:
                attribut_value = None

            # attribut_type_hint = get_origin(attribut_type)

            # To capitalize names
            attribut_name = attribut_name.capitalize()

            # To erase "_" from attribut names
            if "_" in attribut_name:
                attribut_name = attribut_name.replace("_", " ")

            attributs[index] = attribut_name, attribut_value

        return attributs


# book = Book(title="El conde de montecristo",
#             authors=["Dumas"],
#             synopsis="Dantes es llevado a una prisión en Monte-cristo "
#                      "en donde fragua su venganza",
#             publisher="Poche",
#             genre=Genre.FICTION)
#
# print("libro: ", book.to_dict())
# print("Atributos: ", Book.get_attribut_names())
