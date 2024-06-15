from menu import MENU, resources
import random

# Define global variables
money_recieved = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def report():
    global money_recieved
    # Access the current state of resources
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return money_recieved, water, milk, coffee

def sum(quarters, dimes, nickles, pennies):
    # Define the value of each coin
    quarters_value = 0.25
    dimes_value = 0.10
    nickles_value = 0.05
    pennies_value = 0.01
    # Calculate the total amount of money
    total_money = (quarters_value * quarters) + (dimes_value * dimes) + (nickles_value * nickles) + (pennies_value * pennies)
    return total_money

def coffee_machine():
    global money_recieved
    while True:
        # Prompt user for their choice
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            print("Machine turning off...")
            break  # Exit the loop to turn off the machine
        elif user_choice == "report":
            # Generate and print the report
            money_recieved, water, milk, coffee = report()
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money_recieved}")
        elif user_choice not in ["espresso", "latte", "cappuccino"]:
            print("Invalid choice, please try again.")
        else:
            print(f"You chose: {user_choice}")

            # Get the required ingredients and cost for the chosen drink
            drink = MENU[user_choice]
            water_needed = drink["ingredients"]["water"]
            milk_needed = drink["ingredients"].get("milk", 0)  # Some drinks might not need milk
            coffee_needed = drink["ingredients"]["coffee"]
            cost = drink["cost"]

            # Check if there are enough resources
            if resources["water"] < water_needed:
                print("Sorry there is not enough water.")
                continue  # Skip the rest of the loop and prompt again
            if resources["milk"] < milk_needed:
                print("Sorry there is not enough milk.")
                continue
            if resources["coffee"] < coffee_needed:
                print("Sorry there is not enough coffee.")
                continue

            # Process the coin input from the user
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_money = sum(quarters, dimes, nickles, pennies)

            if total_money < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(total_money - cost, 2)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                money_recieved += cost
                # Deduct the used resources
                resources["water"] -= water_needed
                resources["milk"] -= milk_needed
                resources["coffee"] -= coffee_needed
                print(f"Here is your {user_choice}. Enjoy!")

coffee_machine()



