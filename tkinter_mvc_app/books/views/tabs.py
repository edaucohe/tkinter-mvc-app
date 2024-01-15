from tkinter import ttk

from tkinter_mvc_app.books.views.frames import BookFrame


class BookTab(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        # Create book frame
        self.book_frame = BookFrame(self)
        self.book_frame.grid(row=0, column=0, sticky="nsew")
        self.add(self.book_frame, text="Libros")

#         # Create boardgame frame
#         self.boardgame_frame = BoardgameFrame(self)
#         self.boardgame_frame.grid(row=0, column=0, sticky="nsew")
#         self.add(self.boardgame_frame, text="Juegos de mesa")
#
#
# class BoardgameFrame(ttk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#
#         # Setup boardgame grid
#         self.grid_columnconfigure(index=0, weight=0)
#         self.grid_columnconfigure(index=1, weight=1)
#         self.grid_columnconfigure(index=2, weight=2)
#         self.grid_rowconfigure(index=(0, 1, 2, 3, 4, 5), weight=1)
#
#         # Label widgets
#         self.title_label = ttk.Label(self, text="Título", background="cyan")
#         self.title_label.grid(row=0, column=0, sticky="nsew")
#         self.title_input = ttk.Entry(self)
#         self.title_input.grid(row=0, column=1, sticky="nsew")
#
#         self.autor_label = ttk.Label(self, text="Diseñadores", background="orange")
#         self.autor_label.grid(row=1, column=0, sticky="nsew")
#         self.author_input = ttk.Entry(self)
#         self.author_input.grid(row=1, column=1, sticky="nsew")
