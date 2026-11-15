
from datetime import date, timedelta


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = {}


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully!")

    def remove_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        if self.books[book_id].is_issued:
            raise ValueError("Cannot remove an issued book")

        del self.books[book_id]
        print("Book removed successfully!")

    def register_member(self, member):
        self.members[member.member_id] = member
        print("Member registered successfully!")

    def search_book(self, title):
        for book in self.books.values():
            if title.lower() in book.title.lower():
                return book
        return None

    def issue_book(self, book_id, member_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        if member_id not in self.members:
            raise ValueError("Member not found")

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_issued:
            raise ValueError("Book is already issued")

        book.is_issued = True
        due_date = date.today() + timedelta(days=14)
        member.borrowed_books[book_id] = due_date

        print("Book issued successfully!")
        print("Due Date:", due_date)

    def return_book(self, book_id, member_id, return_date=None):
        if member_id not in self.members:
            raise ValueError("Member not found")

        member = self.members[member_id]

        if book_id not in member.borrowed_books:
            raise ValueError("This book was not borrowed by this member")

        due_date = member.borrowed_books[book_id]

        if return_date is None:
            return_date = date.today()

        late_days = max(0, (return_date - due_date).days)
        fine = late_days * 5

        self.books[book_id].is_issued = False
        del member.borrowed_books[book_id]

        print("Book returned successfully!")
        print("Late Days:", late_days)
        print("Fine: Rs.", fine)

        return fine


# Main program

library = Library()

book1 = Book(101, "Python Programming", "John")
book2 = Book(102, "Data Structures", "James")

member1 = Member(1, "Maneesha")

library.add_book(book1)
library.add_book(book2)

library.register_member(member1)

print("\nSearching Book:")
result = library.search_book("Python")

if result:
    print("Book Found:", result.title)
else:
    print("Book Not Found")

print("\nIssuing Book:")
library.issue_book(101, 1)

print("\nReturning Book:")
library.return_book(101, 1)
