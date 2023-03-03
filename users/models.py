from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(null=True, default=False)