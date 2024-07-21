from Library import Library

class Student:
    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId
        self.borrowedBooks = []

    def borrowBook(self, book):
        if book.status == "available":
            book.borrows()
            self.borrowedBooks.append(book)
            Library.borrowed_books.append(book)
            print(f"{book.title} is now on your tab for 7 days")
        else:
            print(f"Sorry, {book.title} is not available")

    def return_book(self, book):
        if book.status == "borrowed":
            book.returns()
            self.borrowedBooks.remove(book)
            Library.borrowed_books.remove(book)
            print(f"{book.title} has been returned")
        else:
            print(f"{book.title} is already on shelf")

    def my_borrowed_books(self):
        print("Your borrowed books are:")
        if len(self.borrowedBooks) > 0:
            for e in self.borrowedBooks:
                print(e)
        else:
            print("You have not borrowed any books")

    def renew_borrowed_book(self, book):
        if book.status == "borrowed":
            print(f"You have an additional 7 days to return {book.title}")

