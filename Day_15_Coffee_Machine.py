# Coffee Machine Project

""" Here, I have created a coffee machine that allows users to choose
from 3 different types of coffees, generate reports and turns off.
I initially coded this program on my own but upon watching Dr. Yu's Udemy video,
I realized some inefficiencies and changed my code to reflect my learnings."""


from coffee_data import MENU, resources


def is_resource_sufficient(order_ingredients):
    """Return True when there are enough resources to complete an order."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def user_coins_value():
    """Return the total calculated from the coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How may pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink):
    """Returns True when payment is accepted or else it is false."""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        global sale
        sale += cost_of_drink
        return True
    else:
        print("\tSorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕️! Enjoy!")


transaction_end = False
sale = 0

while not transaction_end:
    user_selection = input("\tWhat would you like?(espresso/latte/cappuccino) ").lower()
    if user_selection == "off":
        transaction_end = True
    elif user_selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${sale}")
    else:
        drink_name = user_selection
        drink_details = MENU[user_selection]
        if not is_resource_sufficient(MENU[user_selection]["ingredients"]):
            transaction_end = True
        else:
            drink_cost = float(MENU[user_selection]["cost"])
            print(f"\tCost of the drink is ${drink_cost}.")
            payment = user_coins_value()
            print(f"I have received ${payment}.")
            if is_transaction_successful(payment, drink_cost):
                make_coffee(user_selection, drink_details["ingredients"])
