# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('event_homepage/', views.index, name='index'),
  path('user/new', views.user_create, name='user_create'),
  path('user/<int:id>/', views.user_info, name='user_info'),
  path('user/<int:id>/edit', views.user_edit, name='user_edit'),
]

