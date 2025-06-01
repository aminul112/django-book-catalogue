from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin interface configuration for Author model."""

    list_display = ("last_name", "first_name", "birth_date")
    list_filter = ("last_name", "birth_date")
    search_fields = ("last_name", "first_name")
    fieldsets = (
        (None, {"fields": ("first_name", "last_name")}),
        (
            "Additional Info",
            {"fields": ("bio", "birth_date"), "classes": ("collapse",)},
        ),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin interface configuration for Book model."""

    list_display = ("title", "author", "published_date")
    list_filter = ("author", "published_date")
    search_fields = ("title", "author__last_name", "isbn")
    fieldsets = (
        (None, {"fields": ("title", "author", "isbn")}),
        (
            "Details",
            {
                "fields": ("summary", "published_date", "pages"),
                "classes": ("collapse",),
            },
        ),
    )
