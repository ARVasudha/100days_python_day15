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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins():
    print("please insert coins")
    total = int(input("How many quaters?:"))*0.25
    total += int(input("How many dimes?:"))*0.1
    total += int(input("How many nickles?:"))*0.05
    total += int(input("How many pennies?:"))*0.01
    return total


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += money_received
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return  False


def is_resource_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off" or choice == "OFF" or choice == "Off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:${round(profit,2)}")

    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
