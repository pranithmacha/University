from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    user_type = forms.CharField(max_length=20)