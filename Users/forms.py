from django import forms
from django.contrib.auth.forms import UserCreationForm
from Users.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name",
                "username",
                "email",
                "password1",
                "password2",
                "role",
                "phone",
                ]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

