from django.contrib import admin
from django.urls import path, include
from typing import List

urlpatterns: List = [
    path('admin/', admin.site.urls),
    path('', include('books.urls', namespace='books')),
]