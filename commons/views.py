from django.shortcuts import render
from commons.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
import logging

log = logging.getLogger(__name__)


def create_user(user_info_dict):
    # profile = UserProfile.objects.create_user("myname", password="xxxx")
    message = "success"
    profile = None
    try:
        profile = UserProfile.objects.create_user(**user_info_dict)
        log.info("user {0} successfully created".format(profile.username))
    except IntegrityError as ie:
        log.exception(ie)
        message = ie.message
    return profile, message


@login_required
def registration(request):
    if request.method == "GET":
        return render(request, "commons/registration.html", {})
    if request.method == "POST":
        user_info_dict = dict()
        user_info_dict["first_name"] = request.POST.get("firstname")
        user_info_dict["last_name"] = request.POST.get("lastname")
        user_info_dict["username"] = request.POST.get("firstname")+request.POST.get("lastname")
        user_info_dict["user_type"] = "student"
        user_info_dict["password"] = "temp"
        created_user = create_user(user_info_dict)
        return render(request, "faculty/faculty_home.html", {"created_user": created_user})
