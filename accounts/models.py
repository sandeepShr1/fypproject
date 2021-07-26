from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class User(AbstractUser):
    gender = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)


