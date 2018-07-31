from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    password  = models.CharField(max_length=100)
    picture= models.ImageField(upload_to='user/%Y/%m/%d/', null=True, blank=True)
    photo_url = models.TextField()
    interest = models.TextField()


    def __str__(self):
        return self.username

class Event(models.Model):
    attendees = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_events')
    event_name = models.CharField(max_length=100)
    event_datetime = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()

    def __str__(self):
        return self.event_name
