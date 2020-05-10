from mobileadmin.Firebaseengine import Firebaseengine as Fb

class Event:

    def __init__(self, title='', description='', imagepath='', eventid='', jsonobj=''):

        if jsonobj == '':
            self.title = title
            self.imagepath = imagepath
            self.description = description 
            self.eventid = eventid
            self.collectionid = 'events'
            self.folder = 'events-pictures'
        else:
            self.title = jsonobj["title"]
            self.imagepath = jsonobj["imagepath"]
            self.description = jsonobj["description"]
            self.eventid = jsonobj["eventid"]
            self.collectionid = jsonobj["collectionid"]
            self.folder = jsonobj["folder"]


        self.fb = Fb(path='/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/authkey/chiguru-mobile-app-firebase-adminsdk-k59u9-308aabfbcd.json', appid='chiguru-mobile-app.appspot.com')
    
    def to_dict(self):
        return { 'Title':self.title, "Imagepath":self.imagepath, "Description":self.description }

    def to_json(self):
        return '{ "title":"'+ self.title +'", "description":"'+ self.description +'", "imagepath":"'+ self.imagepath +'", "eventid":"'+ self.eventid +'", "collectionid":"'+ self.collectionid +'", "folder":"'+ self.folder +'"}'
    
    def to_event(self, objectdict):
        self.title = objectdict['Title']
        self.imagepath = objectdict['Imagepath']
        self.description = objectdict['Description']

    def print_event(self):
        print("{} {} \n\n{} \n\n{}".format(self.eventid, self.title, self.description, self.imagepath))

    def addEvent(self):
        self.eventid = self.fb.addObject(self.collectionid, self.to_dict())

    def updateEvent(self):
        self.fb.updateObject(self.collectionid, self.eventid, self.to_dict())

    def deleteEvent(self):
        self.fb.deleteObject(self.folder, self.imagepath, self.collectionid, self.eventid)

    def addImage(self, imagename, source, imagetype='jpg'):
        self.imagepath = self.fb.addImage(self.folder, imagename, source, imagetype)

    def updateImage(self, imagename, source, imagetype='jpg'):

        #update the image
        self.imagepath = self.fb.updateImage(self.imagepath, self.folder, imagename, source, imagetype)

        #update the image path
        data = {'Title': self.title, 'Description': self.description, 'Imagepath': self.imagepath}
        self.fb.updateObject(self.collectionid, self.eventid, data)

    def updateTitle(self, newtitle):

        self.title = newtitle

        #update the title
        data = {'Title': self.title, 'Description': self.description, 'Imagepath': self.imagepath}
        self.fb.updateObject(self.collectionid, self.eventid, data)

    def updateDescription(self, newdesc):

        self.description = newdesc

        #update the title
        data = {'Title': self.title, 'Description': self.description, 'Imagepath': self.imagepath}
        self.fb.updateObject(self.collectionid, self.eventid, data)  

    def getEventId(self):
        eventid = self.fb.getDocumentId(self.collectionid, self.to_dict())

        if eventid == False:
            return False

        self.eventid = eventid
        return self.eventid

    def pullEvent(self):
        objectdict = self.fb.getDocumentContent(self.collectionid, self.to_dict())

        if objectdict == False:
            return False

        self.to_event(objectdict)

    def getImage(self):
        return self.fb.getImage(self.folder, self.imagepath)