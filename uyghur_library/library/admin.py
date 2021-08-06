from django.contrib import admin
from .models import Book,Post
# Register your models here.

class Books(admin.ModelAdmin):
    list_display = ("title", "author",'pdf', 'cover')

admin.site.register(Book, Books)

class Posts(admin.ModelAdmin):
    list_display = ("title", "content",'date_posted', 'author')

admin.site.register(Post)