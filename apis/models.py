from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.CharField(max_length=2)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)