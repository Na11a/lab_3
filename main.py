
if __name__ == "__main__":
    from models.pillow import Pillow
    from models.sheet import Sheet
    from models.item import Item
    from models.liners import Liners
    from manager.shopManager import ShopManager
    from models.towel import Towel
    from models.item import Metherial

    sheet = Sheet(name = "sheet",price = 124,code = '1234')
    pillow = Pillow(name = "pillow", price = 1325, code = "125")
    towel = Towel(price=100,code="123456", name = "towel" )

    shop_manager = ShopManager([sheet,pillow,towel])
    goods_sorted_by_price = shop_manager.sort_by_price()
    have_natural_metherial = shop_manager.search_by_metherial(Metherial.NATURAL)

    for el in list_3:
        print("name = {}, price = {}".format(el.name,el.price))
    