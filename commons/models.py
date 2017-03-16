from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    user_type = models.CharField(max_length=20)


class Student(models.Model):
    user = models.OneToOneField(UserProfile)
    is_active = models.BooleanField()


class Staff(models.Model):
    user = models.OneToOneField(UserProfile)
    is_active = models.BooleanField()


