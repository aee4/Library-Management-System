from C_Students import Student
from Librarian import Librarian



class Library:
    books = []
    borrowed_books = []

    def __init__(self):
        self.students = []
        self.librarians = []

    def add_student(self, student, name, studentId):
        student_new = Student(name, studentId)
        self.students.append(student_new)
        print(f"Student '{student_new.name}' has been added to the library system.")

    def add_librarian(self, name, employee_id):
        librarian_new = Librarian(name, employee_id)
        self.librarians.append(librarian_new)
        print(f"Librarian '{librarian_new.name}' has been added to the library system.")

    def book_by_ISBN(self, ISBN_check):

        for book in self.books:
            if book.ISBN == ISBN_check:
                print(f"{book} is a match for ISBN: {ISBN_check}")
                break
        else:
            print(f"No match for {ISBN_check}")

    def get_all_books(self):
        return self.books

    def list_all_borrowed_books(self):
        return self.borrowed_books
