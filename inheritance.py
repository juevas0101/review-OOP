class LibraryBook:
    def __init__(self, title, code_number, publisher_year):
        self.title = title
        self.code_number = code_number
        self.publisher_date = publisher_year


class Book(LibraryBook):
    def __int__(self, title, code_number, publisher_year, author):
        super().__init__(title, code_number, publisher_year)
        self.author = author

    def __repr__(self):
        return f'Title: {self.title} , Code Number: {self.code_number} , Publisher Year: {self.publisher_date}, Author: {self.author}'

book = ('The Book', 435, 2013, 'John Smith')
print(book)

book2 = ('A House', 485, 1990, 'Maria Gonzalez')
print(book2)
