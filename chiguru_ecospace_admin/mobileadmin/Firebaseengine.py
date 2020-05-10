import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

class Firebaseengine:

    def __init__(self, path, appid):

        cred = credentials.Certificate(path)     

        try:
            # Use a service account
            firebase_admin.initialize_app(cred, {
                'storageBucket': appid
            })   
        except:
            print("Firebase Engine Already initialized.")

        self.appid = appid
        self.db = firestore.client()
        self.bucket = storage.bucket()

    def addObject(self, collectionid, objectdict):
        doc_ref = self.db.collection(collectionid).add(objectdict)
        return doc_ref[1].id

    def updateObject(self, collectionid, docid, objectdict):
        self.db.collection(collectionid).document(docid).set(objectdict)

    def deleteObject(self, folder, path, collectionid, docid):

        self.deleteImage(folder, path)
        self.db.collection(collectionid).document(docid).delete()

    def addImage(self, folder, imagename, source, imagetype='jpg'):
        destination_blob_name = folder + "/" + imagename + "." + imagetype
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(source)
        return "gs://" + self.appid + "/" + folder + "/" + imagename + "." + imagetype

    def updateImage(self, oldpath, folder, imagename, source, imagetype='jpg'):

        #delete the old image
        self.deleteImage(folder, oldpath)

        #add the new image and return the new path
        return self.addImage(folder, imagename, source, imagetype)


    def getDocument(self, collectionid, objectdict):
        # Create a reference to the collection
        doc_ref = self.db.collection(collectionid)

        # Create a query against the collection
        for key, value in objectdict.items():

            if len(value) > 50:
                continue
            
            docs = doc_ref.where(key, u'==', value).stream()

            if docs is not None:
                for doc in docs:
                    if doc is not None:
                        return doc

        return False

    def getDocumentId(self, collectionid, objectdict):
        
        doc = self.getDocument(collectionid, objectdict)

        if doc != False:
            return doc.id

        return False

    def getDocumentContent(self, collectionid, objectdict):
        
        doc = self.getDocument(collectionid, objectdict)

        if doc != False:
            return doc.to_dict()

        return False

    def getImage(self, folder, path):
        blob = self.bucket.blob(folder + '/' + path.split('/')[-1])
        blob.from_string(path)
        return blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')

    def deleteImage(self, folder, path):
        blob = self.bucket.blob(folder + '/' + path.split('/')[-1])
        blob.from_string(path)
        blob.delete()