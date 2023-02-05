class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """ Возвращает название книги"""
        return self._name

    @property
    def author(self) -> str:
        """ Возвращает автора книги"""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """ Возвращает количество страниц в книге"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if new_pages <= 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self._pages = new_pages

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}. Кол-во страниц {self.pages}'  # Если необходимо указать количество страниц, то перегружаем метод.
        # Если для пользователя достаточно знать автора и название книги, то этот метод может быть унаследован из класса Book.

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """ Возвращает продолжительность аудиокниги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность аудиокниги."""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть числом с плавающей запятой")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги не может быть отрицательной")
        self._duration = new_duration

    def __str__(self):
        return f'Книга "{self.name}". Автор {self.author}. Продолжительность {self.duration} (час.)'  # Если необходимо знать продолжительность аудиокниги, то перегружаем метод.
        # Если для пользователя достаточно знать автора и название книги, то этот метод может быть унаследован из класса Book.

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


