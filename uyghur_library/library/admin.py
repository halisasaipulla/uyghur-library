from django.contrib import admin
from .models import Book
# Register your models here.

class Books(admin.ModelAdmin):
    list_display = ("title", "author",'pdf', 'cover')

admin.site.register(Book, Books)