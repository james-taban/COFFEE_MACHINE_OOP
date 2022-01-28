from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money = MoneyMachine()

coffee_maker = CoffeeMaker()
make_order = True

while make_order:
    choice = input(f"What coffee would you like to drink today? {menu.get_items()}: ")
    if choice == "report":
        coffee_maker.report()
        money.report()
    elif choice == "off":
        make_order = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


