from enum import Enum

class Metherial(Enum):
    
    NATURAL = 1 
    ARTIFICIAL = 2 
    SYNTHETIC = 3

class OriginCountry(Enum):
    
    UKRAINE = 1
    CHINA = 2
    USA = 3
    GERMAN = 4


class Item():
    def __init__(self,name, price, metherial = Metherial.NATURAL, origin_country = OriginCountry.UKRAINE,code = ""):
        self.__name = name
        self.__price = price
        self.__metherial = metherial
        self.__origin_country = origin_country
        self.__code = code

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price = price
    
    @property
    def metherial(self):
        return self.__metherial
    @metherial.setter
    def metherial(self,metherial):
        self.__metherial = metherial

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,code):
        self.__code = code
  
