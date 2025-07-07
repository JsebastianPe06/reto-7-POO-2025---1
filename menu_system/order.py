from queue import Queue

from .menu_item import MenuItem, MainCourse, Dessert, Drink, Appetizer

class Order:
    def __init__(self, list_menu:list[MenuItem]):
        self.list_menu = list_menu

    def  add_items(self, item):
        self.list_menu.append(item)

    def special_discount_1(self):
        if(any(isinstance(i, MainCourse) and i.get_family_size() == 1 for i in self.list_menu)):
            for j in self.list_menu:
                if(isinstance(j, Dessert)):
                    j.set_condition_discount(True, "123456")
                    j.set_specific_discount(0.05)
                    j.set_condition_discount(False, "123456")
        return self.list_menu

    def special_discount_2(self):
        if(sum(int(isinstance(i, Drink))*i.quantity for i in self.list_menu) > 3):
            for j in self.list_menu:
                if(isinstance(j, Drink)):
                    j.set_condition_discount(True, "123456")
                    j.set_specific_discount(0.07)
                    j.set_condition_discount(False, "123456")
        return self.list_menu

    def special_discount_3(self):
        if(any(isinstance(i, Appetizer) and i.get_size() == "large" for i in self.list_menu)):
            if(any(isinstance(i, MainCourse) and i.get_family_size() == 1 for i in self.list_menu)):
                for j in self.list_menu:
                    if(isinstance(j, Appetizer)):
                        j.set_condition_discount(True, "123456")
                        j.set_specific_discount(0.25)
                        j.set_condition_discount(False, "123456")
                        break
        return self.list_menu

    def total_bill_amount(self)->float:
        self.special_discount_1()
        self.special_discount_2()
        self.special_discount_3()
        total = sum(i.price_total()*(1-i.get_specific_discount())
                    for i in self.list_menu)
        return total

    def __str__(self):
        print_code = "Order:\n"
        for i in range(len(self.list_menu)):
            print_code += f" ({i+1}). {self.list_menu[i]}"
            self.special_discount_1()
            self.special_discount_2()
            self.special_discount_3()
            if(self.list_menu[i].get_specific_discount() != 0):
                print_code += f" (-{self.list_menu[i].get_specific_discount()}$)"
            print_code += "\n"
        print_code += f"\n --> Account total: {self.total_bill_amount()}$"
        return print_code

########################################################
class MultipleOrders:
    """
        Using FIFO to work with multiple orders
    """
    def __init__(self):
        self.list_orders = Queue()
        self.quantity_orders = 0

    def add_order(self, new_order:Order):
        if self.list_orders.full():
            print("No more orders can be received")
        self.list_orders.put(new_order)
        self.quantity_orders += 1

    def process_order(self):
        while not self.list_orders.empty():
            order_n = self.list_orders.get
            print(f"Order in process: \n{order_n}")
            print("order completed")
############################################################

class PayMent():
    def __int__(self):
        pass

    def pay(self, amount:float):
        raise NotImplementedError("Subclasses must implement pay()")

class Effective(PayMent):
    def __init__(self, amount_delivered):
        super().__init__()
        self.amount_delivered = amount_delivered

    def pay(self,amount:float):
        if(self.amount_delivered >= amount):
            self.amount_delivered = self.amount_delivered - amount
            print(f"Payment made in cash. Change: {self.amount_delivered}$")
        else:
            print(f"Insufficient funds. {amount - self.amount_delivered}$ is missing to complete the payment.")

    def add_amout_delivered(self, amount:float):
        self.amount_delivered += amount
        return self.amount_delivered

class Card(PayMent):
    def __init__(self, number:str, cvv:int):
        super().__init__()
        self.number = number
        self.cvv = cvv
    
    def pay(self, amount:float):
        print(f"Paying {amount}$ with card ************{self.number[-4:]}")