from django.forms import ModelForm
from .models import Event

# Create the form class.
class EventForm(ModelForm):
     class Meta:
         model = Event
         fields = '__all__'

# Create the form class.
class SearchForm(ModelForm):
     class Meta:
         model = Event
         fields = ['title']