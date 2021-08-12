from django.contrib import admin
from .models import Book, Comment, Category
# Register your models here.

class Books(admin.ModelAdmin):
    list_display = ("title", "author",'pdf', 'cover', 'category')

class Posts(admin.ModelAdmin):
    list_display = ("commenter_name", "comment_body", 'date_added')

admin.site.register(Book, Books)
admin.site.register(Comment)
admin.site.register(Category)

