from django.shortcuts import render, redirect
from .models import User, Event
from .forms import UserForm



## Homepage##

def index(request):
    events = Event.objects.all()
    return render(request, 'homepage.html', { 'events': events })


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











