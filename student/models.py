from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    roll = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
# Create your models here.
