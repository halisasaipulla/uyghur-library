from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('', views.home, name="library-home"),
    path('faq/', views.faq, name='faq'),
    path('search/', views.searchbar, name='search'),
    path('books/', views.book_list, name='book_list'),
    path('books/info/<str:isbn>', views.book_info, name='book_info'),
    path('books/info/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('books/info/<int:pk>/delete-comment/', views.delete_comment, name='delete-comment'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('contact/', views.contact, name='contact_us'),
]
