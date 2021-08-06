"""uyghur_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from library import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from library.views import (
    # PostListView,
    # PostDetailView,
    PostCreateView,
    # PostUpdateView,
    # PostDeleteView
)

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('', include('library.urls')),
    path('faq/', views.faq, name='faq'),
    path('search/', views.searchbar, name='search'),
    path('books/', views.book_list, name='book_list'),
    path('books/info/<str:isbn>', views.book_info, name='book_info'),
    # path('', PostListView.as_view(), name='book_info'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('books/info/<str:isbn>/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('contact/', views.contact, name='contact_us'),
]

urlpatterns += i18n_patterns (
    path('', include('library.urls')),
)
# just for development purposes
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)