from django.db import models
from datetime import date



class About(models.Model):
    name = models.CharField(max_length=50, null=True)
    desc = models.TextField(max_length=5000)
    age = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)
    phone = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    image = models.ImageField(upload_to="images/", null=True)
    first_function = models.CharField(max_length=50, null=True)
    second_function = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.email

class ProfessionalSkills(models.Model):
    color = (('blue','blue'), ('green','green'))
    name = models.CharField(max_length= 50)
    value = models.PositiveIntegerField()
    color = models.CharField(max_length=50, choices=color, default='blue')
    def __str__(self):
        return self.name


class WorkExperience (models.Model):
    position = models.CharField(max_length= 50)
    place = models.CharField(max_length= 50)
    date_started = models.DateField(default=date.today())
    date_ended = models.DateField(default= date.today(), null=True, blank=True)
    desc = models.TextField(max_length=5000)

    def __str__(self):
        return self.place

class Education (models.Model):
    degree = models.CharField(max_length= 50)
    place = models.CharField(max_length= 50)
    date_started = models.DateField(default=date.today())
    date_ended = models.DateField(default=date.today(), null=True, blank=True)
    desc = models.TextField(max_length=5000)

    def __str__(self):
        return self.place

class Certification (models.Model):
    name = models.CharField(max_length= 50)
    organisation = models.CharField(max_length= 50)
    date_acheived = models.DateField(default=date.today())
    score = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

