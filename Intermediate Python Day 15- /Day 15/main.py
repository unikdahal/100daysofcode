resources = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0,
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def checkresources(water, milk, coffee):
    if resources['Water'] - water >= 0 and resources['Milk'] - milk >= 0 and resources['Coffee'] - coffee >= 0:
        return True
    elif resources['Water'] - water < 0:
        print("Sorry there is not enough Water")
    elif resources['Milk'] - milk < 0:
        print("Sorry there is not enough Milk")
    else:
        print("Sorry there is not enough coffee")
    return False


def money(drink):
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total < MENU[drink]['cost']:
        print("Sorry that's not enough money refunded")
        return 1
    elif total > MENU[drink]['cost']:
        print(f"Here is ${total - MENU[drink]['cost']} dollars in change \n")


def updateResource(drink):
    resources['Water'] -= MENU[drink]['ingredients']['water']
    resources['Milk'] -= MENU[drink]['ingredients']['milk']
    resources['Coffee'] -= MENU[drink]['ingredients']['coffee']
    resources['Money'] += MENU[drink]['cost']
    return 0


while True:
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()

    if drink == "off":
        break
    elif drink == "report":
        print(resources)
        continue

    resources1= checkresources(MENU[drink]['ingredients']['water'], MENU[drink]['ingredients']['milk'],
                               MENU[drink]['ingredients']['coffee'])
    if resources1:
        print("Please Insert Coins \n")
        sufficient = money(drink)
        if sufficient == 1:
            continue
        updateResource(drink)
        print(f"Here is your {drink}. Enjoy!")
