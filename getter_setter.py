class Book:
    def __init__(self, title, author, publisher_date, available):
        self.__title = title
        self.__author = author
        self.__publisher_date = publisher_date
        self.__available = available

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_tile):
        if isinstance(new_tile, str):
            self.__title = new_tile
        else:
            raise ValueError('The title being a string')

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, str):
            self.__author = new_author
        else:
            raise ValueError('The author being a string')

    @property
    def publisher_date(self):
        return (self.__publisher_date)

    @publisher_date.setter
    def publisher_date(self, new_publisher):
        if isinstance(new_publisher, int):
            self.__publisher_date = new_publisher
        else:
            raise ValueError('The publisher date being int')

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, available_bool):
        if isinstance(available_bool, bool):
            self.__available = available_bool
        else:
            raise ValueError('The available must be the boolean type')

    def lend(self):
        if self.__available == True:
            self.__available = False
            return f'BOOK: {self.__title}'
        else:
            return f'BOOK: {self.__title} unavailable'

    def giveback(self):
        if self.__available == False:
            self.__available = True
            return f'BOOK: {self.__available} successfully returned'

book = Book('The House', 'Maria Doe', 2010, True)

print(book.title)
print(book.author)
print(book.publisher_date)
print(book.available)

print(book.lend())
print(book.lend())
print(book.giveback())
print(book.lend())

book.title = 'Python II'
book.author = 'Maria Gonzalez'
book.publisher_date = 1998
book.available = False

print(book.title)
print(book.author)
print(book.publisher_date)
print(book.available)

print(book.giveback())
print(book.lend())
