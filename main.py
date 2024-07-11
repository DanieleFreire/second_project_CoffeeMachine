MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
profit = 0


def is_resources(drink_chosen, standard_resource):
    """Take the drink chosen and the resource and calculate the difference between them"""
    for item in drink_chosen['ingredients']:
        if standard_resource[item] >= drink_chosen['ingredients'][item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False


def process_coins():
    """Calculate the monetary value of the coins inserted"""
    print("Please, insert the coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction(name_drink, money):
    """Take the drink chosen cost and the coins inserted and return True if there is money"""
    if money >= MENU[name_drink]['cost']:
        change = round(money - MENU[name_drink]['cost'], 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += MENU[user_choice]['cost']
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredients, drink_name):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if is_resources(MENU[user_choice], resources):
            coins_inserted = process_coins()
            if is_transaction(user_choice, coins_inserted):
                make_coffee(MENU[user_choice]['ingredients'], user_choice)

