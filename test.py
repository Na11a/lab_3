import unittest

from models.pillow import Pillow
from models.sheet import Sheet
from models.item import Item
from models.liners import Liners
from manager.shopManager import ShopManager
from models.towel import Towel
from models.item import Metherial

class TestShopManager(unittest.TestCase):
    sheet = Sheet(name = "sheet",price = 124,code = '1234',metherial=Metherial.NATURAL)
    pillow = Pillow(name = "pillow", price = 1325, code = "125",metherial=Metherial.SYNTHETIC)
    towel = Towel(price=100,code="123456", name = "towel",metherial=Metherial.ARTIFICIAL)

    test_manager = ShopManager([sheet,pillow,towel])

    def test_search_by_price(self):
        self.assertEqual(self.test_manager.search_by_price(1325),[self.pillow])
    
    def test_sort_by_price(self):
        self.assertEqual(self.test_manager.sort_by_price(False),[self.towel,self.sheet,self.pillow])
    
    def test_search_by_metherial(self):
        self.assertEqual(self.test_manager.search_by_metherial(Metherial.NATURAL),[self.sheet])

if __name__ == "__main__":
    unittest.main()
