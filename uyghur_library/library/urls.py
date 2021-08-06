from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from library.views import (
    # PostListView,
    # PostDetailView,
    PostCreateView,
    # PostUpdateView,
    # PostDeleteView
)

urlpatterns = [
    path('', views.home, name="library-home"),
    path('faq/', views.faq, name='faq'),
    path('search/', views.searchbar, name='search'),
    path('books/', views.book_list, name='book_list'),
    path('books/info/<str:isbn>', views.book_info, name='book_info'),
    # path('', PostListView.as_view(), name='book_info2'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('books/info/<str:isbn>/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<str:isbn>/', views.delete_book, name='delete_book'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('contact/', views.contact, name='contact_us'),
]
