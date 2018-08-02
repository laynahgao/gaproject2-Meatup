from django.urls import path
from . import views

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('events/', views.event_list, name='event_list'),
  path('events/<int:id>', views.event_detail, name='event_detail'),
  path('events/new', views.event_create, name='event_create'),
  path('events/<int:id>/edit', views.event_edit, name='event_edit'),
  path('events/<int:id>/delete', views.event_delete, name='event_delete'),
  path('login/', views.login_view, name="login"),
  path('homepage/', views.index, name='index'),
  path('logout/', views.logout_view, name="logout"),
  path('user/new', views.user_create, name='user_create'),
  path('user/<int:id>/', views.user_info, name='user_info'),
  path('user/<int:id>/edit', views.user_edit, name='user_edit'),
  ]
