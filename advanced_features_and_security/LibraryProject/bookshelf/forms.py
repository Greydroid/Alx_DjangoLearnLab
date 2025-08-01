# bookshelf/forms.py

from django import forms
from .models import Book  # Adjust based on your model name

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # match your model fields

