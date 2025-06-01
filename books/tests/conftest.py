import pytest
from django.contrib.auth.models import User
from books.models import Author, Book
from typing import Generator

@pytest.fixture
def test_user() -> Generator[User, None, None]:
    """Fixture for creating a test user."""
    user = User.objects.create_user(
        username='testuser',
        password='testpass123'
    )
    yield user
    user.delete()

@pytest.fixture
def test_author() -> Generator[Author, None, None]:
    """Fixture for creating a test author."""
    author = Author.objects.create(
        first_name='John',
        last_name='Doe',
        bio='Test biography',
        birth_date='1980-01-01'
    )
    yield author
    author.delete()

@pytest.fixture
def test_book(test_author: Author) -> Generator[Book, None, None]:
    """Fixture for creating a test book with author dependency."""
    book = Book.objects.create(
        title='Test Book',
        author=test_author,
        isbn='1234567890123',
        summary='Test summary',
        pages=200
    )
    yield book
    book.delete()