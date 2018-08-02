from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

def upload_path(instance, filename):
    now = datetime.datetime.now()
    return 'images/%s/%s/%s/%s' % (now.year, now.month, instance.user.username, filename)

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=100, blank=True)
  email = models.EmailField(max_length=50, null=True, blank=True)
  interest = models.TextField(null=True, blank=True)
  picture= models.ImageField(upload_to='user/%Y/%m/%d/', null=True, blank=True)
  photo_url = models.TextField(null=True, blank=True)
  updated = models.BooleanField(default=False)

  def __str__(self):
    return self.user.username

class Event(models.Model):
    attendees = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='events')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='my_events')
    event_name = models.CharField(max_length=100)
    event_datetime = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()

    def __str__(self):
        return self.event_name
