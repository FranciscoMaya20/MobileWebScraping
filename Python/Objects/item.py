
class Item: 
    def __init__(self,UPC,price,name,):
        self.UPC = UPC
        self.price = price
        self.name = name

    def setUPC(self,UPC):
        if UPC is int and len(UPC==12):
            self.UPC = UPC
        else:
            raise Exception("INVALID UPC")

    def getUPC(self):
        return self.UPC

    def setPrice(self,price):
        if price is float:
            self.price = round(price,2)
        else:
            raise Exception ("INVALID PRICE")

    def getPrice(self):
        return self.price

    def setName(self,name):
        #Needs more checks
        if name is str:
            self.name = name
        else:
            raise Exception("INVALID NAME")

    def getName(self):
        return self.name