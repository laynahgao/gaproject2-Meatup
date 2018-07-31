from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

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
