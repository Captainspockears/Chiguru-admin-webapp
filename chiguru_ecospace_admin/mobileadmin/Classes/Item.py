from mobileadmin.Firebaseengine import Firebaseengine as Fb

class Item:

    def __init__(self, name='', description='', imagepath='', itemid='', jsonobj=''):

        if jsonobj == '':
            self.name = name
            self.imagepath = imagepath
            self.description = description 
            self.itemid = itemid
            self.collectionid = 'items'
            self.folder = 'items-pictures'
        else:
            self.name = jsonobj["name"]
            self.imagepath = jsonobj["imagepath"]
            self.description = jsonobj["description"]
            self.itemid = jsonobj["itemid"]
            self.collectionid = jsonobj["collectionid"]
            self.folder = jsonobj["folder"]


        self.fb = Fb(path='/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/Classes/chiguru-mobile-app-firebase-adminsdk-k59u9-308aabfbcd.json', appid='chiguru-mobile-app.appspot.com')

    def to_dict(self):

        self.imagepath = self.imagepath.split('/')[-1]
        print(self.imagepath)
        return { 'Name':self.name, "Imagepath":self.imagepath, "Description":self.description }

    def to_json(self):
        return '{ "name":"'+ self.name +'", "description":"'+ self.description +'", "imagepath":"'+ self.imagepath +'", "itemid":"'+ self.itemid +'", "collectionid":"'+ self.collectionid +'", "folder":"'+ self.folder +'"}'
    
    def to_item(self, objectdict):
        self.name = objectdict['Name']
        self.imagepath = objectdict['Imagepath']
        self.description = objectdict['Description']

    def print_item(self):
        print("{} {} \n\n{} \n\n{}".format(self.itemid, self.name, self.description, self.imagepath))

    def addItem(self):
        self.itemid = self.fb.addObject(self.collectionid, self.to_dict())

    def updateItem(self):
        self.fb.updateObject(self.collectionid, self.itemid, self.to_dict())

    def deleteItem(self):
        imagepath = "gs://chiguru-mobile-app.appspot.com/items-pictures/"+self.imagepath
        self.fb.deleteObject(self.folder, imagepath, self.collectionid, self.itemid)

    def addImage(self, imagename, source, imagetype='jpg'):
        self.imagepath = self.fb.addImage(self.folder, imagename, source, imagetype)
        self.imagepath = self.imagepath.split('/')[-1]

    def updateImage(self, imagename, source, imagetype='jpg'):

        #update the image
        imagepath = "gs://chiguru-mobile-app.appspot.com/items-pictures/"+self.imagepath
        self.imagepath = self.fb.updateImage(imagepath, self.folder, imagename, source, imagetype)

        self.imagepath = self.imagepath.split('/')[-1]
        print(self.imagepath)

        #update the image path
        data = {'Name': self.name, 'Description': self.description, 'Imagepath': self.imagepath}
        self.fb.updateObject(self.collectionid, self.itemid, data)

    def updateName(self, newname):

        self.name = newname
        self.imagepath = self.imagepath.split('/')[-1]
        print(self.imagepath)

        #update the name
        data = {'Name': self.name, 'Description': self.description, 'Imagepath': self.imagepath}
        self.fb.updateObject(self.collectionid, self.itemid, data)

    def updateDescription(self, newdesc):

        self.description = newdesc
        self.imagepath = self.imagepath.split('/')[-1]
        print(self.imagepath)

        #update the desc
        data = {'Name': self.name, 'Description': self.description, 'Imagepath': self.imagepath}
        self.fb.updateObject(self.collectionid, self.itemid, data)  

    def getItemId(self):
        itemid = self.fb.getDocumentId(self.collectionid, self.to_dict())

        if itemid == False:
            return False

        self.itemid = itemid
        return self.itemid

    def pullItem(self):
        objectdict = self.fb.getDocumentContent(self.collectionid, self.to_dict())

        if objectdict == False:
            return False

        self.to_item(objectdict)

    def getImage(self):
        imagepath = "gs://chiguru-mobile-app.appspot.com/items-pictures/"+self.imagepath
        return self.fb.getImage(self.folder, imagepath)