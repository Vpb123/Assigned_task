from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(User):
         pass
    
class Post(models.Model):
     text = models.CharField(max_length=255)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='author')