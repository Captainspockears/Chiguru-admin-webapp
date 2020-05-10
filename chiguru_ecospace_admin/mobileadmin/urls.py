from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mobileadmin-home'),
    path('analytics/', views.analytics, name='mobileadmin-analytics'),
    path('edit/', views.edit, name='mobileadmin-edit'),
    path('logout/', views.logout, name='mobileadmin-logout'),

    #events
    path('events/add/', views.addevent, name='mobileadmin-addevent'),
    path('events/update/', views.updateevent, name='mobileadmin-updateevent'),
    path('events/delete/', views.deleteevent, name='mobileadmin-deleteevent'),

    #product
    path('product/add/', views.addproduct, name='mobileadmin-addproduct'),
    path('product/update/', views.updateproduct, name='mobileadmin-updateproduct'),
    path('product/delete/', views.deleteproduct, name='mobileadmin-deleteproduct'),

    #item
    path('item/add/', views.additem, name='mobileadmin-additem'),
    path('item/update/', views.updateitem, name='mobileadmin-updateitem'),
    path('item/delete/', views.deleteitem, name='mobileadmin-deleteitem'),

]
