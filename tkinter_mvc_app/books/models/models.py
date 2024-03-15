import dataclasses
import inspect
from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Dict, get_type_hints, get_origin, Any

from tkinter_mvc_app.books.models.my_enums import Language, Genre
from tkinter_mvc_app.helpers.const import FIRST_MEMBER_POS, ATTR_POS


@dataclass
class Book:
    title: str
    author: str
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
        attributs = dict()
        members: Dict = inspect.getmembers(cls)[FIRST_MEMBER_POS][ATTR_POS]

        original_names = list()
        formatted_names = list()
        for attribut_name in members.keys():
            # try:
            #     attribut_value = getattr(cls, attribut_name)
            # except AttributeError:
            #     attribut_value = None

            # attribut_type_hint = get_origin(attribut_type)

            # To capitalize names
            formatted_name = attribut_name.capitalize()

            # To erase "_"
            if "_" in formatted_name:
                formatted_name = formatted_name.replace("_", " ")

            # attributs[index] = attribut_name, attribut_value
            # attributs[attribut_name] = formatted_name

            original_names.append(attribut_name)
            formatted_names.append(formatted_name)

        # print(attributs)
        attributs["original_name"] = original_names
        attributs["formatted_name"] = formatted_names

        print("attributs: ", attributs)

        return attributs

    @classmethod
    def from_widgets(cls, widgets: List[Any]):
        new_widgets = {}
        widgets[3][1] = Genre(widgets[3][1].get())
        print(widgets[3][0])
        print(widgets[3][1])

        new_widgets["title"] = widgets[0][1].get()
        new_widgets["author"] = widgets[1][1].get()
        new_widgets["synopsis"] = widgets[2][1].get()
        new_widgets["genre"] = widgets[3][1]

        return cls(**new_widgets)



# book = Book(title="El conde de montecristo",
#             authors=["Dumas"],
#             synopsis="Dantes es llevado a una prisión en Monte-cristo "
#                      "en donde fragua su venganza",
#             publisher="Poche",
#             genre=Genre.FICTION)
#
# print("libro: ", book.to_dict())
# print("Atributos: ", Book.get_attribut_names())
