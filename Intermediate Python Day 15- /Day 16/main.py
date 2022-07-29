from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

while True:
    choice = input("What would you like?( "+ menu.get_items()+")").lower()
    if choice == "off":
        break
    elif choice== "report":
        coffee_maker.report()
        money_machine.report()
        continue
    drink=menu.find_drink(choice)
    resources1=coffee_maker.is_resource_sufficient(drink)
    if resources1:
        sufficient = money_machine.make_payment(drink.cost)
        if sufficient == False:
            continue
        coffee_maker.make_coffee(drink)
