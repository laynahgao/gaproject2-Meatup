from django import forms
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
  # class Meta:
  #   model: User
  #   fields=['username', 'password']
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ['picture','first_name', 'username', 'email', 'interest', 'photo_url']

