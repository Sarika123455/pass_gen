from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("username","password1","password2")

        username = forms.CharField(widget=forms.TextInput())
        password1 = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())        