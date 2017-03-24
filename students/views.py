from django.shortcuts import render
import logging

log = logging.getLogger(__name__)


def add_student(request):
    pass


def delete_student(request, student_id):
    pass


def update_student(request, student_id):
    pass


def get_student_list_by_year(request, year):
    pass


def get_student_list_by_semester(request, semester_id):
    pass


def student_by_id(request, student_id):
    log.info("getting student with id {0}".format(student_id))
    pass


def get_student_by_name(request, first_name, last_name):
    pass


def students_by_year(request, year):
    log.info("getting all students from year {0}".format(year))
    pass


def students_by_year_month(request, year, month):
    log.info("getting all students from year {0} and month {1}".format(year, month))
    pass
