from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

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

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
