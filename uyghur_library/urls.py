from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from library import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('', include('library.urls')),
    path('faq/', views.faq, name='faq'),
    path('search/', views.searchbar, name='search'),
    path('books/', views.book_list, name='book_list'),
    path('books/info/<str:isbn>/', views.book_info, name='book_info'),
    path('books/info/<str:isbn>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('books/info/<str:isbn>/add_comment/', views.add_comment, name='add_comment'),
    path('books/info/<str:isbn>/delete-comment/<int:comment_pk>/', views.delete_comment, name='delete-comment'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/<str:isbn>/remove_favorite/', user_views.remove_favorite, name='remove_favorite'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('contact/', views.contact, name='contact_us'),
]

urlpatterns += i18n_patterns (
    path('', include('library.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)