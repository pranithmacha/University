from django.shortcuts import render
from commons.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from commons.forms import RegistrationForm
import logging

log = logging.getLogger(__name__)


def create_user(user_info_dict):
    message = "success"
    profile = None
    try:
        profile = UserProfile.objects.create_user(**user_info_dict)
        log.info("user {0} successfully created".format(profile.username))
    except IntegrityError as ie:
        log.exception(ie)
        message = "username {0} already exists".format(user_info_dict["username"])
    return profile, message


@login_required
def registration(request):
    if request.method == "GET":
        return render(request, "commons/registration.html", {})
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            log.info("valid registration form")
            user_info_dict = dict()
            user_info_dict["first_name"] = request.POST.get("first_name")
            user_info_dict["last_name"] = request.POST.get("last_name")
            user_info_dict["username"] = request.POST.get("first_name") + request.POST.get("last_name")
            user_info_dict["user_type"] = "student"
            user_info_dict["password"] = "temp"
            created_user, message = create_user(user_info_dict)
        else:
            log.error("not a valid form")
        return render(request, "faculty/faculty_home.html", {"created_user": created_user, "message": message})
