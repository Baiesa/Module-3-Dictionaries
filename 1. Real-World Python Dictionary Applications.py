'''
Objective:
The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, 
and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, 
demonstrating your ability to manipulate and manage complex data structures.

Task 1: Restaurant Menu Update
You are given an initial structure of a restaurant menu stored in a nested dictionary. 
Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries 
and manage data effectively.

Problem Statement:
Given the initial menu:

Add a new category called "Beverages" with at least two items.
Update the price of "Steak" to 17.99.
Remove "Bruschetta" from "Starters".
'''

# restaurant_menu = {
#     "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
#     "Main Course": {"Steak": 15.99, "Salmon": 13.99},
#     "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
# }
# restaurant_menu["Beverages"] = {"kabab": "12.90", "saamosa": "9.5"}
# restaurant_menu["Main Course"]["Steak"]= "17.99"
# del restaurant_menu["Starters"]["Bruschetta"]


# print("Update menu")
# for category,items in restaurant_menu.items():
#     print(f"{category}")
#     for item, price in items.items():
#          print(f" - {item}: ${price}")


def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = []
        print(f"category {category} Adeed.")
    else:
        print(f"category {category} Already exist")


def add_product(catalog, category, product):
    try:
        if product not in catalog[category]:
            catalog[category].append(product)
            print(f"product {product} Added to {category}")
        else:
            print(f"product {product} Already exist in {category}")
    except KeyError:
        print(f"category does not {category} Exist")


catalog = {"add": "abi", "Bob": "tom"}

add_category(catalog, "clothig")
add_product(catalog, "add", "camera")
print(catalog)
