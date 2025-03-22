"""
Library Management System

This Python program is a simple Library Management System that allows users to:
-Add books to the library
-Borrow books (if available)
-Return books to the library
-Display available books
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available :
            self.is_available = False
            return True
        return False

    def return_book(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title , author):
        book = Book(title, author)
        self.books.append(book)
        print(f'Book "{title}" by "{author}" is added to the library.')

    def display_books(self):
        print("----- Available books in Library -----")
        for book in self.books:
            if book.is_available:
                print(f'{book.title} by {book.author}')
        print()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.borrow()
                print(f'You have borrowed "{book.title}".')
                return
        print(f'Sorry, "{title}" is not available.')

    def return_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.return_book()
                print(f'You have returned "{book.title}".')
                return
        print(f'Sorry, "{title}" was not borrowed from this library.')

