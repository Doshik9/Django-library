from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'genre_type_id', 'publisher']
        help_texts = {
            'book_name': '',
            'author': '',
            'genre_type_id': '',
            'publisher': '',
        }