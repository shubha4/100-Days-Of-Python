# Coffee Machine Project in OOP

""" Here, I have created a coffee machine using OOP that allows users to choose
from 3 different types of coffees, generate reports and turns off."""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

transaction_end = False

while not transaction_end:
    user_selection = input(f"\tWhat would you like?({menu.get_items()}) ").lower()
    if user_selection == "off":
        transaction_end = True
    elif user_selection == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_selection)
        if coffee_machine.is_resource_sufficient(drink):
            transaction_end = True
        else:
            print(f"\tCost of the drink is ${drink.cost}.")
            money_machine.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)