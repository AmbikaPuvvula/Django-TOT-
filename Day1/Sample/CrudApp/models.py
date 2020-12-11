from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    rollnum = models.CharField(max_length=10)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)


class Employee(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now=False, auto_now_add=False)
    dec = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(max_length=30)
    upload = models.FileField(upload_to='path/')
    flt = models.FloatField()
    img = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100)
    age = models.IntegerField()
    txt = models.TextField()
    url = models.URLField(max_length=200)
    # publish = models.DateTimeField()
