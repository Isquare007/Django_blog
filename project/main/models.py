from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """post model"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return (f'{self.title}\n{self.description}')