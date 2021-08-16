from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    ISBN = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', default='books/covers/default.png',blank=True)
    category = models.ForeignKey('Category',on_delete=models.PROTECT,default=1)
    publishedYear=models.CharField(max_length=100, default='',blank=True)
    publisher = models.CharField(max_length=100, default='',blank=True)
    
    summary = models.TextField(max_length=500,blank=True)
    favorite = models.ManyToManyField(User,related_name='favorite', blank=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
    
    def avg_rating(self):
        self.average = sum(Comment.objects.all().rate/Comment.count())
        print(self.average)
        return self.average

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name ="comments", on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    commenter_name = models.CharField(max_length=100)
    comment_body = models.TextField(max_length=200, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=1)
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.book.title, self.commenter_name)
        
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name