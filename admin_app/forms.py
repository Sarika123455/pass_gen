from django import forms
from .models import Member,Societyloan,Loan
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'



class Memberform(forms.ModelForm):
    class Meta:
        model=Member  
        fields="__all__"
        date_of_birth = widgets = {'date_of_birth': DateInput()}
              

           


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("username","password1","password2")

        username = forms.CharField(widget=forms.TextInput())
        password1 = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())      

class SocietyForm(forms.ModelForm):
    class Meta:
        model=Societyloan
        fields="__all__"
        date = widgets = {'date': DateInput()}


class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields="__all__"