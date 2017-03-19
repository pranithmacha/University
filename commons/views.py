from django.shortcuts import render
from commons.models import UserProfile

# Create your views here.


def create_user():
    pass
    # profile = models.UserProfile.objects.create_user("myname", password="xxxx"


def registration(request):
    if request.method == "GET":
        return render(request, "commons/registration.html", {})
    if request.method == "POST":
        return render(request, "faculty/faculty_home.html", {})