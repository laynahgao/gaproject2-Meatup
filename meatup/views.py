

from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import Profile
from .models import Event

from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from .forms import ProfileForm
from pprint import pprint

## Homepage##

def index(request):
    events = Event.objects.all()
    return render(request, 'homepage.html', { 'events': events })


def signup(request):
    return HttpResponseRedirect('')
        # user = User.objects.get(id:username)

    # if user:
    #     return render(request, 'signup.html')


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
                return redirect('homepage')
            else:
                return render(request, 'login.html', {error: 'Username/password not found'})

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
    form = ProfileForm(request.POST)
    if form.is_valid():
        user= form.save()
        return redirect('user_info', id=user.id)
  else:
    form = ProfileForm()
  return render(request, 'user_form.html', {'form': form})

## edit ##

def  user_edit(request,id):
  user= User.objects.get(id=id)
  if request.method == 'POST':
    form = ProfileForm(request.POST, instance=user)
    if form.is_valid():
        user = form.save()
        return redirect('user_info', id=user.id)
  else:
    form = ProfileForm(instance=user)
  return render(request, 'user_form.html', {'form': form})

