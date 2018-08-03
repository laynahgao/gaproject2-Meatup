
from django.shortcuts import render, redirect

from .models import Event
from .models import Profile


from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.

from .forms import EventForm
from .forms import LoginForm
from .forms import ProfileForm


############################  EVENTS ###########################
#Event Index
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def index_landing(request):
    user = request.user
    if user is None:
      print('user is none')
      return render(request, 'index.html')

    if user.is_authenticated:
      print('user is authenticated')
      return redirect('index')

    # user is available but either is not valid
    # or has not yet authenticated
    print('user is not authenticated')
    return render(request, 'index.html')

#Event Show
def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'event_detail.html', {'event': event})

#Event Create
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
 #Event Attendees
def event_attendees(request, id):
    # event_id = request.GET.get('event_id', None)
    print('Id',id)
    attendees = 0
    if (id):
        event = Event.objects.get(id=int(id))
        if event is not None:
            attendees = event.attendees + 1
            event.attendees = attendees
            event.save()
    return redirect('event_detail', id=event.id)
## Homepage##

def index(request):
    events = Event.objects.all()
    return render(request, 'homepage.html', { 'events': events })


def signup(request):
  # email = Profile.objects.get()
  # POST Request for a new user
  if request.method == 'POST':
    # Verify passwords
    if request.POST['password1'] == request.POST['password2'] and request.POST['password1'] != '':
      try:
        # If Username already exists, render form with error
        user = User.objects.get(username=request.POST['username'])
        return render(request, 'signup.html', {'error': 'Username already in use'})
      # If user does not exist, create and login new user then redirect to home
      except User.DoesNotExist:
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        profile = Profile.objects.create(user=user)
        auth.login(request, user)
        return redirect('index')
        send_mail(
                    'Succesfull Signup',
                    'Hey Welcome to Meatup! Happy Networking!!.',
                    'gupta.sweet.niti@gmail.com',
                    ['gupta.sweet.niti@gmail.com'],
                    fail_silently=False,
                )
    else:
      return render(request, 'signup.html', {'error': 'Passwords do not match'})
  # GET request for empty sign up form
  else:
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)

        print("login POST request")

        if form.is_valid():
            e = form.cleaned_data['username']
            p = form.cleaned_data['password']

            print("form is valid: " + e)

            foundUser = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if foundUser:
                auth.login(request, foundUser)
                return redirect('index')
            else:
                return render(request, 'login.html', { 'error' : 'invalid', 'username' : e })

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

#### User ####

## user profile page ##
# @login_required
def user_info(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    #events = Event.objects.filter
    return render(request, 'user.html', {'profile': profile})


## edit ##

def  user_edit(request,id):
  user = User.objects.get(id=id)
  profile = Profile.objects.get(user=user)
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        profile = form.save()
        return redirect('user_info', id=id)
  else:
    form = ProfileForm(instance=profile)
  return render(request, 'user_form.html', {'form': form})

