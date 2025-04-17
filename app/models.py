from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField()
    email = models.EmailField()
    age = models.PositiveIntegerField()
    ssn = models.CharField()
