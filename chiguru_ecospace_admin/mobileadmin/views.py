from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

from .forms import EventForm
from .forms import SearchForm

from .Classes.Event import Event

# Create your views here.

#home
def home(request):
    return render(request,'mobileadmin/home.html')

#login
def login(request):
    return render(request,'mobileadmin/login.html')

#analytics
def analytics(request):
    return render(request,'mobileadmin/analytics.html')

#edits
def edit(request):
    return render(request,'mobileadmin/edit.html')

#events

#add
def addevent(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        imagedata = request.FILES
        data = request.POST

        imagenamedata = imagedata['image'].name.split('.')
        imagename = imagenamedata[0]
        imagetype = imagenamedata[1]

        title = data['title']
        desc = data['description']

        source = "/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/static/mobileadmin/images/cache/"+imagename+'.'+imagetype

        event = Event(title, desc)
        event.addImage(imagename, source, imagetype)
        event.addEvent()

        #image = request.FILES['image']
        #img = Image.open(image)
        #img.save("sample.jpeg", "jpeg")

    else:
        form = EventForm()


    context = {'form':form}
    return render(request,'mobileadmin/events/add.html', context)

#update
def updateevent(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()

        data = request.POST

        title = data['title']

        event = Event(title)
        event.getEventId()
        event.pullEvent()

        imageurl = event.getImage()

        context = {'form':form, 'searchvisibility':True, 'title':event.title, 'desc':event.description, 'imagepath': imageurl}
        return render(request,'mobileadmin/events/update.html', context)

    else:
        form = SearchForm()
        context = {'form':form, 'searchvisibility':False,}
        return render(request,'mobileadmin/events/update.html', context)