from django import forms
from django.contrib.auth.models import User
from password_project_app.models import UserProfileInfoModel

class UserProfileInfo(forms.ModelForm):

    password=forms.CharField(max_length=128,widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model=UserProfileInfoModel
        fields=('profile_pic','portfolio_form')
