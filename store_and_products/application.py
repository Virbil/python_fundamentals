from classStore import Store
from classProduct import Product

aldi = Store("Aldi")

coffee = Product(0, "Cuvee - Ethiopian", 12.99, "Coffee & Tea")
cinnamon_rolls = Product(1, "Annie's Cinnamon Rolls", 3.49, "Breakfast")
green_beans = Product(2, "Big O' Green Beans", 0.99, "Canned Veggies")
cereal = Product(3, "Kashi Vanilla Wheat", 4.29, "Breakfast")




print(aldi.name)
aldi.add_product(coffee).add_product(green_beans).add_product(cinnamon_rolls).add_product(cereal)
aldi.list_products()
aldi.sell_product(1)
aldi.inflation(0.01)
print("Inflation, oh no! New prices:")
aldi.list_products()
print("Yay, It's CLEARANCE DAY!!!!")
aldi.set_clearance("Breakfast", 0.1)
aldi.list_products()