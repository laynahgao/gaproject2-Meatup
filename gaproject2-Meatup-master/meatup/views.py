from django.shortcuts import render
from .models import User,Event

# Create your views here.


def profile(request, username):
    username = User.objects.get(username=username)
    events = Event.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'events': events})
