import pytest
from django.urls import reverse
from books.models import Author, Book
from typing import Any


@pytest.mark.django_db
class TestAuthorViews:
    """Test cases for Author views."""

    def test_author_list_view(self, client: Any, test_author: Author) -> None:
        """Test author list view returns correct response."""
        url = reverse('books:author-list')
        response = client.get(url)
        assert response.status_code == 200
        assert test_author in response.context['authors']

    def test_author_create_view(self, client: Any) -> None:
        """Test author creation through view."""
        url = reverse('books:author-create')
        data = {
            'first_name': 'New',
            'last_name': 'Author',
            'bio': 'Test bio'
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert Author.objects.filter(last_name='Author').exists()


@pytest.mark.django_db
class TestBookViews:
    """Test cases for Book views."""

    def test_book_detail_view(self, client: Any, test_book: Book) -> None:
        """Test book detail view returns correct book."""
        url = reverse('books:book-detail', kwargs={'pk': test_book.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert response.context['book'] == test_book

    def test_book_delete_view(self, client: Any, test_book: Book) -> None:
        """Test book deletion through view."""
        url = reverse('books:book-delete', kwargs={'pk': test_book.pk})
        response = client.post(url)
        assert response.status_code == 302
        assert not Book.objects.filter(pk=test_book.pk).exists()