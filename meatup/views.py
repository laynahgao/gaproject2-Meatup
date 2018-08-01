
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout

############################  EVENTS ###########################
#Event Index
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

#Event Show
def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'event_detail.html', {'event': event})

#Event Creat
def event_create(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      event = form.save()
      return redirect('event_detail', id=event.id)
  else:
    form = EventForm()
  return render(request, 'event_form.html', {'form': form})

#Event Edit
def event_edit(request, id):
  event = Event.objects.get(id=id)
  if request.method == 'POST':
    form = EventForm(request.POST, instance=event)
    if form.is_valid():
      event = form.save()
      return redirect('event_detail', id=event.id)
  else:
    form = EventForm(instance=event)
  return render(request, 'event_form.html', {'form': form})

#Event Delete
def event_delete(request, id):
  Event.objects.get(id=id).delete()
  return redirect('event_list')

#Event attendees
# def event_attendees(request):
#     event_id = request.GET.get('event_id', None)
#     attendees = 0
#     if (event_id):
#         event = Event.objects.get(id=int(event_id))
#         if event is not None:
#             attendees = event.attendees + 1
#             event.attendees = attendees
#             event.save()
#     return HttpResponse(attendees)



## Homepage##

def index(request):
    events = Event.objects.all()
    return render(request, 'homepage.html', { 'events': events })


def login_view(request):
  if request.method == 'POST':
    # if post, then authenticate (user submitted username and password)
    form = LoginForm(request.POST)
    if form.is_valid():
        u = form.cleaned_data['username']
        p = form.cleaned_data['password']
        user = authenticate(username = u, password = p)
        if user is not None:
            if user. is_active:
                login(request, user)
                return redirect('user_info', id=user.id)
            else:
                print("The account has been disabled.")
        else:
            print("The username and/or password is incorrect.")
  else:
      form = LoginForm()
      return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


#### User ####

## user profile page ##
# @login_required
def user_info(request,id):
    username = User.objects.get(id=id)
    print(username)
    #events = Event.objects.filter
    return render(request, 'user.html', {'username': username})

# @login_required
## create ##
def  user_create(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
        user= form.save()
        return redirect('user_info', id=user.id)
  else:
    form = UserForm()
  return render(request, 'user_form.html', {'form': form})

## edit ##

def  user_edit(request,id):
  user= User.objects.get(id=id)
  if request.method == 'POST':
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        user = form.save()
        return redirect('user_info', id=user.id)
  else:
    form = UserForm(instance=user)
  return render(request, 'user_form.html', {'form': form})

