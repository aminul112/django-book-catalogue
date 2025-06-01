import pytest
from books.forms import AuthorForm, BookForm
from books.models import Author
from typing import Dict, Any


@pytest.mark.django_db
class TestAuthorForm:
    """Test cases for AuthorForm."""

    def test_valid_form(self) -> None:
        """Test valid author form submission."""
        form_data: Dict[str, Any] = {
            'first_name': 'Jane',
            'last_name': 'Austen',
            'bio': 'English novelist'
        }
        form = AuthorForm(data=form_data)
        assert form.is_valid()

    def test_invalid_form(self) -> None:
        """Test invalid author form submission."""
        form_data: Dict[str, Any] = {
            'first_name': '',
            'last_name': 'Anonymous'
        }
        form = AuthorForm(data=form_data)
        assert not form.is_valid()
        assert 'first_name' in form.errors


@pytest.mark.django_db
class TestBookForm:
    """Test cases for BookForm."""

    def test_valid_form(self, test_author: Author) -> None:
        """Test valid book form submission."""
        form_data: Dict[str, Any] = {
            'title': 'Pride and Prejudice',
            'author': test_author.id,
            'isbn': '9780141439518',
            'pages': 279
        }
        form = BookForm(data=form_data)
        assert form.is_valid()

    def test_isbn_validation(self, test_author: Author) -> None:
        """Test ISBN validation in form."""
        form_data: Dict[str, Any] = {
            'title': 'Invalid Book',
            'author': test_author.id,
            'isbn': 'invalid-isbn'
        }
        form = BookForm(data=form_data)
        assert not form.is_valid()
        assert 'isbn' in form.errors