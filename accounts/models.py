
from django.contrib.auth.models import AbstractUser
from django.db import models

class AdminUser(AbstractUser):  
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Book(models.Model):  
    title = models.CharField(max_length=255)  
    author = models.CharField(max_length=255)  
    published_date = models.DateField()  
    isbn = models.CharField(max_length=13, unique=True)  
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title
