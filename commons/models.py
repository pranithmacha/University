from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    user_type = models.CharField(max_length=20)


class Student(models.Model):
    profile = models.OneToOneField(UserProfile)
    is_active = models.BooleanField()
    # current_semester = models.CharField()
    # graduation_date = models.DateTimeField(null=True)
    # user_type = models.CharField(max_length=20)
    # primary_address = models.ForeignKey('Address')
    # secondary_address = models.ForeignKey('Address')
    # primary_phone_num = models.CharField()
    # student_phone_num = models.CharField()
    # parent_email = models.EmailField()
    # department = models.ForeignKey('Department')


class Staff(models.Model):
    user = models.OneToOneField(UserProfile)
    is_active = models.BooleanField()


