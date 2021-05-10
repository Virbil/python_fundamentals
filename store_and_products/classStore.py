from classProduct import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product) 
        return self

    def list_products(self):
        for product in self.products:
            # since product is an object instantiation,
            product.print_info()

    def sell_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                sold_product = self.products.pop(product.product_id)
                print(f"Sold: {sold_product.name}. Removed from cart.")

    #  increases the price of each product by the percent_increase given 
    #  (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        
    #  updates all the products matching the given category by reducing 
    #  the price by the percent_discount given (use the method you wrote 
    #  in the Product class!)
    def set_clearance(self, category, percent_discount):
        print("Code for clearance goes here")
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)