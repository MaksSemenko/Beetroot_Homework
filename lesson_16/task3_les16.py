class Product:
    def __init__(self, its_type, name, price):
        self.its_type = its_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self, income=0):
        self.income = income
        self.products = {}
        pass

    def add(self, product, amount):
        product_dict = {}
        product_dict['name'] = product.name
        product_dict['amount'] = amount
        product_dict['price'] = round(product.price * 1.3, 2)
        product_dict['its_type'] = product.its_type
        self.products[product.name] = product_dict
        return self.products

    def set_discount(self, identifier, percent):
        self.products[identifier]['price'] = self.products[identifier]['price'] * ((100-percent)/100)
        return self.products[identifier]['price']

    def sell_product(self, product_name, amount):
        try:
            if self.products[product_name]['amount'] >= amount:
                self.products[product_name]['amount'] -= amount
                self.income += self.products[product_name]['price'] * amount
            else:
                raise ValueError
        except ValueError:
            print(f"There is not enough {self.products[product_name]['name']} "
                  f"in the store!")
        return

    def get_income(self):
        return round(self.income, 2)

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        return product_name, self.products[product_name]['amount']


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
print(s.get_income())
print(s.get_product_info('Ramen'))
print(s.products)
