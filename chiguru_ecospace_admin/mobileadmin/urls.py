from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mobileadmin-home'),
    path('login/', views.login, name='mobileadmin-login'),
    path('analytics/', views.analytics, name='mobileadmin-analytics'),
    path('edit/', views.edit, name='mobileadmin-edit'),

    #events
    path('events/add/', views.addevent, name='mobileadmin-addevent'),
    path('events/update/', views.updateevent, name='mobileadmin-updateevent'),
    path('events/delete/', views.deleteevent, name='mobileadmin-deleteevent'),
]
