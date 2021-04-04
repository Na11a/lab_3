from .item import Item
from .item import Metherial
from .item import OriginCountry

class Sheet(Item):
    def __init__(self,name, price, metherial = Metherial.NATURAL, origin_country = OriginCountry.UKRAINE,code = "",color = "blue",width_mm = 300,length_mm =200):
        super().__init__(name = name,price = price,code = code)
        self.color = color
        self.width_mm = width_mm
        self.length_mm = length_mm
    def __str__(self):
        return " name = {}\n color = {}\n width_mm = {}\n length_mm = {}\n".format(self.name,self.color,self.width_mm, self.length_mm)

sheet = Sheet(name = "sheet",price = 124,code = '1234')
