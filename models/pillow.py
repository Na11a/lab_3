from enum import Enum
from .item import Item
from .item import OriginCountry
from .item import Metherial

class PillowForm(Enum):
    CIRCLE = 0
    SQUARE = 1

class Pillow(Item):
    def __init__(self,name, price, metherial = Metherial.NATURAL, origin_country = OriginCountry.UKRAINE,code = "",width = 15,height = 30, length = 45,color = "black",form = PillowForm.SQUARE):
        super().__init__(name = name, price = price, code = code)
        self.width = width
        self.heigth = height
        self.length = length
        self.color = color
        self.form = form
    
    def __str__(self):
        return "width:{}\n heigth: {} \n length:{} \n form: {} \n color: {} \n".format(self.width,self.heigth,self.length,self.form,self.color)
         
pillow = Pillow(name = "pillow", price = 1325, code = "125")
