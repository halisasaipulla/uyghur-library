from django import forms
from .models import Book, Comment

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('ISBN', 'title', 'author','publishedYear', 'publisher','pdf', 'cover', 'category', 'summary')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body', 'rate',)


