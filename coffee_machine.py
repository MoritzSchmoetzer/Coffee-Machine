class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.selection = None
        self.action_input = None

    def __str__(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee_beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        print()

    def action(self, ui):
        # ui = user_input
        print(f"\nWrite action (buy, fill, take, remaining, exit):")
        if ui == "buy":
            self.buy()
        elif ui == "fill":
            self.fill()
        elif ui == "take":
            self.take()
        elif ui == "remaining":
            self.__str__()
        elif ui == "exit":
            pass

    def resources(self, minus_water, minus_milk, minus_coffee_beans, add_money):
        # r_... = remaining_...
        r_water = self.water - minus_water
        r_milk = self.milk - minus_milk
        r_coffee_beans = self.coffee_beans - minus_coffee_beans
        r_cups = self.cups - 1

        if r_cups == 0:
            print("Sorry, not enough disposable cups")
        elif self.water >= r_water >= r_cups and self.milk >= r_milk >= r_cups and self.coffee_beans >= r_coffee_beans >= r_cups:
            self.water -= minus_water
            self.milk -= minus_milk
            self.coffee_beans -= minus_coffee_beans
            self.money += add_money
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
        else:
            if r_water <= self.water:
                print("Sorry, not enough water!")
            elif r_milk <= self.milk:
                print("Sorry, not enough milk")
            elif r_coffee_beans <= self.coffee_beans:
                print("Sorry, not enough coffee beans")

    def buy(self):
        selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if selection == "1":  # espresso
            self.resources(250, 0, 16, 4)
        elif selection == "2":  # latte
            self.resources(350, 75, 20, 7)
        elif selection == "3":  # cappuccino
            self.resources(200, 100, 12, 6)
        elif selection == "back":
            pass
        print()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        self.money -= self.money
        print(f"I gave you ${self.money}\n")


coffee_machine = CoffeeMachine()
user_input = ""

while user_input != "exit":
    coffee_machine.action(user_input)
    user_input = input()
