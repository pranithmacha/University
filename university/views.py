from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

import logging

logger = logging.getLogger(__name__)


@login_required
def home(request):
    """
    :param request:
    :return:
    """

    logger.info("getting home page for {0}".format(request.user.username))
    role = "faculty"
    if role == "faculty":
        return render(request, "faculty/faculty_home.html", {})
    return render(request, 'index.html', {})


def student_registration(request):
    return render(request, 'students/student_registration.html', {})


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='media/profiles')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'students/success.html', {
            'uploaded_file_url': uploaded_file_url
        })


@login_required
def login(request):
    """
    login for all users
    check user group/role
    forward to respective home page
    :param request:
    :return:
    """
    role_based_login_url = ""
    return redirect(reverse(role_based_login_url))


def about(request):
    return render(request, "", {})


