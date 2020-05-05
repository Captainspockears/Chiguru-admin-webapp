from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('install/', views.install, name='website-install'),
    path('contact/', views.contact, name='website-contact'),
]
