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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(drink):
    """Check resources sufficient"""
    drink_ingredients = drink["ingredients"]
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def process_coins_total():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def save_money(s_m):
    global money
    money += s_m


def check_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        save_money(drink_cost)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        False


def make_coffee(drink_name):
    """Deduct the required ingredients from the resources."""
    drink_ingredients = MENU[drink_name]["ingredients"]
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕ . Enjoy!")


def print_report():
    """shows the current resource"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        if is_resources_sufficient(MENU[choice]):
            coins_total = process_coins_total()
            if check_transaction_successful(coins_total, MENU[choice]["cost"]):
                make_coffee(choice)



