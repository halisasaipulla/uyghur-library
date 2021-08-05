from os import name
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from .forms import BookForm
from .models import Book
from django.contrib import messages

def home(request):
    trans = translate(language='fr')
    return render(request, 'library/home.html', {'trans': trans})

def translate(language):
    current_language = get_language()
    try:
        activate(language)
        text=gettext('Library')
    finally:
        activate(current_language)
    return text

def about(request):
    return render(request, 'library/about.html')

def searchbar(request):
    if request.method=="GET":
        search = request.GET.get('q')
        book = Book.objects.all().filter(title__icontains=search)
        return render(request, 'library/search.html', {'book':book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books
    })

def book_info(request, isbn):
    book = get_object_or_404(Book, ISBN=isbn)
    return render(request, 'library/book_info.html', {'book':book})

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            check_book = Book.objects.filter(ISBN=request.POST['ISBN'])
            if not check_book:
                form.save()
                return redirect('book_list')
            else:
                messages.error(request, 'Book already exists.')
                return render(request, 'library/upload_book.html', {'form': BookForm()})
    else:
        form = BookForm()
    return render(request, 'library/upload_book.html', {
        'form': form
    })

def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

