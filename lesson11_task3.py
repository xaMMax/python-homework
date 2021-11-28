class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:

    def __init__(self):
        self.produ_dict = {}
        self.ammount = int

    def add(self, product, amount):
        produ_dict = {product: amount}
        return produ_dict

    def set_discount(self, ident, percent, ident_type = 'name'):
        pass
    def sell_product(self, product_name, amount):
        pass
    def get_income(self):
        pass
    def get_all_products(self):
        pass
    def get_product_info(self, product_name):
        info = (p.name,)
        return info


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.get_product_info('Football T-Shirt')