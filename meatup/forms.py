from django import forms
from.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class UserForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ['picture','first_name', 'username', 'email','password', 'interest', 'photo_url']

