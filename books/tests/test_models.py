import pytest
from django.core.exceptions import ValidationError
from books.models import Author, Book
from typing import Any


@pytest.mark.django_db
class TestAuthorModel:
    """Test cases for Author model."""

    def test_author_creation(self, test_author: Author) -> None:
        """Test author creation and string representation."""
        assert str(test_author) == 'John Doe'
        assert test_author.first_name == 'John'
        assert test_author.bio == 'Test biography'

    def test_author_ordering(self) -> None:
        """Test authors are ordered by last name, then first name."""
        Author.objects.create(first_name='B', last_name='B')
        Author.objects.create(first_name='A', last_name='A')
        authors = list(Author.objects.all())
        assert authors[0].last_name == 'A'
        assert authors[1].last_name == 'B'


@pytest.mark.django_db
class TestBookModel:
    """Test cases for Book model."""

    def test_book_creation(self, test_book: Book) -> None:
        """Test book creation and string representation."""
        assert str(test_book) == 'Test Book'
        assert test_book.pages == 200
        assert test_book.isbn == '1234567890123'

