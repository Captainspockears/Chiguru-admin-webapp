from django.db import models

# Create your models here.

class Event(models.Model):

    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='mobileadmin/static/mobileadmin/images/cache')

    def __str__(self):
        return self.title

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='mobileadmin/static/mobileadmin/images/cache')
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='mobileadmin/static/mobileadmin/images/cache')

    def __str__(self):
        return self.name