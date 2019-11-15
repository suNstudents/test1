from django.db import models

# Create your models here.

class Grade(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    grade = models.CharField(max_length=500,null=True,blank=True)

