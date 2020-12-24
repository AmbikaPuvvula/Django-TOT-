from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class RegData(models.Model):
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
                 ('English', 'English'),
                 ('Malayalam', 'Malayalam')]
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    url = models.URLField()
    gender = models.CharField(max_length=10, choices=genders, null=True)
    branch = models.CharField(max_length=4, choices=branches, null=True)
    lang = MultiSelectField(max_choices=3, choices=languages, null=True)


class Register(models.Model):
    genders = [('Female', 'Female'),
               ('Male', 'Male'),
               ('Others', 'Others')]
    branchs = [('Select', 'Select'), ('ECE', "ECE"),
               ('MEC', "MEC"), ('CSE', "CSE"), ('IT', "IT")]
    # languages = [('Telugu', 'Telugu'),
    #              ('Hindi', 'Hindi'),
    #              ('English', 'English'),
    #              ('Malayalam', 'Malayalam')]
    name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10, choices=genders, null=True)
    branch = models.CharField(
        max_length=10, choices=branchs, null=True, default=None)
    # lang = models.CharField(max_length=10, choices=languages, null=True)
