from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=300, validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(blank=True)
    ssn = models.CharField(unique=True)
