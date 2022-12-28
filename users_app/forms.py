from django import forms
from books_app.models import UserBook


class UserForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['reader', 'book', 'return_date']
        help_texts = {
            'reader': '',
            'book': '',
            'return_date': '',
        }