from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#home
def home(request):
    return HttpResponse('<h1>Mobile-Home<h1>')

#users

#main
def users(request):
    return HttpResponse('<h1>Mobile-users<h1>')

#users create
def users_create(request):
    return HttpResponse('<h1>Mobile-users-create<h1>')

#users edit
def users_edit(request):
    return HttpResponse('<h1>Mobile-users-edit<h1>')

#users delete
def users_delete(request):
    return HttpResponse('<h1>Mobile-users-delete<h1>')

#items

#main
def items(request):
    return HttpResponse('<h1>Mobile-items<h1>')

#items create
def items_create(request):
    return HttpResponse('<h1>Mobile-items-create<h1>')

#items edit
def items_edit(request):
    return HttpResponse('<h1>Mobile-items-edit<h1>')

#items delete
def items_delete(request):
    return HttpResponse('<h1>Mobile-items-delete<h1>')
