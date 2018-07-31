from django import forms
from .models import Event

class EventForm(forms.ModelForm):
  class Meta:
    model = Event
    fields = ('event_name', 'event_datetime', 'event_location', 'event_description')

