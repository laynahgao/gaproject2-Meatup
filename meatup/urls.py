# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('event_homepage/', views.index, name='index'),
  ]
