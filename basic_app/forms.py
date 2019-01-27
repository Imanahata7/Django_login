from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import UserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
         model = User
         fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('portfolio', 'profile_pic')
