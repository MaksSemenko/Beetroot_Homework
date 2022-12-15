class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        self.authors.append(author)
        author.books.append(new_book.name)
        Book.all_books += 1
        return new_book

    def group_by_author(self, author):
        return author.books

    def group_by_year(self, year):
        return [i for i in self.books if i.year == year]

    def __repr__(self):
        return f'{self.name}, {self.books}, {self.authors}'

    def __str__(self):
        return f'{self.name}, {self.books}, {self.authors}'


class Book:
    all_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'{self.name}, {self.year}, {self.author}'

    def __str__(self):
        return f'{self.name}, {self.year}, {self.author}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'


author_1 = Author('Donna Tartt', 'USA', '23.12.1963')
author_2 = Author('Erich Maria Remarque', 'Germany', '22.06.1898')
my_library = Library('Poltava Regional Library')
my_library.new_book('The goldfinch', 2013, author_1)
my_library.new_book('Spark of Life', 1952, author_2)
my_library.new_book('Three Comrades', 1937, author_2)
print(my_library.group_by_author(author_1))
print(my_library.group_by_author(author_2))
print(my_library.group_by_year(2013))
