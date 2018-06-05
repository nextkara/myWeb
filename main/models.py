from django.db import models

# Create your models here.
class menu(models.Model):
    menuName = models.CharField(max_length=30)
    menuImg = models.CharField(max_length=200)
    menuLink = models.CharField(max_length=200)

class user(models.Model):
    userName = models.CharField(max_length=200)
    userID = models.IntegerField()
    userPassword = models.CharField(max_length=200)
    userGroup = models.CharField(max_length=200)