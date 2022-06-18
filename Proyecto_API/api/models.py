from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.TextField(max_length=9)
    address = models.TextField(max_length=50)
    about = models.TextField(max_length=100)