from django import forms
from.models import User


class UserForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ['picture','first_name', 'username', 'email','password', 'interest', 'photo_url']
