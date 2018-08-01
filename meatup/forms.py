from django import forms
from.models import User
from .models import Event


class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ('event_name', 'event_datetime', 'event_location', 'event_description')

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class UserForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ['first_name', 'username', 'email','password', 'interest', 'photo_url']






