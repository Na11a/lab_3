from enum import Enum


class ShopManager:
    def __init__(self,product_list = list):
        self.goods = product_list
    
    def search_by_price(self,price):
        out_list = []
        for el in self.goods:
            if el.price == price:
                out_list.append(el)
        return out_list

    def search_by_metherial(self,metherial):
        out_list = []
        for el in self.goods:
            if el.metherial == metherial:
                out_list.append(el)
        return out_list
    
    def sort_by_price(self,order = True):
        out_list = []
        self.goods.sort(key= lambda x: x.price,reverse=order)
        out_list = self.goods
        return out_list