class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта Book

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("Param id_ must be of type int.")
        if id_ < 0:
            raise ValueError("Param id_ must be a non-negative number")
        if not isinstance(name, str):
            raise TypeError("Param name must be of type string.")
        if not isinstance(pages, int):
            raise TypeError("Param pages must be of type int.")
        if id_ <= 0:
            raise ValueError("Param pages must be a positive number")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Получение представления о книги в формате: Книга "название_книги"

        :return: Строка формата: Книга "название_книги"
        """
        return f'Книга {self.name}'

    def __repr__(self) -> str:
        """
        Получение валидной python строки, по которой можно инициализировать точно такой же экземпляр

        :return: Python строка для инициализации экземпляра Book
        """
        return f'Book(id_={self.id_}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __int__(self, books=None):
        """
        Инициализация объекта Library

        :param books: Необязательный аргумент, список книг
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Получение идентификатора для добавления новой книги

        :return: id для новой книги + 1 или 1, если книг нет
        """
        if not self.books:
            return 1

        return max(book.id_ for book in self.books) + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Получение индекса книги по id

        :param id_: id книги

        :return: Индекс книги с указанным id в списке
        """
        if not isinstance(id_, int):
            raise TypeError("Param id_ must be of type int.")
        if id_ <= 0:
            raise ValueError("Param id_ must be a positive number")

        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index

        raise ValueError("Книги с запрашиваемым id не существует")
