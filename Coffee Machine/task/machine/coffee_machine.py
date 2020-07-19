class Coffee:

    def __init__(self, water, milk, coffee, money, cups=1):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

espresso = Coffee(250, 0, 16, 4)
late = Coffee(350, 75, 20, 7)
cappuccino = Coffee(200, 100, 12, 6)

class CoffeeMachine:

    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.action()

    def make_coffee(self, coffee):
            if self.water < coffee.water:
                    print("Sorry, not enough water!")
            elif self.coffee < coffee.coffee:
                    print("Sorry, not enough coffee!")
            elif self.milk < coffee.milk:
                print("Sorry, not enough milk!")
            elif self.cups < coffee.cups:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= coffee.water
                self.milk -= coffee.milk
                self.coffee -= coffee.coffee
                self.cups -= 1
                self.money += coffee.money

    def buy(self):
        number = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if number == "1":
            self.make_coffee(espresso)
        elif number == "2":
            self.make_coffee(late)
        elif number == "3":
            self.make_coffee(cappuccino)
        elif number == "back":
           pass

    def fill(self):
            self.water += int(input("Write how many ml of water do you want to add:"))
            self.milk += int(input("Write how many ml of milk do you want to add:"))
            self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
            self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
            print("I gave you ${}".format(self.money))
            self.money -= self.money

    def remaining(self):
            print(
                "The coffee machine has:\n{water} of water\n{milk} of milk\n{coffee} of coffee beans\n{cups} of disposable cups\n${money} of money".
                format(water=self.water, milk=self.milk, coffee=self.coffee, cups=self.cups, money=self.money))

    def action(self):
        while True:
            option = str(input("Write action (buy, fill, take, remaining, exit):"))
            if option == "buy":
                self.buy()
            elif option == "fill":
                self.fill()
            elif option == "take":
                self.take()
            elif option == "remaining":
                self.remaining()
            elif option == "exit":
                break

machine = CoffeeMachine()