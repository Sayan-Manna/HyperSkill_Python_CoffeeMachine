def summary():
    print(f"The coffee machine has:\n{water} of water\n{milk} of milk\n{beans} of coffee beans\n{cups} of disposable cups\n{money} of money")


water = int(400)
milk = int(540)
beans = int(120)
cups = int(9)
money = int(550)

summary()
print()
action = input("Write action (buy, fill, take):\n")
if action == "buy":
    coffee_type = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n'))
    if coffee_type == 1:
        water -= 250
        beans -= 16
        cups = cups - 1
        money += 4

    elif coffee_type == 2:
        water -= 350
        milk -= 75
        beans -= 20
        cups = cups - 1
        money += 7

    elif coffee_type == 3:
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6

elif action == "fill":
    added_water = int(input("Write how many ml of water do you want to add:\n"))
    added_milk = int(input("Write how many ml of milk do you want to add:\n"))
    added_beans = int(input("Write how many grams of coffee do you want to add:\n"))
    cups_of_coffee = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water += added_water
    milk += added_milk
    beans += added_beans
    cups += cups_of_coffee

elif action == "take":
    print("I gave you ${}".format(money))
    money = 0
    print()
summary()
