from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=100, default='Unknown')
    category = models.CharField(max_length=100, default='Unknown')
    author = models.CharField(max_length=100, default='Unknown')
    content = models.TextField(default='Unknown')
    created_at = models.DateTimeField()
