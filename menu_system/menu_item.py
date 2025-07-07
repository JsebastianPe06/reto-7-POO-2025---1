"""
This module contain the class for create items of menu
"""

class MenuItem:
    def __init__(self, name:str, price:float, quantity:int):
        self._name = name
        self._price = price
        self.quantity = quantity
        self._specific_discount:float = 0
        self.__password = "123456"
        self._condition_discount = False

    def price_total(self)->float:
        return self._price*self.quantity

    def get_name(self)->str:
        return self._name

    def set_name(self, new_name:str)->str:
        insert = input("Password: ")
        if(insert == self.__password):
            self._name = new_name
        else:
            return("Access denied")
        return self._name

    def get_condition_discount(self)->bool:
        return self._condition_discount

    def set_condition_discount(self, new_condition_discount:bool, password:str)->bool:
        if(password == self.__password):
            self._condition_discount = new_condition_discount
        else:
            return("Access denied")
        return self._condition_discount

    def get_price(self)->float:
        return self._price

    def set_price(self, new_price:str)->float:
        insert = input("Password: ")
        if(insert == self.__password):
            self._price = new_price
        else:
            return("Access denied")
        return self._price

    def get_specific_discount(self)->float:
        return self._specific_discount

    def set_specific_discount(self, new_specific_discount:float)->float:
        if(self._condition_discount):
            self._specific_discount = new_specific_discount
        else:
            insert = input("Password: ")
            if(insert == self.__password):
                self._specific_discount = new_specific_discount
            else:
                return("Access denied")
        return self._specific_discount

    def get_password(self)->str:
        i = ""
        for j in self.__password:
            i += "*"
        return f"password: {i}"

    def set_password(self, new_password)->str:
        insert = input("Password: ")
        if(insert == self.__password):
            self.__password = new_password
        else:
            return("Access denied")
        return self.__password

    def __str__(self):
        return f"{self._name}: {self._price}$"

class Appetizer(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, size:str):
        super().__init__(name, price, quantity)
        self._size = size

    def get_size(self)->str:
        return self._size

    def set_size(self, new_size:str)->str:
        insert = input("Password: ")
        if(insert == self.__password):
            self._name = new_size
        else:
            return("Access denied")
        return self._size

class Drink(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, type_:str):
        super().__init__(name, price, quantity)
        self._type = type_

    def get_type(self)->str:
        return self._type

    def set_type(self, new_type:str)->str:
        insert = input("Password: ")
        if(insert == self.__password):
            self._type = new_type
        else:
            return("Access denied")
        return self._type

class MainCourse(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, vegetarian:bool,
                family_size:bool):
        super().__init__(name, price, quantity)
        self._vegetarian = vegetarian
        self._family_size = family_size

    def get_vegetarian(self)->bool:
        return self._vegetarian

    def set_vegetarian(self, new_vegetarian:bool)->bool:
        insert = input("Password: ")
        if(insert == self.__password):
            self._vegetarian = new_vegetarian
        else:
            return("Access denied")
        return self._vegetarian

    def get_family_size(self)->bool:
        return self._family_size
    
    def set_family_size(self, new_family_size:bool)->bool:
        insert = input("Password: ")
        if(insert == self.__password):
            self._family_size = new_family_size
        else:
            return("Access denied")
        return self._family_size

class Dessert(MenuItem):
    def __init__(self, name:str, price:float, quantity:int, size:str):
        super().__init__(name, price, quantity)
        self._size = size

    def get_size(self)->str:
        return self._size

    def set_size(self, new_size:str)->str:
        insert = input("Password: ")
        if(insert == self.__password):
            self._size = new_size
        else:
            return("Access denied")
        return self._size