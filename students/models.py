"""


from django.db import models


class StudentProfile(models.Model):
    student_id = models.CharField(primary_key=True, auto_created=False)
    first_name = models.CharField()
    last_name = models.CharField()
    joining_date = models.DateTimeField()
    current_semester = models.CharField()
    department = models.ForeignKey('Department')
    graduation_date = models.DateTimeField(null=True)
    address = models.ForeignKey('Address')
    parent_address = models.ForeignKey('Address')
    student_phone_num = models.CharField()
    parent_phone_num = models.CharField()
    student_email = models.EmailField()
    parent_email = models.EmailField()


class Address(models.Model):
    address_line_one = models.CharField()
    city = models.CharField()
    state = models.CharField()
    zip = models.CharField()
    country = models.CharField()


class Department(models.Model):
    name = models.CharField()


class Course(models.Model):
    name = models.CharField()
    year = models.CharField()
    semester = models.CharField()
    department = models.ForeignKey('Department')
    # grade = models.ForeignKey('Grade')


class Grade(models.Model):
    grade = models.CharField()
    marks = models.CharField()
    student = models.ForeignKey('Student')
    course = models.ForeignKey('Course')
"""


