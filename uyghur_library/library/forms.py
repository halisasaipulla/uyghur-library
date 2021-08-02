from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')
        # fields = ('isbn','title', 'author', 'pdf', 'cover')



        # if isbn in the database, printout alert "we alreday have this book"
        #else 