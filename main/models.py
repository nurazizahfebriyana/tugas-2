from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255, default = '')
    price = models.CharField(max_length=255, default = '')
    description = models.TextField()
    amount = models.IntegerField(default=0)
    date_added = models.DateField(auto_now = True, null= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=255, default = '')