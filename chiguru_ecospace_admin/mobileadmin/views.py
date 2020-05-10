from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from PIL import Image

from .forms import EventForm
from .forms import SearchForm
from .forms import ImageForm
from .forms import ProductForm
from .forms import ItemForm
import json

from .Classes.Event import Event
from .models import Event as Eventmodel

from django.contrib.auth.models import User

from .Classes.Product import Product
from .models import Product as Productmodel

from .Classes.Item import Item
from .models import Item as Itemmodel

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout as logoutuser

# Create your views here.

#home

@staff_member_required
def home(request):
    return render(request,'mobileadmin/home.html')

@staff_member_required
def logout(request):
    logoutuser(request)
    return redirect('website-home')

#analytics
@staff_member_required
def analytics(request):
    return render(request,'mobileadmin/analytics.html')

#edits
@staff_member_required
def edit(request):
    return render(request,'mobileadmin/edit.html')

############################################################################################################################################################

#events

#add
@staff_member_required
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
@staff_member_required
def updateevent(request):

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        data = request.POST

        title = data['title']

        event = Event(title)
        
        eventid = event.getEventId()

        if eventid is False:
            print("hello")
            form = SearchForm()
            context = {'form':form, 'warningflag':True}
            return render(request,'mobileadmin/events/update.html', context)    

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

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        event = Event(jsonobj=jsonobject)

        event.updateTitle(title)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/update.html', context)

    elif request.method == 'POST' and 'descsubmit' in request.POST:
        data = request.POST
        desc = data['descinput']

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        event = Event(jsonobj=jsonobject)

        event.updateDescription(desc)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/update.html', context)

    else:
        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/update.html', context)

#delete
@staff_member_required
def deleteevent(request):

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        data = request.POST

        title = data['title']

        event = Event(title)

        eventid = event.getEventId()
        if eventid is False:
            form = SearchForm()
            context = {'form':form, 'warningflag':True}
            return render(request,'mobileadmin/events/delete.html', context)

        event.pullEvent()

        imageurl = event.getImage()

        jsonStr = event.to_json()
        f = open("temp.json", "w")
        f.write(jsonStr)
        f.close()

        context = {'form':form, 'searchvisibility':True, 'dispflag':True, 'title':event.title, 'desc':event.description, 'imagepath': imageurl}
        return render(request,'mobileadmin/events/delete.html', context)

    if request.method == 'POST' and 'delete' in request.POST:

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        event = Event(jsonobj=jsonobject)

        event.deleteEvent()

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/delete.html', context)

    else:
        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/events/delete.html', context)

############################################################################################################################################################

#product

