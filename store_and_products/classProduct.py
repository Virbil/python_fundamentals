class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

# If is_increased is True, the price should increase by the percent_change provided. 
# If False, the price should decrease by the percent_change provided.
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += percent_change * self.price
        else:
            self.price -= percent_change * self.price

# print the name of the product, its category, and its price.
    def print_info(self):
        print(f"Product: {self.name}. Category: {self.category}. Price: ${self.price}")


coffee = Product(0, "Cuvee - Ethiopian", 12.99, "Coffee & Tea")
cinnamon_rolls = Product(1, "Annie's Cinnamon Rolls", 3.49, "Breakfast")
green_beans = Product(2, "Big O' Green Beans", 0.99, "Canned Veggies")
cereal = Product(3, "Kashi Vanilla Wheat", 4.29, "Breakfast")