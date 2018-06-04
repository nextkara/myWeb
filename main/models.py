from django.db import models

# Create your models here.
class menu(models.Model):
    menuName = models.CharField(max_length=30)
    menuImg = models.CharField(max_length=200)
    menuLink = models.CharField(max_length=200)

