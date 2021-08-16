from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from library.models import Book, Comment
from django.db.models import Avg


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('library-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    favorite_books = user.favorite.all()
    context = {
        'favorite_books': favorite_books,
    }
    return render(request, 'users/profile.html', context)
    

def remove_favorite(request, isbn):
    book = get_object_or_404(Book, ISBN=isbn)
    book.favorite.remove(request.user)
    return redirect(reverse('profile'))  
