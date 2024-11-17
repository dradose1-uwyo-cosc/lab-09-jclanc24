# John Clancy
# UWYO COSC 1010
# Submission Date: 11/17/2024
# Lab 09
# Lab Section: 13
# Sources, people worked with, help given to:
# See Readme
# Light debugging use of chat gpt: example queries were trouble shooting why certain lines of codes were not executing and explaining attribute errors

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza:


    def __init__(self, size, sauce="marinara"):
        
        self.setSize(size)
        self.sauce = sauce
        self.toppings = ["cheese"]  # Default is cheese

    def setSize(self, size):
        if size >= 10:
            self.size = size
        else:
            self.size = 10  # Default to 10"

    def getSize(self):
        return self.size

    def getSauce(self):
        return self.sauce

    def getToppings(self):
        return self.toppings

    def addToppings(self, toppings): #needs asterisk since outout is type list
        for topping in toppings:
            self.toppings.append(topping)   #appending to topping attribute of Pizza

    def getAmountOfToppings(self):
        return len(self.toppings)

# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


class Pizzeria:
    
    def __init__(self):
        # Instance-level variables
        self.price_per_topping = 0.30
        self.price_per_inch = 0.60
        self.order_count = 0  # Instance-level order counter
        self.orders = []  # List of all orders placed

    def placeOrder(self):

        size = int(input("Enter pizza size: "))
        sauce = input("Enter sauce (leave blank for marinara): ").strip()
        if "" == sauce:
            sauce = "marinara"

        pizza = Pizza(size, sauce) #create object

        toppings_input = input("Enter toppings (separate by commas, leave blank when done): ").strip()
        if toppings_input:
            toppings = toppings_input.split(",")
            pizza.addToppings(toppings) 

        
        self.orders.append(pizza) 
        self.order_count += 1

        return pizza

    def getPrice(self, pizza):
        return (pizza.getSize() * self.price_per_inch) + (pizza.getAmountOfToppings() * self.price_per_topping)

    def getReceipt(self, pizza):
        pizza_price = self.getPrice(pizza)
        print("*" * 78)
        print(f"\t\t\tReceipt for Order #{self.order_count}")
        print("*" * 78)
        print(f"{pizza.getSize()}' Pizza" + f"\t\t\t\t\t\t\t${pizza.getSize() * self.price_per_inch:.2f}")
        print(f"{pizza.getSauce().title()} Sauce Base")
        print(f"Toppings:\t\t\t\t\t\t\t${pizza.getAmountOfToppings() * self.price_per_topping:.2f}")
        for topping in pizza.getToppings():
            print(f"\t{topping.title()}")
        print("*" * 78)
        print(f"Total:\t\t\t\t\t\t\t\t${pizza_price:.2f}")
        print("*" * 78)

    def getNumberOfOrders(self):
        return self.order_count








#PROGRAM START




# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.





pizzeria = Pizzeria()

while True:
    user_input = input("Would you like to place an order? (yes to continue, exit to quit): ").lower()

    if user_input == "exit":
        break
    elif user_input == "yes":
        pizza = pizzeria.placeOrder()
    else:
        print("Invalid input, please type 'yes' or 'exit'.")

print(f"Orders Placed: {pizzeria.getNumberOfOrders()}")

