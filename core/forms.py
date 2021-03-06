from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    email=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=('username','email','password1','password2')