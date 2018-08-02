from django import forms
from .models import Profile
from django.contrib.auth.models import User
from.models import User
from .models import Event

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ('event_name', 'event_datetime', 'event_location', 'event_description')

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
