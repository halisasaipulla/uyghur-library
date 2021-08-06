from os import name
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from .forms import BookForm
from .models import Book
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

from django.http import HttpResponse
from django.core.mail import send_mail

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
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books
    })

def book_info(request, isbn):
    book = get_object_or_404(Book, ISBN=isbn)
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

        message.save()
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



class PostListView(ListView):
    model = Post
    template_name = 'library/book_info.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'library/book_info.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

