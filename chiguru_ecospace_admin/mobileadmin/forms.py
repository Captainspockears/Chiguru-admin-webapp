#from django.forms import ModelForm
#from .models import Event
from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField()

class EventForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

class ProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    price = forms.IntegerField()

class ItemForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()


class SearchForm(forms.Form):
    title = forms.CharField()

'''
# Create the form class.
class EventForm(ModelForm):
     #class Meta:
         model = Event
         fields = '__all__'

# Create the form class.
class SearchForm(ModelForm):
     class Meta:
         model = Event
         fields = ['title']
'''