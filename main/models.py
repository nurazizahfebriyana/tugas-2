from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField(default=0)