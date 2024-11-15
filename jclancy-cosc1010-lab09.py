class Pizza:
    def __init__(self, size, sauce="marinara"):
        """
        Initialize a new pizza with a given size and sauce.
        Default sauce is marinara if not specified.
        """
        self.setSize(size)
        self.sauce = sauce
        self.toppings = ["cheese"]  # Default topping is cheese

    def setSize(self, size):
        if size >= 10:
            self.size = size
        else:
            self.size = 10  # Default to 10" if size is smaller than 10 inches

    def getSize(self):
        return self.size

    def getSauce(self):
        return self.sauce

    def getToppings(self):
        return self.toppings

    def addToppings(self, *toppings): #needs asterisk since outout is type list
        for topping in toppings:
            self.toppings.append(topping)   #appending to topping attribute of Pizza

    def getAmountOfToppings(self):
        return len(self.toppings)


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
            pizza.addToppings(*toppings)  # Add toppings to the pizza

        
        self.orders.append(pizza)   # Store the pizza object in the orders list
        self.order_count += 1

        return pizza

    def getPrice(self, pizza):
        return (pizza.getSize() * self.price_per_inch) + (pizza.getAmountOfToppings() * self.price_per_topping)

    def getReceipt(self, pizza):
        print("*" * 78)
        print(f"Receipt for Order #{self.order_count}")
        print(f"Size: {pizza.getSize()} inches")
        print(f"Sauce: {pizza.getSauce()}")
        print("Toppings:")
        for topping in pizza.getToppings():
            print(f"  - {topping}")
        print("*" * 78)

        pizza_price = self.getPrice(pizza)
        print(f"Base Price: ${pizza.getSize() * self.price_per_inch:.2f}")
        print(f"Toppings Price: ${pizza.getAmountOfToppings() * self.price_per_topping:.2f}")
        print(f"Total: ${pizza_price:.2f}")
        print("*" * 78)

    def getNumberOfOrders(self):
        return self.order_count


def main():
    pizzeria = Pizzeria() #create object

    while True:
        user_input = input("Would you like to place an order? (yes to continue, exit to quit): ").lower()

        if user_input == "exit":
            break
        elif user_input == "yes":
            pizza = pizzeria.placeOrder()  # Place a new order/create object
            pizzeria.getReceipt(pizza)     # Show the receipt
        else:
            print("Invalid input, please type 'yes' or 'exit'.")

    print(f"Total orders placed: {pizzeria.getNumberOfOrders()}")

if __name__ == "__main__":
    main()
