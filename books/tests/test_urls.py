import pytest
from django.urls import reverse, resolve

from books.models import Author, Book
from books.views import (
    AuthorListView, AuthorDetailView,
    BookListView, BookDetailView
)
from typing import Any


@pytest.mark.parametrize(
    "url_name,view_class",
    [
        ('books:author-list', AuthorListView),
        ('books:book-list', BookListView),
    ]
)
def test_list_views(url_name: str, view_class: Any) -> None:
    """Test list views resolve to correct view classes."""
    url = reverse(url_name)
    assert resolve(url).func.view_class == view_class


@pytest.mark.django_db
def test_detail_views(client: Any, test_author: Author, test_book: Book) -> None:
    """Test detail views return 200 status code."""
    author_url = reverse('books:author-detail', kwargs={'pk': test_author.pk})
    book_url = reverse('books:book-detail', kwargs={'pk': test_book.pk})

    assert client.get(author_url).status_code == 200
    assert client.get(book_url).status_code == 200