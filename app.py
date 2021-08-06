from enum import Enum
import random
import time

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3

class Food:
    def __init__(self, name, description, price, size: Size, discount):
        self._name = name
        self._description = description
        self._price = price
        self._size = size
        self._discount = discount

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setDecription(self, description):
        self._description = description

    def getDescription(self):
        return self._description

    def setPrice(self, price):
        self._price = price

    def getPrice(self):
        return self._price

    def setSize(self, size):
        self._size = size

    def getSize(self):
        return self._size.name

class Burger(Food):
    def __init__(self, name, description, price, size: Size, discount):
        super().__init__(name, description, price, size, discount)

    def getPrice(self):
        if self._discount :
            return round(self._price - (self._price / 10), 2)
        return self._price

class Drink(Food):
    def __init__(self, name, description, price, size: Size, discount):
        super().__init__(name, description, price, size, discount)

    def getPrice(self):
        if self._discount:
            return round(self._price - (self._price / 8), 2)
        return self._price

class Side(Food):
    def __init__(self, name, description, price, size: Size, discount):
        super().__init__(name, description, price, size, discount)
    
    def getPrice(self):
        if self._discount:
            return round(self._price - (self._price / 5), 2)
        return self._price

class Order:
    def __init__(self, burger: Burger, drink: Drink, side: Side):
        self._burger = burger
        self._drink = drink
        self._side = side

    def totalPrice(self):
        total = self._burger.getPrice() + self._drink.getPrice() + self._side.getPrice()
        return total

    def getTableNumber(self):
        return random.randint(1, 50)

    def getOrder(self):
        print(f"{self._burger.getName()}|{self._burger.getSize()} - €{self._burger.getPrice()}")
        print(f"{self._drink.getName()}|{self._drink.getSize()} - €{self._drink.getPrice()}")
        print(f"{self._side.getName()}|{self._side.getSize()} - €{self._side.getPrice()}")
        print(f"Total: {self.totalPrice()}")

burgers = [] 
burgers.append(Burger("Beef Burger", "", 5.9, Size.MEDIUM, True))
burgers.append(Burger("Beef Burger", "", 7.9, Size.BIG, True))
burgers.append(Burger("Chicken Burger", "", 3.9, Size.MEDIUM, True))
burgers.append(Burger("Chicken Burger", "", 6.9, Size.BIG, False))
burgers.append(Burger("Veggie Burger", "", 8.9, Size.SMALL, False))

drinks = [] 
drinks.append(Drink("Coca", "", 2.5, Size.SMALL, False))
drinks.append(Drink("Coca", "", 3.5, Size.MEDIUM, False))
drinks.append(Drink("7up", "", 2.0, Size.SMALL, False))
drinks.append(Drink("7up", "", 2.5, Size.MEDIUM, True))
drinks.append(Drink("Orange Juice", "", 2.5, Size.MEDIUM, True))

sides = []
sides.append(Side("Fries", "", 3.9, Size.SMALL, False))
sides.append(Side("Fries", "", 4.9, Size.MEDIUM, False))
sides.append(Side("Fries", "", 5.9, Size.BIG, True))
sides.append(Side("Salad", "", 2.9, Size.MEDIUM, False))
sides.append(Side("Salad", "", 3.9, Size.BIG, False))


print("Welcome to the Prototype Kiosk System!")

print("First, choose: (1)'Eat in' or (2)'Take out'.")
string = int(input())

print("Select your burger: ")
for i, burger in enumerate(burgers, start=0):
    print(f"({i+1}){burger.getName()}:{burger.getSize()} - €{burger.getPrice()}")
burgerChosen = int(input())

print("Select your drink: ")
for i, drink in enumerate(drinks, start=0):
    print(f"({i+1}){drink.getName()}:{drink.getSize()} - €{drink.getPrice()}")
drinkChosen = int(input())

print("Select your side: ")
for i, side in enumerate(sides, start=0):
    print(f"({i+1}){side.getName()}:{side.getSize()} - €{side.getPrice()}")
sideChosen = int(input())

order = Order(burgers[burgerChosen - 1], drinks[drinkChosen - 1], sides[sideChosen - 1])

print("Here is your order: ")
order.getOrder()

print("Do you want to cancel your order? (1)yes | (2)no")
cancel = int(input())

if cancel == 1:
    print("Bye... thank you!")
    exit()

print("Checkout...")

print("Select payment method: (1)debit card | (2)credit card | (3)cash")
payment = int(input())
print("Processing...")
time.sleep(3)
print("Done!")
print("Printing your receipt...")
time.sleep(5)

table = order.getTableNumber()
print(f"This is your table number: {table}")

print("Thanks for choosing us!")

exit()