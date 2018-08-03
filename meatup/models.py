from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100, blank=True)
  email = models.EmailField(max_length=50, null=True, blank=True)
  interest = models.TextField(null=True, blank=True)
  picture= models.ImageField(upload_to='user/%Y/%m/%d/', null=True, blank=True)
  updated = models.BooleanField(default=False)

  def __str__(self):
    return self.user.username

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()
    attendees = models.IntegerField(default=0)
    date = models.DateField(("Date"), default=datetime.date.today)
    time = models.TimeField(("Time"), default='00:00')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name
