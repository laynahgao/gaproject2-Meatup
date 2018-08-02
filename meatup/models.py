from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    email  = models.CharField(max_length=100)
    picture= models.ImageField(upload_to='user/%Y/%m/%d/', null=True, blank=True)
    photo_url = models.TextField(null=True, blank=True)
    interest = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.email

class Event(models.Model):
    attendees = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='events')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='my_events')
    event_name = models.CharField(max_length=100)
    event_datetime = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()


    def __str__(self):
        return self.event_name
