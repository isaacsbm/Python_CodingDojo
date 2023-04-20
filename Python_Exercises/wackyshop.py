# Worldy wacky shop of wonders!!!!

# Together as a group, come up with an idea for a shop that sells anything you want. (CLASS SHOP)
# Think about what a shop might have as attributes, maybe a name, address, list of items etc
# Associate that Shop with another class called Inventory (CLASS INVENTORY)
# Give the inventory a name and a price.

# Create the items first and then create the Shop and add the items to the shops inventory (TO CALL)
# Make a method to loop through the inventory and display the info of each item - think about how you can simplify that code in the class

# Bonus: create a staticmethod to check and make sure in the Item class: the name is not an empty string and the price is greater than 0
# Bonus: Validate the values before creating the Item and print "Not valid" if it fails
# Bonus: Add some more methods together and embrace your creativity!

# First Try: 
class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.item_list = []
    def order_item(self, item):
        self.item_list.append(item)
        # print(f"{item.name} : {item.price}")
    def display_item_info(self):
        for item in self.item_list:
            print(f"{item.name}: {item.price}")

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

fruit_shop=Shop("Fruit Shop", "1234 Fruit Street")
apple=Item("apple", 3.99)
item2=Item("kiwi", 3.00)
item3=Item("banana", 1.50)
item4=Item("starfruit", 1.99)

fruit_shop.order_item(apple)
fruit_shop.order_item(item2)
fruit_shop.order_item(item3)
fruit_shop.display_item_info()


# Second Try: 
class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []
    def add_item(self,item_data_list):
        self.inventory = Item.create_inventory(item_data_list)
    def display_item_info(self):
        for item in self.inventory:
            print(f"{item.name}: {item.price}")

class Item:
    def __init__(self, item):
        self.name = item["name"]
        self.price = item["price"]
    @classmethod
    def create_inventory(cls, item_data_list):
        inventory = []
        for item_data in item_data_list:
            inventory.append(Item(item_data))
        return inventory

car_data_list = [
        {"name": "Nissan",
        "price": 27000},
        {"name": "Mazada",
        "price": 26000
        },
        {"name": "Mustang",
        "price": 26500
        },
        {"name": "Nissan",
        "price": 27000}
    ]

# car_item_list=[]
# for car in car_data_list:
#     car_item_list.append(Item(car))

car_shop = Shop("Ninja Cars", "1234 Maple St.")
print(car_shop.inventory)
car_shop.add_item(car_data_list)
print(car_shop.inventory)
car_shop.display_item_info()


