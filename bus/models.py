from os import times

from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField


# Create your models here.

class Login(models.Model):
    name = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    phone_number = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.name

class Bus(models.Model):
    name = models.CharField(max_length=200)
    number= models.IntegerField(blank=True,null=True)
    destination = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True ,auto_now=False)
    def __str__(self):
        return self.name

class Seat(models.Model):
    choice= models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='bus/Seat', blank=True, null=True)
    def __str__(self):
        return self.choice
