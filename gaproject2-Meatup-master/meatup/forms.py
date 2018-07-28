from django import forms
from.models import user


class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'username', 'email','password', 'interest','photo_url']
