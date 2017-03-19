from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

import logging

logger = logging.getLogger(__name__)


def home(request):
    """
    :param request:
    :return:
    """
    user = request.user
    if user.is_authenticated():
        return render(request, 'faculty/faculty_home.html', {})
    else:
        return render(request, 'home.html', {})


@login_required
def login_success(request):
    """
    :param request:
    :return:
    """

    logger.info("{0} logged in successfully! getting home page".format(request.user.username))
    return redirect(to=reverse('home'))


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


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


