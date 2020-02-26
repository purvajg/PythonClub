from django.urls import path
from django.urls import re_path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resource'),
    path('meeting/', views.getMeetings, name='meeting'),
    path('meeting/details/<int:id>', views.getMeetingDetails, name='details'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('newResource/', views.newResource, name='newResource'),
    # path('login/', views.login, name='login'),
    path('loginMessage/', views.loginMessage, name='loginMessage'),
    path('logoutMessage/', views.logoutMessage, name='logoutMessage'),
]