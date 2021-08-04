from os import name
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

def home(request):
    return render(request, 'library/home.html')

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

def book_info(request):
    return render(request, 'library/book_info.html')

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            check_book = Book.objects.filter(ISBN=request.POST['ISBN'])
            if not check_book:
                form.save()
            else:
                return redirect('book_list')
        return redirect('book_list')
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

