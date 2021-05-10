import classProduct

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product): # id, name, price, category
        # Wanted to instantiate Product(id, name, price, category)
        # do i need to add all arguments used for instantiation?
        # new_product = Product(0, "Cuvee - Ethiopian", 12.99, "Coffee & Tea")
        # can i call an instantiated product FROM product class (line 21)
        # new_product = Product(coffee) - CAN I DO THIS OR:
        # but i wont have a "name" for the product as I'm storing it in new_product, right...
        self.products.append(new_product) 
        return self

    def sell_product(self, product_id):
        for i in range(len(self.products)):
            if i == product_id:
                sold_product = self.products.pop(i)
                print(f"Sold: {sold_product}. Removed from cart.")

    #  increases the price of each product by the percent_increase given 
    #  (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        print("Code for inflation goes here")
        for i in range(len(self.products)):
            if i == product_id:
                # Can I instantiate Product and call a Product Method here?
                print("Call Product Method - update_price")
        
    #  updates all the products matching the given category by reducing 
    #  the price by the percent_discount given (use the method you wrote 
    #  in the Product class!)
    def set_clearance(self, category, percent_discount):
        print("Code for clearance goes here")
        # Can I instantiate Product and call a Product Method here?
        for i in range(len(self.products)):
            if i == category:
                print("Call Product Method - update_price")


aldi = Store("Aldi")
print(aldi.name)
aldi.add_product("coffee").add_product("green beans").add_product("cinnamon rolls")
print(aldi.products)
aldi.sell_product(1)
print(aldi.products)