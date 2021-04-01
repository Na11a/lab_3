from .pillow import Pillow
from .sheet import Sheet

class Liners(Pillow,Sheet):
    def __init__(self,name_pillow, name_sheet, price_pillow, price_sheet,pillowcases = 1, design = "standart"):
        self.pillow = Pillow(name = name_pillow,price= price_pillow)
        self.sheet = Sheet(name = name_sheet, price = price_sheet)
        self.pillowcases = pillowcases
        self.design = design
    def __str__(self):
        return "Pillow = {}\n Sheet = {}\n pillowcases = {}\n design = {}\n".format(self.pillow,self.sheet,self.pillowcases,self.design)

