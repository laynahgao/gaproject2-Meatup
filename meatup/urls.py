from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/<int:id>', views.event_detail, name='event_detail'),
    path('events/new', views.event_create, name='event_create'),
    path('events/<int:id>/edit', views.event_edit, name='event_edit'),
    path('events/<int:id>/delete', views.event_delete, name='event_delete'),
    # path('event_attendees/', views.event_attendees, name='event_attendees')
]
