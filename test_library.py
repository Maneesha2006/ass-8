
import pytest
from datetime import date, timedelta

from library import Book, Member, Library


@pytest.fixture
def setup_library():
    library = Library()

    book1 = Book(101, "Python Programming", "John")
    book2 = Book(102, "Data Structures", "James")

    member1 = Member(1, "Maneesha")

    library.add_book(book1)
    library.add_book(book2)
    library.register_member(member1)

    return library


def test_add_book(setup_library):
    assert 101 in setup_library.books


def test_remove_book(setup_library):
    setup_library.remove_book(102)
    assert 102 not in setup_library.books


def test_register_member(setup_library):
    assert 1 in setup_library.members


def test_issue_book(setup_library):
    setup_library.issue_book(101, 1)
    assert setup_library.books[101].is_issued is True


def test_double_borrowing(setup_library):
    setup_library.issue_book(101, 1)

    with pytest.raises(ValueError):
        setup_library.issue_book(101, 1)


def test_late_fine_calculation(setup_library):
    setup_library.issue_book(101, 1)

    due_date = setup_library.members[1].borrowed_books[101]
    return_date = due_date + timedelta(days=5)

    fine = setup_library.return_book(101, 1, return_date)

    assert fine == 25
