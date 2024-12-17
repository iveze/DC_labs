import doctest


class Backpack:
    def __init__(self, books_capacity: int, books_occupied: int):
        """
        Создание и подготовка к работе объекта "Рюкзак"

        :param books_capacity: Количество книг, которое вмещает рюкзак
        :param books_occupied: Текущее количество книг

        Примеры:
        >>> my_backpack = Backpack(30, 5) #инициализация экземпляра класса
        """
        if not isinstance(books_capacity, int):
            raise TypeError("Объём рюкзака должен быть типа int.")
        if books_capacity <= 0:
            raise ValueError("Объём рюкзака должен быть положительным числом.")
        self.books_capacity = books_capacity

        if not isinstance(books_occupied, int):
            raise TypeError("Занимаемый книгами объём должен быть типа int.")
        if books_occupied < 0:
            raise ValueError("Количество книг не может быть отрицательным числом.")
        self.occupied_volume = books_occupied

    def is_empty_backpack(self) -> bool:
        """
        Функция, которая проверяет, является ли рюкзак пустым

        :return: Является ли рюкзак пустым

        Примеры:
        >>> my_backpack = Backpack(30, 5)
        >>> my_backpack.is_empty_backpack()
        """
        ...

    def add_books_to_backpack(self, books: int) -> None:
        """
        Добавление книг в рюкзак.
        :param books: Количество добавляемых книг

        :raise ValueError: Если количество добавляемых книг превышает свободное место в рюкзаке, то вызываем ошибку

        Примеры:
        >>> my_backpack = Backpack(30, 5)
        >>> my_backpack.add_books_to_backpack(20)
        """
        if not isinstance(books, int):
            raise TypeError("Количество добавляемых книг должно быть типа int.")
        if books <= 0:
            raise ValueError("Количество добавляемых книг должно быть положительным числом.")
        ...

    def remove_books_from_backpack(self, books: int) -> None:
        """
        Извлечение книг из рюкзака

        :param books: Количество извлекаемых книг
        :raise ValueError: Если количество извлекаемых книг превышает количество книг в рюкзаке, то вызывается ошибка.

        Примеры:
        >>> my_backpack = Backpack(30, 30)
        >>> my_backpack.remove_books_from_backpack(25)
        """
        ...


class Library:
    def __init__(self, name: str, library_capacity: int):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param name: Название библиотеки
        :param library_capacity: Количество книг, которое может содержать библиотека

        Примеры:
        >>> library = Library("Friends Library", 1000)
        """
        if not isinstance(name, str):
            raise TypeError("Название библиотки должно быть типа string.")
        self.name = name

        if not isinstance(library_capacity, int):
            raise TypeError("Вместимость библиотки должна быть типа int.")
        if library_capacity <= 0:
            raise ValueError("Вместимость библиотеки должна быть положительным числом.")
        self.library_capacity = library_capacity

        self.books = []
        self.current_number_of_books = 0

    def add_book(self, book: str) -> None:
        """
        Добавление книги в библиотеку

        :param book: Название книги

        Примеры:
        >>> library = Library("Friends Library", 1000)
        >>> library.add_book("Fahrenheit 451")
        """
        if not isinstance(book, str):
            raise TypeError("Название книги должно быть типа string.")
        if self.current_number_of_books == self.library_capacity:
            raise ValueError("Достигнута максимальная вместимость библиотеки.")
        ...

    def borrow_book(self, book: str) -> str:
        """
        Взять книгу из библиотеки

        :param book: Название книги

        :return: Взятую книгу или же сообщение об ошибке, если книги нет или библиотека пуста

        Примеры:
        >>> library = Library("Friends Library", 1000)
        >>> library.borrow_book("Fahrenheit 451")
        """
        if not isinstance(book, str):
            raise TypeError("Название книги должно быть типа string.")
        ...

    def get_book_count(self) -> int:
        """
        Получить текущее количество книг в библиотеке.

        :return: Количество книг в библиотеке

        Примеры:
        >>> library = Library("Friends Library", 1000)
        >>> library.borrow_book("Fahrenheit 451")
        >>> library.get_book_count()
        """
        ...


class Phone:
    def __init__(self, memory: float):
        """
        Инициализация объекта Phone

        :param memory: Общая память телефона

        Примеры:
        >>> my_phone = Phone(512)
        """
        if not isinstance(memory, (int, float)):
            raise TypeError("The phone memory size must be of type int or float.")
        if memory <= 0:
            raise ValueError("The memory size must be a positive number")
        self.memory = memory

        self.apps = {}
        self.used_memory = 0

    def install_app(self, app_name: str, app_size: float) -> str:
        """
        Установить приложение на телефон.

        :param app_name: Название приложения
        :param app_size: Размер приложения

        :return: Сообщение о результате установки

        Примеры:
        >>> my_phone = Phone(512)
        >>> my_phone.install_app("YouTube", 100)
        """
        if not isinstance(app_name, str):
            raise TypeError("The app name must be of type string.")
        if not isinstance(app_size, (int, float)):
            raise ValueError("The app size must be of type int or float.")
        if app_size <= 0:
            raise ValueError("The app size must be a positive number.")
        if self.used_memory + app_size > self.memory:
            return f'Not enough memory to install {app_name}.'

        if app_name in self.apps:
            return f'{app_name} is already installed.'

        self.apps[app_name] = app_size
        self.used_memory += app_size
        return f'{app_name} installed successfully.'

    def uninstall_app(self, app_name: str) -> str:
        """
        Удалить приложение с телефона.

        :param app_name: Название приложения

        :return: Сообщение о результате удаления

        Примеры:
        >>> my_phone = Phone(512)
        >>> my_phone.install_app("YouTube", 100)
        >>> my_phone.uninstall_app("YouTube")
        """
        if not isinstance(app_name, str):
            raise TypeError("The app name must be of type string.")

        if app_name in self.apps:
            app_size = self.apps.pop(app_name)
            self.used_memory -= app_size
            return f'{app_name} uninstalled successfully.'
        else:
            return f'{app_name} not found.'

    def get_used_memory(self) -> float:
        """
        Получить текущее использование памяти.

        :return: Размер используемой памяти

        Примеры:
        >>> my_phone = Phone(512)
        >>> my_phone.install_app("YouTube", 100)
        >>> my_phone.get_used_memory()
        """
        return self.used_memory


if __name__ == "__main__":
    doctest.testmod()
