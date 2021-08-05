from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('', views.home, name="library-home"),
    path('about/', views.about, name='about'),
    path('search/', views.searchbar, name='search'),
    path('books/', views.book_list, name='book_list'),
    path('books/info', views.book_info, name='book_info'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
