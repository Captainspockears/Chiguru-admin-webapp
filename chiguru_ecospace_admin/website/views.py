from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#home
def home(request):
    return render(request, 'website/home.html')

#about
def about(request):
    return render(request, 'website/about.html')

#install
def install(request):
    return render(request, 'website/install.html')

#contact
def contact(request):
    return render(request, 'website/contact.html')