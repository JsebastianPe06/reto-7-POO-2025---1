from menu_system.menu_item import MenuItem, MainCourse, Dessert, Drink, Appetizer
from menu_system.order import MultipleOrders, Order, PayMent, Effective, Card 
from menu_system.menu import Menu, bruschetta, burger, couple_combo

#Colombian food
empanada = Appetizer("Empanada de Carne", 6, 3, "Small")
bandeja = MainCourse("Bandeja Paisa", 18, 1, False, True)
postre_leche = Dessert("Arroz con Leche", 5, 1, "Medium")
aguapanela = Drink("Aguapanela con Limón", 3, 1, "Traditional")
menu_co = [empanada, bandeja, aguapanela, postre_leche]

#Italian food
lasagna = MainCourse("Lasagna Bolognesa", 15, 1, False, False)
tiramisu = Dessert("Tiramisú", 6, 1, "individual")
vino = Drink("Vino", 9, 1, "vino tinto")
menu_it = [bruschetta, lasagna, tiramisu, vino]

if __name__ == "__main__":
    if 'colombian_menu' in globals():
        print("colombian_menu already exists")
    else:
        colombian_menu = Menu("colombian_food")
        print("Menu colombian_food created")
    if 'italian_menu' in globals():
        print("italian_menu already exists")
    else:
        italian_menu = Menu("italian_food")
        print("Menu italian_food created")

    for i in menu_co: 
        colombian_menu.add_item(i)

    for i in menu_it:
        italian_menu.add_item(i)

    print(colombian_menu)
    print(italian_menu)

    colombian_menu.add_item(burger)
    print(colombian_menu)

    orden1 = couple_combo(
        vino, aguapanela, empanada, lasagna, bandeja, postre_leche
        )

    print(orden1.maincourse2)