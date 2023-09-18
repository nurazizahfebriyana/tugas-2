from django.db import models

# Create your models here.
class Product(models.Model):
    nama = models.CharField(max_length=255, default='')
    kelas = models.CharField(max_length=255, default = '')
    name = models.CharField(max_length=255, default = '')
    price = models.CharField(max_length=255, default = '')
    description = models.TextField()
    amount = models.IntegerField(default=0)
    date_added = models.DateField(auto_now = True, null= True)