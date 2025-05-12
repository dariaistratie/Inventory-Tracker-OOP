#Create a class
class Item:
    total_items = 0  # Class variable to count total items created
    all_items = []  # List to store all items created

    def __init__(self,name,category,price):
        self.name=name
        self.category=category
        self.price=price
        Item.total_items +=1 # Increase the count of total items created when a new item is added

    def get_details(self):
        return f"{self.name} and category:{self.category} and price:{self.price}"

    @classmethod

    def items_in_category(cls, category):
        count = sum(1 for item in cls.all_items if item.category == category)
        return f"There are {count} items in the {category} category."

    @staticmethod
    def is_expired(name):
        expired_items=['milk','bread']  # Example expired items
        return name.lower() in expired_items

    @classmethod
    def add_item(cls,item):
        cls.all_items.append(item)

# Create some items
item1 = Item("Milk", "Dairy", 2.5)
item2 = Item("Bread", "Bakery", 1.5)
item3 = Item("Laptop", "Electronics", 999.99)

# Add items to the global list
Item.add_item(item1)
Item.add_item(item2)
Item.add_item(item3)

# Print item details using instance method
print(item1.get_details())  # Milk  Category: Dairy Price: $2.5
print(item2.get_details())  # Bread Category: Bakery  Price: $1.5

# Check total items in a category using class method
print(Item.items_in_category("Dairy"))  # There are one items in the Dairy category.
print(Item.items_in_category("Electronics"))  # There are one items in the Electronics category.

# Check if an item is expired using static method
print(Item.is_expired("Milk"))  # True (expired)
print(Item.is_expired("Laptop"))  # False (not expired)
