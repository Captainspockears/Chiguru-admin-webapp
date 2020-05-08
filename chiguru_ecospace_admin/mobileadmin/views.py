from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

from .forms import EventForm
from .forms import SearchForm
from .forms import ImageForm
import json

from .Classes.Event import Event
from .models import Event as Eventmodel

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
            name = form.cleaned_data.get('title') 
            desc = form.cleaned_data.get('description') 
            img = form.cleaned_data.get('image') 
            obj = Eventmodel.objects.create( 
                                 title = name, 
                                 description = desc, 
                                 image = img 
                                 ) 
            obj.save() 

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

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        data = request.POST

        title = data['title']

        event = Event(title)
        event.getEventId()
        event.pullEvent()

        imageurl = event.getImage()

        jsonStr = event.to_json()
        f = open("temp.json", "w")
        f.write(jsonStr)
        f.close()

        context = {'form':form, 'searchvisibility':True, 'dispflag':True, 'title':event.title, 'desc':event.description, 'imagepath': imageurl}
        return render(request,'mobileadmin/events/update.html', context)

    elif request.method == 'POST' and 'image' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        event = Event(jsonobj=jsonobject)

        imageurl = event.getImage()
        context = {'form':form, 'searchvisibility':True, 'imageflag':True,'title':event.title, 'desc':event.description, 'imagepath': imageurl}
        
        return render(request,'mobileadmin/events/update.html', context)

    elif request.method == 'POST' and 'title' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        event = Event(jsonobj=jsonobject)

        imageurl = event.getImage()
        context = {'form':form, 'searchvisibility':True, 'titleflag':True,'title':event.title, 'desc':event.description, 'imagepath': imageurl}

        return render(request,'mobileadmin/events/update.html', context)

    elif request.method == 'POST' and 'description' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        event = Event(jsonobj=jsonobject)

        imageurl = event.getImage()
        context = {'form':form, 'searchvisibility':True, 'descflag':True,'title':event.title, 'desc':event.description, 'imagepath': imageurl}
        
        return render(request,'mobileadmin/events/update.html', context)

    elif request.method == 'POST' and 'imagesubmit' in request.POST:
        data = request.FILES
        imagedata = data['imageinput']

        obj = Eventmodel.objects.create( 
                                 title = 'name', 
                                 description = 'desc', 
                                 image = imagedata 
                                 ) 
        obj.save()

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        event = Event(jsonobj=jsonobject)

        imagenamedata = imagedata.name.split('.')
        imagename = imagenamedata[0]
        imagetype = imagenamedata[1]

        source = "/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/static/mobileadmin/images/cache/"+imagename+'.'+imagetype

        event.updateImage(imagename, source, imagetype)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/update.html', context)

    elif request.method == 'POST' and 'titlesubmit' in request.POST:
        data = request.POST
        title = data['titleinput']


        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/update.html', context)

    elif request.method == 'POST' and 'descsubmit' in request.POST:
        data = request.POST
        desc = data['descinput']


        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/update.html', context)

    else:
        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/update.html', context)

#delete
def deleteevent(request):

    context = {'searchvisibility':True, 'titleflag':True, 'descflag':True}
    return render(request,'mobileadmin/events/delete.html', context)