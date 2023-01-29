BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификационный номер должен быть целым числом")
        if id_ < 0:
            raise ValueError("Идентификационный номер должен быть положительным")
        self.id = id_
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть записано текстом")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id!r}, name='{self.name!r}', pages={self.pages!r})"


book = Book(1, "test_name_1", 200)
if __name__ == '__main__':

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
