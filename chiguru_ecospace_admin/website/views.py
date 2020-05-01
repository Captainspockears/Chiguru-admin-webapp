from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#home
def home(request):
    return HttpResponse('<h1>Website-Home<h1>')

#about
def about(request):
    return HttpResponse('<h1>Website-about<h1>')

#install
def install(request):
    return HttpResponse('<h1>Website-install<h1>')

#contact
def contact(request):
    return HttpResponse('<h1>Website-contact<h1>')