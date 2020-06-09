# Practice creating classes
# Practice associating classes
# Practice modularizing code

class Store:
    def __init__(self, name, prod_list=[]):
        self.name = name
        self.products = prod_list

    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        print("Name: {}, Price: {}, Category {}".format(self.products[id].name,self.products[i].price, self.products[i].category))
        del self.products[id]

    def inflation(self, percent_increase):
        for i in range (len(self.products)):
            self.products[i].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for i in range (len(self.products)):
            if (self.products[i].category == category):
                self.products[i].update_price(percent_discount, False)

    def view_products(self):
        print("*"*10+self.name,"Products"+"*"*10)
        for i in range (len(self.products)):
            self.products[i].print_info()

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if (is_increased == True):
            self.price += (self.price*percent_change)
        else:
            self.price -= (self.price*percent_change)
        return self

    def print_info(self):
        print("="*20)
        print("Name:", self.name)
        print("Price: ${}".format(self.price))
        print("Category:", self.category)
        print("="*20)


supply_shop = Store("Supply Store")

pencil = Product("pencil", 1.00, "draw")
paintbrush = Product("paintbrush", 3.00, "draw")
mug = Product("mug", 5.00, "drink")
bottle = Product("water bottle", 5.00, "drink")

supply_shop.add_product(pencil).add_product(paintbrush).add_product(mug).add_product(bottle)

supply_shop.view_products()
supply_shop.set_clearance("draw", 0.1)
supply_shop.view_products()