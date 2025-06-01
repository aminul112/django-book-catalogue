from django.db import models
from django.urls import reverse
from typing import Optional


class Author(models.Model):
    """
    Represents an author in the book catalogue.

    Attributes:
        first_name (str): Author's first name
        last_name (str): Author's last name
        bio (str, optional): Short biography
        birth_date (date, optional): Date of birth
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self) -> str:
        """String representation of the author."""
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self) -> str:
        """Returns URL to access a particular author instance."""
        return reverse("author-detail", kwargs={"pk": self.pk})


class Book(models.Model):
    """
    Represents a book in the catalogue.

    Attributes:
        title (str): Book title
        author (Author): Book author (foreign key)
        summary (str, optional): Brief description
        isbn (str): International Standard Book Number
        published_date (date, optional): Publication date
        pages (int, optional): Number of pages
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    summary = models.TextField(blank=True, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    published_date = models.DateField(blank=True, null=True)
    pages = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        """String representation of the book."""
        return self.title

    def get_absolute_url(self) -> str:
        """Returns URL to access a particular book instance."""
        return reverse("book-detail", kwargs={"pk": self.pk})
