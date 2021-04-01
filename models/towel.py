from .item import Item
from .item import OriginCountry,Metherial

class Towel(Item):
    def __init__(self,name, price,width_mm = 200,length_mm = 300, number_in_the_set = 2,metherial = Metherial.NATURAL, origin_country = OriginCountry.UKRAINE,code = "",with_print = False):
        super().__init__(price = price,name = name,code = code)
        self.width_mm = width_mm
        self.length_mm = length_mm
        self.number_in_the_set = number_in_the_set
        self.with_print = with_print
    def __str__(self):
        return "width_mm = {}\n length_mm = {}\n number_in_the_set = {}\n with_print = {}".format(self.width_mm, self.length_mm,self.number_in_the_set,self.with_print)

towel = Towel(price=100,code="123456", name = "towel" )
