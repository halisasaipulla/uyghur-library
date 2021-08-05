from django.db import models
# from django.contrib.auth.models import User

class Book(models.Model):
    ISBN = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    # reviews = relationship pk 

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

# class Comment(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)

#     def __str__(self):
#         return self.title
