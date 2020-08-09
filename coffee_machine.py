water, milk, coffee_beans, cups, money = 400, 540, 120, 9, 550


def information():
    global water, milk, coffee_beans, cups, money
    print("The coffee machine has: ")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee_beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")
    print()


def resources(minus_water, minus_milk, minus_coffee_beans, add_money):
    global water, milk, coffee_beans, cups, money
    # r_... = remaining_...
    r_water = water - minus_water
    r_milk = milk - minus_milk
    r_coffee_beans = coffee_beans - minus_coffee_beans
    r_cups = cups - 1

    if r_cups == 0:
        print("Sorry, not enough disposable cups")
    elif water >= r_water >= r_cups and milk >= r_milk >= r_cups and coffee_beans >= r_coffee_beans >= r_cups:
        print("I have enough resources, making you a coffee!")
        water -= minus_water
        milk -= minus_milk
        coffee_beans -= minus_coffee_beans
        money += add_money
        cups -= 1
    else:
        if r_water <= water:
            print("Sorry, not enough water!")
        elif r_milk <= milk:
            print("Sorry, not enough milk")
        elif r_coffee_beans <= coffee_beans:
            print("Sorry, not enough coffee beans")


def buy():
    selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    global water, milk, coffee_beans, cups, money
    if selection == "1":  # espresso
        resources(250, 0, 16, 4)
    elif selection == "2":  # latte
        resources(350, 75, 20, 7)
    elif selection == "3":  # cappuccino
        resources(200, 100, 12, 6)
    elif selection == "back":
        pass
    print()


def fill():
    global water, milk, coffee_beans, cups
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))


def take():
    global money
    print(f"I gave you ${money}")
    print()
    money -= money


def action():
    while True:
        action_input = input("Write action (buy, fill, take, remaining, exit):\n")
        print()
        if action_input == "buy":
            buy()
        elif action_input == "fill":
            fill()
        elif action_input == "take":
            take()
        elif action_input == "remaining":
            information()
        elif action_input == "exit":
            break


def coffee_machine():
    action()


coffee_machine()
