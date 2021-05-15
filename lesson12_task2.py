from operator import attrgetter, itemgetter, methodcaller

class Library:
    book_dict = {}

    def __init__(self, libr_name, books: list, authors: list):
        self.libr_name = libr_name
        self.books = books
        self.authors = authors

    def __str__(self):
        return f'Library name is {self.libr_name}'

    def __repr__(self):
        return repr((self.books, self.authors))

############################################################################
    def new_book(self, name: str, year: int, author):
        self.books.append(name)
        self.authors.append(author)
        self.book_dict[name] = author, year
        return self.book_dict

    def group_by_author(self):
        return sorted(self.book_dict)


############################################################################
class Book:
    name = ''
    year = ''
    author = ''
    amount = ''
    def __init__(self, name: str, year: int, author: str):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.name}, {self.year}, {self.author}'

    def __repr__(self):
        return f'{self.name}, {self.year}, {self.author}'

class Author:
    def __init__(self, name: str, country: str, bdate: int, books: list):
        self.name = name
        self.country = country
        self.bdate = bdate
        self.books = books

    def __str__(self):
        return f'{self.name}, {self.country}, {self.bdate}, {self.books}'

    def __repr__(self):
        return f'{self.name}'


###################################################################################################
'''Объявление библиотеки'''
new_lib = Library('Great Library', [], [])
###################################################################################################
'''Объявление авторов как экземпляров класса Author'''
rock_star = Author('Rock Star', 'USA', 1993, ['Business story', 'GTA Story', 'Black & White'])
marvels = Author('Marvell', 'USA', 1956, ['Marvels Avengers', 'Winter soldier', 'Spider Man'])
stop_game = Author('StopGame', 'Ukraine', 2000, ['Review on Resident Evil 1', 'Games as painting'])
book_author = Author('Bookau', 'Malaysia', 2010, ['About BOOK', 'Book for dogs'])
###################################################################################################
'''Объявление книг как экземпляров класса Book'''
RS_gta_book = Book(rock_star.books[1], 2020, rock_star.name)
RS_business_book = Book(rock_star.books[0], 2015, rock_star.name)
M_avengers_book = Book(marvels.books[0], 1961, marvels.name)
M_spider_book = Book(marvels.books[2], 1975, marvels.name)
sg_review_book = Book(stop_game.books[0], 2012, stop_game.name)
ba_dog_book = Book(book_author.books[1], 2011, book_author.name)
###################################################################################################
'''Добавление книг в библиотеку'''
new_lib.new_book(RS_gta_book.name, RS_gta_book.year, RS_gta_book.author)
new_lib.new_book(M_avengers_book.name, M_avengers_book.year, M_avengers_book.author)
new_lib.new_book(M_spider_book.name, M_spider_book.year, M_spider_book.author)
new_lib.new_book(RS_business_book.name, RS_business_book.year, RS_business_book.author)
# new_lib.new_book(sg_review_book.name, sg_review_book.year, sg_review_book.author)
# new_lib.new_book(ba_dog_book.name,ba_dog_book.year, ba_dog_book.author)
###################################################################################################
'''Выводим на экран название библиотеки, авторов и книг'''
# print(new_lib.libr_name)
print(new_lib.books)
print(new_lib.authors)
print(new_lib.book_dict)
print(new_lib.group_by_author())

###################################################################################################
