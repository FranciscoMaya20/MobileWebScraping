from item import Item

class Item_List:

    #Need to make list a dict
    def __init__(self):
        self.items_List = []

    def addItem(self,currentItem):
        #Probably needs more checks
        if currentItem is Item:
            self.items_List.append(currentItem)
        else:
            raise Exception("ITEM IS NOT TYPE ITEM")

    def removeItem(self,currentItem):
        if currentItem in self.items_List and currentItem is Item:
            self.items_List.remove(currentItem)
        else:
            raise Exception("ERROR REMOVING ITEM")

    def getItemList(self):
        return self.items_List

    def getItemInfo(self):
        #Todo
        pass
    def findBestPrice(self,currentItem):
        #Need to change to dict first
        pass
