# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_view, name="login"),
  path('event_homepage/', views.index, name='index'),
  path('logout/', views.logout_view, name="logout"),
  ]

