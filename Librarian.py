from Library import Library
from Book import Book


class Librarian:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def add_book(self, title, author, ISBN, publicationYear, status):
        new_book = Book(title, author, ISBN, publicationYear, status)
        Library.books.append(new_book)
        print(f"{new_book.title} by {new_book.author} has been added to the library")

    def remove_book(self, removed_book):
        removed_book = removed_book
        Library.books.remove(removed_book)
        print(f" Book has been removed from the library")

    def view_all_books(self):
        print("All books in the library are: ")
        for book in Library.books:
            print(book)

    def view_all_borrowed_books(self):
        print("All borrowed books in the library are: ")
        for book in Library.borrowed_books:
            print(book)

    def view_all_available_books(self):
        print("Available books are:")
        for book in Library.books:
            if book.status == "available":
                print(book)

    def update_book_status(self, book, status):
        book.status = status
        print(f"{book.title} is now  {status}")