#add
@staff_member_required
def addproduct(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name') 
            desc = form.cleaned_data.get('description') 
            pri = form.cleaned_data.get('price') 
            img = form.cleaned_data.get('image') 
            obj = Productmodel.objects.create( 
                                 name = name, 
                                 description = desc, 
                                 image = img, 
                                 price = pri
                                 ) 
            obj.save() 

        imagedata = request.FILES
        data = request.POST

        imagenamedata = imagedata['image'].name.split('.')
        imagename = imagenamedata[0]
        imagetype = imagenamedata[1]

        name = data['name']
        desc = data['description']
        price = data['price']

        source = "/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/static/mobileadmin/images/cache/"+imagename+'.'+imagetype

        product = Product(name=name, description=desc, price=price)
        product.addImage(imagename, source, imagetype)
        product.addProduct()

    else:
        form = ProductForm()


    context = {'form':form}
    return render(request,'mobileadmin/product/add.html', context)

#update
@staff_member_required
def updateproduct(request):

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        data = request.POST

        name = data['title']

        product = Product(name)
        
        productid = product.getProductId()

        if productid is False:
            form = SearchForm()
            context = {'form':form, 'warningflag':True}
            return render(request,'mobileadmin/product/update.html', context)    

        product.pullProduct()

        imageurl = product.getImage()

        jsonStr = product.to_json()
        f = open("temp.json", "w")
        f.write(jsonStr)
        f.close()

        context = {'form':form, 'searchvisibility':True, 'dispflag':True, 'name':product.name, 'desc':product.description, 'imagepath': imageurl, 'price':product.price}
        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'image' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        imageurl = product.getImage()
        context = {'form':form, 'searchvisibility':True, 'imageflag':True,'name':product.name, 'desc':product.description, 'imagepath': imageurl, 'price':product.price}
        
        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'name' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        imageurl = product.getImage()
        context = {'form':form, 'searchvisibility':True, 'nameflag':True,'name':product.name, 'desc':product.description, 'imagepath': imageurl, 'price':product.price}

        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'description' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        imageurl = product.getImage()
        context = {'form':form, 'searchvisibility':True, 'descflag':True,'name':product.name, 'desc':product.description, 'imagepath': imageurl, 'price':product.price}
        
        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'price' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        imageurl = product.getImage()
        context = {'form':form, 'searchvisibility':True, 'priceflag':True,'name':product.name, 'desc':product.description, 'imagepath': imageurl, 'price':product.price}

        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'imagesubmit' in request.POST:
        data = request.FILES
        imagedata = data['imageinput']

        obj = Productmodel.objects.create( 
                                name = "name", 
                                description = "desc", 
                                image = imagedata,
                                price = "pri"
                                ) 
        obj.save() 
        
        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        imagenamedata = imagedata.name.split('.')
        imagename = imagenamedata[0]
        imagetype = imagenamedata[1]

        source = "/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/static/mobileadmin/images/cache/"+imagename+'.'+imagetype

        product.updateImage(imagename, source, imagetype)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'namesubmit' in request.POST:
        data = request.POST
        name = data['nameinput']

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        product.updateName(name)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'descsubmit' in request.POST:
        data = request.POST
        desc = data['descinput']

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        product.updateDescription(desc)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/update.html', context)

    elif request.method == 'POST' and 'pricesubmit' in request.POST:
        data = request.POST
        price = data['priceinput']

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        product.updatePrice(price)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/update.html', context)

    else:
        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/update.html', context)

#delete
@staff_member_required
def deleteproduct(request):

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        data = request.POST

        name = data['title']

        product = Product(name)

        productid = product.getProductId()
        if productid is False:
            form = SearchForm()
            context = {'form':form, 'warningflag':True}
            return render(request,'mobileadmin/product/delete.html', context)

        product.pullProduct()

        imageurl = product.getImage()

        jsonStr = product.to_json()
        f = open("temp.json", "w")
        f.write(jsonStr)
        f.close()

        context = {'form':form, 'searchvisibility':True, 'dispflag':True, 'name':product.name, 'desc':product.description, 'imagepath': imageurl, 'price': product.price}
        return render(request,'mobileadmin/product/delete.html', context)

    if request.method == 'POST' and 'delete' in request.POST:

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        product = Product(jsonobj=jsonobject)

        product.deleteProduct()

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/delete.html', context)

    else:
        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/delete.html', context)

############################################################################################################################################################

#item

#add
@staff_member_required
def additem(request):

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name') 
            desc = form.cleaned_data.get('description') 
            img = form.cleaned_data.get('image') 
            obj = Itemmodel.objects.create( 
                                 name = name, 
                                 description = desc, 
                                 image = img
                                 ) 
            obj.save() 

        imagedata = request.FILES
        data = request.POST

        imagenamedata = imagedata['image'].name.split('.')
        imagename = imagenamedata[0]
        imagetype = imagenamedata[1]

        name = data['name']
        desc = data['description']

        source = "/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/static/mobileadmin/images/cache/"+imagename+'.'+imagetype

        item = Item(name=name, description=desc)
        item.addImage(imagename, source, imagetype)
        item.addItem()

    else:
        form = ItemForm()


    context = {'form':form}
    return render(request,'mobileadmin/item/add.html', context)

#update
@staff_member_required
def updateitem(request):

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        data = request.POST

        name = data['title']

        item = Item(name)
        
        itemid = item.getItemId()

        if itemid is False:
            form = SearchForm()
            context = {'form':form, 'warningflag':True}
            return render(request,'mobileadmin/item/update.html', context)    

        item.pullItem()

        imageurl = item.getImage()

        jsonStr = item.to_json()
        f = open("temp.json", "w")
        f.write(jsonStr)
        f.close()

        context = {'form':form, 'searchvisibility':True, 'dispflag':True, 'name':item.name, 'desc':item.description, 'imagepath': imageurl}
        return render(request,'mobileadmin/item/update.html', context)

    elif request.method == 'POST' and 'image' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        item = Item(jsonobj=jsonobject)

        imageurl = item.getImage()
        context = {'form':form, 'searchvisibility':True, 'imageflag':True,'name':item.name, 'desc':item.description, 'imagepath': imageurl}
        
        return render(request,'mobileadmin/item/update.html', context)

    elif request.method == 'POST' and 'name' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        item = Item(jsonobj=jsonobject)

        imageurl = item.getImage()
        context = {'form':form, 'searchvisibility':True, 'nameflag':True,'name':item.name, 'desc':item.description, 'imagepath': imageurl}

        return render(request,'mobileadmin/item/update.html', context)

    elif request.method == 'POST' and 'description' in request.POST:
        form = SearchForm(request.POST)

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        item = Item(jsonobj=jsonobject)

        imageurl = item.getImage()
        context = {'form':form, 'searchvisibility':True, 'descflag':True,'name':item.name, 'desc':item.description, 'imagepath': imageurl}
        
        return render(request,'mobileadmin/item/update.html', context)

    elif request.method == 'POST' and 'imagesubmit' in request.POST:
        data = request.FILES
        imagedata = data['imageinput']

        obj = Itemmodel.objects.create( 
                                name = "name", 
                                description = "desc", 
                                image = imagedata
                                ) 
        obj.save() 
        
        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        item = Item(jsonobj=jsonobject)

        imagenamedata = imagedata.name.split('.')
        imagename = imagenamedata[0]
        imagetype = imagenamedata[1]

        source = "/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/static/mobileadmin/images/cache/"+imagename+'.'+imagetype

        item.updateImage(imagename, source, imagetype)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/item/update.html', context)

    elif request.method == 'POST' and 'namesubmit' in request.POST:
        data = request.POST
        name = data['nameinput']

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        item = Item(jsonobj=jsonobject)

        item.updateName(name)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/item/update.html', context)

    elif request.method == 'POST' and 'descsubmit' in request.POST:
        data = request.POST
        desc = data['descinput']

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        item = Item(jsonobj=jsonobject)

        item.updateDescription(desc)

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/item/update.html', context)

    else:
        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/product/update.html', context)

#delete
@staff_member_required
def deleteitem(request):

    if request.method == 'POST' and 'search' in request.POST:
        form = SearchForm(request.POST)

        data = request.POST

        name = data['title']

        item = Item(name)

        itemid = item.getItemId()
        if itemid is False:
            form = SearchForm()
            context = {'form':form, 'warningflag':True}
            return render(request,'mobileadmin/item/delete.html', context)

        item.pullItem()

        imageurl = item.getImage()

        jsonStr = item.to_json()
        f = open("temp.json", "w")
        f.write(jsonStr)
        f.close()

        context = {'form':form, 'searchvisibility':True, 'dispflag':True, 'name':item.name, 'desc':item.description, 'imagepath': imageurl}
        return render(request,'mobileadmin/item/delete.html', context)

    if request.method == 'POST' and 'delete' in request.POST:

        f = open("temp.json", "r")
        jsonStr = f.read()
        f.close()

        jsonobject = json.loads(jsonStr)
        item = Item(jsonobj=jsonobject)

        item.deleteItem()

        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/item/delete.html', context)

    else:
        form = SearchForm()
        context = {'form':form}
        return render(request,'mobileadmin/item/delete.html', context)

############################################################################################################################################################