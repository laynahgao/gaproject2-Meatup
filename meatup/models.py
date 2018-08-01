from django.db import models
from django import forms


PictureOptions=[
('pic1','Pic1')


]
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    password  = models.CharField(max_length=100)
    photo_url = models.TextField()
    interest = models.TextField()




    def __str__(self):
        return self.username

class Event(models.Model):
    attendees = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_events', null=True)
    event_name = models.CharField(max_length=100)
    event_datetime = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()

    def __str__(self):
        return self.event_name
