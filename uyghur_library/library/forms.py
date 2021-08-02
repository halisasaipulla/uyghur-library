from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('ISBN', 'title', 'author', 'pdf', 'cover')

    def check_book_isbn(self):
        book_isbn = self.cleaned_data.get('ISBN')
        if book_isbn == "":
            raise forms.ValidationError()
        for instance in Book.objects.all():
            if instance.ISBN != book_isbn:
                return book_isbn
            else:
                raise forms.ValidationError('There is already a book with ISBN: ' + book_isbn)
        

# just check to see if book with isbn exists, if yes, then alert
