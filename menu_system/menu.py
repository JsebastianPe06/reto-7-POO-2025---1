from collections import namedtuple
import json
import os
from copy import deepcopy

from .menu_item import MenuItem, Appetizer, Dessert, Drink, MainCourse
from .order import Order

#Menu
bruschetta = Appetizer("Bruschetta", 8, 1, "Medium")
cheese_nachos = Appetizer("Cheese Nachos", 10, 1, "Large")
coca_cola = Drink("Coca Cola", 3, 1, "Soda")
orange_juice = Drink("Orange Juice", 4, 1, "Natural")
coffee = Drink("Coffee", 5, 1, "Hot")
alfredo_pasta = MainCourse("Alfredo Pasta", 15, 1, True, False)
burger = MainCourse("Burger", 12, 1, False, False)
family_grill = MainCourse("Family Grill", 35, 1, False, True)
chocolate_cake = Dessert("Chocolate Cake", 6, 1, "Medium")
vanilla_ice_cream = Dessert("Vanilla Ice Cream", 4, 1, "Small")
cheesecake = Dessert("Cheesecake", 7, 1, "Large")
caesar_salad = MainCourse("Caesar Salad", 10, 1, True, False)

## Special combos using namedtuples
personal_combo = namedtuple("Order", ["drink", "appetizer", "Maincourse"])
couple_combo = namedtuple("Order", ["drink1", "drink2", "appetizer", "mainCourse1",
                                    "maincourse2", "dessert"])
family_combo = namedtuple("Order", [ "drink1", "drink2","drink3", "drink4",
                                    "appetizer", "mainCourse1", "maincourse2", 
                                    "mainCourse3", "maincourse4","dessert1",
                                    "dessert2"])

menu_ = [
    bruschetta, cheese_nachos, coca_cola, orange_juice, coffee, alfredo_pasta,
    burger, family_grill, chocolate_cake, vanilla_ice_cream, cheesecake,
    caesar_salad
]

#Discount
"""None"""

###############################################################################
class Menu:
    """
    Create a new_menu with .json
    """
    def __init__(self, name:str):
        self.name = name
        self.__path_file = f"data/{name}.json" #path_file cannot be modified
        self.menu = self.load_menu()

    def load_menu(self):
        if os.path.exists(self.__path_file):
            with open(self.__path_file, 'r') as file:
                return json.load(file)
        print("Create menu")
        return {}

    def save_menu(self):
        with open(self.__path_file, 'w') as file:
            json.dump(self.menu, file, indent=4)
        print("file save")

    @staticmethod
    def to_sub_dictionary(item: MenuItem):
        if isinstance(item, MenuItem):
            return {
                attribute.lstrip('_'): value
                for attribute, value in item.__dict__.items()
                if "__" not in attribute and value != item.get_name()
            }

    def add_item(self, new_item:MenuItem ):
        if isinstance(new_item, MenuItem):
            if new_item.get_name() not in self.menu:
                self.menu[new_item.get_name()] = self.to_sub_dictionary(new_item)
                self.save_menu()
        else:
            return f"The item already exists in {self.name} or isn't a MenuItem"

    def update_item(self, name_item:str, changes:dict):
            if name_item in self.menu:
                copy_item = deepcopy(self.menu[name_item])
                for attribute, value in changes.items():
                        if attribute in self.menu[name_item]:
                            self.menu[name_item][attribute] = value
                        else:
                            self.menu[name_item] = copy_item
                            return "Error. make sure that the attributes to be changed exist"
                self.save_menu()
            else:
                return "Error. item not found"

    def delete_item(self, name_item:str):
        if name_item in self.menu:
            del self.menu[name_item]
            self.save_menu()
        else:
            return "Item no found"

    def __str__(self):
        if not self.menu:
            return f"Menu '{self.name}' is empty."
        output = f"Menu '{self.name}':\n"
        for item_name, attributes in self.menu.items():
            output += f"  - {item_name}:\n"
            for attr, value in attributes.items():
                output += f"      {attr}: {value}\n"
        return output
###############################################################################