from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    rollnum = models.CharField(max_length=10)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=30)
    address = models.TextField(null=True)

    def __str__(self):
        return self.name+' '+self.email


class Employee(models.Model):
    empname = models.CharField(max_length=50)
    empid = models.CharField(max_length=20)
    sal = models.IntegerField()
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.empname+' '+self.empid


class Emp(models.Model):
    empname = models.CharField(max_length=50)
    empid = models.CharField(max_length=20)
    sal = models.IntegerField()
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.empname+' '+self.empid


class StudentDetails(models.Model):
    branches = [('None', 'None'),
                ('CSE', 'CSE'),
                ('ECE', 'ECE'),
                ('MEC', 'MEC'),
                ('EEE', 'EEE'),
                ('IT', 'IT')]
    genders = [('Female', 'Female'),
               ('Male', 'Male'),
               ('Others', 'Others')]
    languages = [('Telugu', 'Telugu'),
                 ('Hindi', 'Hindi'),
                 ('English', 'English')]
    stuname = models.CharField(max_length=30)
    stunum = models.IntegerField(null=True)
    branch = models.CharField(max_length=4, choices=branches, null=True)
    gender = models.CharField(max_length=10, choices=genders, null=True)
    lang = MultiSelectField(max_choices=3, choices=languages, null=True)
    email = models.EmailField(max_length=30)
    # DOB = models.DateField(null=True)

    def __str__(self):
        return self.stuname+' '+self.email
