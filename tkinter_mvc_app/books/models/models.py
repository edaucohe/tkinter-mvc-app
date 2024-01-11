from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from my_enums import Genre, Language


@dataclass
class Book:
    title: str
    authors: List[str]
    synopsis: str
    publisher: str
    genre: List[Genre]
    original_language: Language
    book_language: Language
    number_of_pages: int
    current_page: int
    created_date: date = date.today()
    purchase_date: Optional[date] = None
    publication_date: Optional[date] = None
    reading_date: Optional[date] = None
    already_read: bool = False
    is_current_book: bool = False
