from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from .forms import BookForm, CommentForm
from .models import Book, Category, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User

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

def faq(request):
    return render(request, 'library/faq.html')

def searchbar(request):
    if request.method=="GET":
        search = request.GET.get('q')
        if search:
            book = Book.objects.all().filter(title__icontains=search)
            return render(request, 'library/search.html', {'book':book})
        else:
            return render(request, 'library/home.html')

def book_list(request):
    category = request.GET.get('category')
    if category == None:
        
            books = Book.objects.all()
    else:
        books = Book.objects.filter(category__name=category)
    categories = Category.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books,
        'categories':categories
    })

def book_info(request, isbn):
    book = get_object_or_404(Book, ISBN=isbn)
    num_comments = Comment.objects.filter(book=book).count()
    return render(request, 'library/book_info.html', {'book':book, 'num_comments': num_comments})


def add_comment(request, pk):
    book = get_object_or_404(Book, id=pk)

    form = CommentForm(instance=book)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(book=book, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect(reverse('book_info', args=[pk]))
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    

    context = {
        'form': form
    }

    return render(request, 'library/add_comment.html', context)


def delete_comment(request, pk):
    comment = Comment.objects.filter(book=pk).last()
    book_id = comment.book.id
    comment.delete()
    return redirect(reverse('book_info', args=[book_id]))

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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])

        send_mail(data['subject'], message, '', ['capstoneprojectadac15@gmail.com'])
    return render(request, 'library/contact_us.html', {})

