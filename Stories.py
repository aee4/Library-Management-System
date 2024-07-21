from Book import Book
from Librarian import Librarian
from Library import Library
from C_Students import Student



Student_one = Student("Emmanuel", "101")
Student_two = Student("Emmanuella", "102")

Storybook1 = Book("Cinderella", "Eyram ", 400, 2024, "available")
Textbook1 = Book("Aki-Ola Math", "Emmanuel", 300, 2024, "available")
Storybook2 = Book("Beauty and the Beast", "Korku", 200, 2024, "available")
Textbook3 = Book("Atta Kay Physics", "Agbetor", 100, 2024, "available")

Librarian_one = Librarian("Daniel", "899")
Librarian_two = Librarian("Daniella", "799")

Library = Library()
Library.books.append(Storybook1)
Library.books.append(Textbook1)
Library.books.append(Storybook2)
Library.books.append(Textbook3)

# stories
# Book
Book.status_check(Storybook1)
Librarian.update_book_status(Librarian_one, Storybook1, 'borrowed')
Book.getDetails(Storybook1)
Librarian.add_book(Librarian_two, "Cars", "kofi", 800, 2021, "available")

# Student
Student.borrowBook(Student_two, Textbook1)
Student.borrowBook(Student_one, Textbook3)
Student.return_book(Student_two, Textbook1)
Student.my_borrowed_books(Student_one)
Student.renew_borrowed_book(Student_one, Textbook3)

# Librarian
Librarian.view_all_books(Librarian_two)
Librarian.remove_book(Librarian_two, Storybook1)
Librarian.view_all_borrowed_books(Librarian_two)
Library.add_student(Librarian_one, 'Jedel', "3443")

# Library
Library.add_student(Librarian_one, 'Joel', "3400")
Library.add_librarian('Elikpem', "7990")
Library.book_by_ISBN(100)
Librarian.view_all_available_books(Librarian_two)