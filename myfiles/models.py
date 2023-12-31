from django.db import models

# Create your models here.

class Servise(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='media')
    data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    adres = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

class Home(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='media')
    data = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

