from Objects.itemList import Item_List
from Objects.item import Item

class User_Account():
    def __init__(self,email,password,rememberMe=False):
        self.userItemList = Item_List()
        self.email = email
        self.password = password

    def setEmail(self,email):
        #need to add checking for @
        if email is str:
            self.email = email
        else:
             raise Exception("INVALID EMAIL")

    def getEmail(self):
        return self.email

    def setPassword(self,password):
        #Add a check for Special Characters
        if password is str and len(password)>=6:
            self.password = password
        else:
            raise Exception("Please make password longer")
    def updateRememberMe(self):
        if self.rememberMe==False:
            self.rememberMe = True
        else:
            self.rememberMe = False 

    def addItem(self,item):
        self.userItemList.addItem(item)
    
    def getItemList(self):
        return self.userItemList.getItemList()

    def removeItem(self,item):
        if item is Item and item in self.userItemList:
            self.userItemList.removeItem(item)
        else:
            raise Exception("ITEM NOT ON LIST")