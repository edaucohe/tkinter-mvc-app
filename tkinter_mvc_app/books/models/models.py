import dataclasses
import inspect
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional, Dict, get_type_hints, get_origin, Any

from tkinter_mvc_app.books.models.my_enums import Language, Genre
from tkinter_mvc_app.helpers.const import FIRST_MEMBER_POS, ATTR_POS


@dataclass
class Book:
    title: Optional[str] = "Sin título"
    author: Optional[str] = "Desconocido"
    synopsis: Optional[str] = "Sin sinopsis"
    genre: Optional[Genre] = None
    publisher: str = "Desconocido"
    original_language: Optional[Language] = None
    book_language: Optional[Language] = None
    number_of_pages: Optional[int] = None
    current_page: Optional[None] = 0
    created_date: Optional[date] = None
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

    @classmethod
    def deserialize_from_user(cls, book_data: Dict[str, str]) -> 'Book':
        data = dict()
        data["title"] = book_data["title"]
        data["author"] = book_data["author"]
        data["synopsis"] = book_data["synopsis"]
        data["genre"] = None if book_data["genre"] == "" else Genre(book_data["genre"])
        data["publisher"] = book_data["publisher"]
        data["original_language"] = None if book_data["original_language"] == "" else Language(book_data["original_language"])
        data["book_language"] = None if book_data["book_language"] == "" else Language(book_data["book_language"])
        data["number_of_pages"] = cls.to_integer(book_data["number_of_pages"])
        data["current_page"] = cls.current_page if book_data["current_page"] == "" else cls.to_integer(book_data["current_page"])
        data["created_date"] = date.today()
        data["purchase_date"] = cls.to_date(book_data["purchase_date"])
        data["publication_date"] = cls.to_date(book_data["publication_date"])
        data["reading_date"] = cls.to_date(book_data["reading_date"])
        data["already_read"] = bool(book_data["already_read"])
        data["is_current_book"] = bool(book_data["is_current_book"])

        return cls(**data)

    @staticmethod
    def to_integer(number_as_str: str):
        if number_as_str.isdigit():
            return int(number_as_str)
        else:
            print("Data is not a number")
            return None

    @staticmethod
    def to_date(date_as_str):
        if date_as_str == "":
            print("There is no date")
            return None
        else:
            new_date = date_as_str.split("-")
            new_date.reverse()
            new_date = "-".join(new_date)
            return date.fromisoformat(new_date)




# book = Book(title="El conde de montecristo",
#             authors=["Dumas"],
#             synopsis="Dantes es llevado a una prisión en Monte-cristo "
#                      "en donde fragua su venganza",
#             publisher="Poche",
#             genre=Genre.FICTION)
#
# print("libro: ", book.to_dict())
# print("Atributos: ", Book.get_attribut_names())
