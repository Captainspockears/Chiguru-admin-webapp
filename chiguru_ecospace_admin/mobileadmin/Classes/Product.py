from mobileadmin.Firebaseengine import Firebaseengine as Fb

class Product:

    def __init__(self, name='', description='', imagepath='', price='', productid='', jsonobj=''):

        if jsonobj == '':
            self.name = name
            self.imagepath = imagepath
            self.description = description 
            self.productid = productid
            self.price = price
            self.collectionid = 'shop'
            self.folder = 'shop'
        else:
            self.name = jsonobj["name"]
            self.imagepath = jsonobj["imagepath"]
            self.description = jsonobj["description"]
            self.productid = jsonobj["productid"]
            self.price = int(jsonobj["price"])
            self.collectionid = jsonobj["collectionid"]
            self.folder = jsonobj["folder"]


        self.fb = Fb(path='/home/captainspockears/Projects/Chiguru-admin-webapp/chiguru_ecospace_admin/mobileadmin/authkey/chiguru-mobile-app-firebase-adminsdk-k59u9-308aabfbcd.json', appid='chiguru-mobile-app.appspot.com')
    
    def to_dict(self):
        return { 'Name':self.name, "Imagepath":self.imagepath, "Description":self.description, "Price":self.price }

    def to_json(self):
        return '{ "name":"'+ self.name +'", "description":"'+ self.description +'", "imagepath":"'+ self.imagepath +'", "price":"'+ str(self.price) +'", "productid":"'+ self.productid +'", "collectionid":"'+ self.collectionid +'", "folder":"'+ self.folder +'"}'
    
    def to_product(self, objectdict):
        self.name = objectdict['Name']
        self.imagepath = objectdict['Imagepath']
        self.description = objectdict['Description']
        self.price = int(objectdict['Price'])

    def print_product(self):
        print("{} {} \n\n{} \n\n{} \n\n{}".format(self.productid, self.name, self.description, self.imagepath, self.price))

    def addProduct(self):
        self.productid = self.fb.addObject(self.collectionid, self.to_dict())

    def updateProduct(self):
        self.fb.updateObject(self.collectionid, self.productid, self.to_dict())

    def deleteProduct(self):
        self.fb.deleteObject(self.folder, self.imagepath, self.collectionid, self.productid)

    def addImage(self, imagename, source, imagetype='jpg'):
        self.imagepath = self.fb.addImage(self.folder, imagename, source, imagetype)

    def updateImage(self, imagename, source, imagetype='jpg'):

        #update the image
        self.imagepath = self.fb.updateImage(self.imagepath, self.folder, imagename, source, imagetype)

        #update the image path
        data = {'Name': self.name, 'Description': self.description, 'Imagepath': self.imagepath, 'Price': self.price}
        self.fb.updateObject(self.collectionid, self.productid, data)

    def updateName(self, newname):

        self.name = newname

        #update the name
        data = {'Name': self.name, 'Description': self.description, 'Imagepath': self.imagepath, 'Price': self.price}
        self.fb.updateObject(self.collectionid, self.productid, data)

    def updateDescription(self, newdesc):

        self.description = newdesc

        #update the desc
        data = {'Name': self.name, 'Description': self.description, 'Imagepath': self.imagepath, 'Price': self.price}
        self.fb.updateObject(self.collectionid, self.productid, data)  

    def updatePrice(self, newprice):

        self.price = newprice

        #update the price
        data = {'Name': self.name, 'Description': self.description, 'Imagepath': self.imagepath, 'Price': self.price}
        self.fb.updateObject(self.collectionid, self.productid, data)

    def getProductId(self):
        productid = self.fb.getDocumentId(self.collectionid, self.to_dict())

        if productid == False:
            return False

        self.productid = productid
        return self.productid

    def pullProduct(self):
        objectdict = self.fb.getDocumentContent(self.collectionid, self.to_dict())

        if objectdict == False:
            return False

        self.to_product(objectdict)

    def getImage(self):
        return self.fb.getImage(self.folder, self.imagepath)