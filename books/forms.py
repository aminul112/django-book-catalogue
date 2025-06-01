from django import forms
from .models import Author, Book
from typing import Any, Dict


class AuthorForm(forms.ModelForm):
    """Form for creating and updating Author instances."""
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self) -> Dict[str, Any]:
        """Custom validation for the author form."""
        cleaned_data = super().clean()
        # Add any custom validation here
        return cleaned_data


class BookForm(forms.ModelForm):
    """Form for creating and updating Book instances."""
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'summary': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_isbn(self) -> str:
        """Validate the ISBN field."""
        isbn = self.cleaned_data['isbn']
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN should contain only digits.")
        if len(isbn) not in (10, 13):
            raise forms.ValidationError("ISBN must be 10 or 13 digits long.")
        return isbn