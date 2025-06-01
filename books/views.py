from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book
from .forms import AuthorForm, BookForm
from typing import Any


class HomeView(View):
    """Home page view."""
    def get(self, request, *args, **kwargs) -> Any:
        """Handle GET request for home page."""
        return render(request, 'books/base.html')


class AuthorListView(ListView):
    """View for listing all authors."""
    model = Author
    template_name = 'books/author_list.html'
    context_object_name = 'authors'


class AuthorDetailView(DetailView):
    """View for showing author details."""
    model = Author
    template_name = 'books/author_detail.html'


class AuthorCreateView(CreateView):
    """View for creating a new author."""
    model = Author
    form_class = AuthorForm
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('books:author-list')


class AuthorUpdateView(UpdateView):
    """View for updating an existing author."""
    model = Author
    form_class = AuthorForm
    template_name = 'books/author_form.html'
    success_url = reverse_lazy('books:author-list')


class AuthorDeleteView(DeleteView):
    """View for deleting an author."""
    model = Author
    template_name = 'books/author_confirm_delete.html'
    success_url = reverse_lazy('books:author-list')


class BookListView(ListView):
    """View for listing all books."""
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    """View for showing book details."""
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(CreateView):
    """View for creating a new book."""
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book-list')


class BookUpdateView(UpdateView):
    """View for updating an existing book."""
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book-list')


class BookDeleteView(DeleteView):
    """View for deleting a book."""
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book-list')