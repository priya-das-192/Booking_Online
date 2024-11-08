from os import times

from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField


# Create your models here.

class Bus(models.Model):
    name = models.CharField(max_length=200)
    number= models.IntegerField(blank=True,null=True)
    destination = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True ,auto_now=False)
