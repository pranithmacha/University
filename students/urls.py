from django.conf.urls import url
from students import views as student_views


urlpatterns = [
    url(r'^(?P<student_id>[0-9]{10})$', student_views.student_by_id, name='student_by_id'),
    url(r'^(?P<year>[0-9]{4})$', student_views.students_by_year, name='students_by_year'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$',
        student_views.students_by_year_month, name='student_by_year_month'),
]
