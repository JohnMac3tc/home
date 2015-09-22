__author__ = 'jay'



class Bicycle(object):

    # TODO: CR: PEP-8 compliance change modelName to model_name
    def __init__(self, modelName, weight, cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost

# TODO: CR: PEP-8 compliance: make CamelCase
class Bike_Shop(object):
    def __init__(self, name):
        self.name = name
        self.inventory = []

    # TODO: CR: PEP-8; change to add_bike
    def addBike(self, bike):
        self.inventory.append(bike)

    # TODO: CR: PEP-8; change to display_inventory
    def displayInventory(self):
        print self.inventory

# TODO: CR: All Python classes are written in CamelCase (unless their code is in C like list, int, dict, etc.)
# So change this to Customer
class customer(object):
    def __init__(self, money, own):
        self.money = money
        self.own = own

# TODO: CR: somehow all of these quotation marks are Unicode -- they need to be ascii parenthesis
# or Python cannot parse them.  Maybe an email thing -- try to send as file attachments!
redRunner = Bicycle(“red runner”, 20, 100)
blueDemon = Bicycle(“blue demon”, 30, 200)
greenhornet = Bicycle(“green hornet”, 20, 300)
purpledot = Bicycle(“purple dot”, 30, 400)
yellowjacket = Bicycle(“yellow jacket”, 20, 500)
blackstreak = Bicycle(“black streak”, 30, 800)

# TODO: CR: same comment about the quotation marks
mikeShop = Bike_Shop(“Mikes Shop”)
mikeShop.displayInventory()
mikeShop.addBike(redRunner)
mikeShop.addBike(blueDemon)
mikeShop.displayInventory()

# TODO: CR: let's talk about objects when you get a chance -- all the mystery will be revealed!
# in the meantime, axe the first argument OR add an additional parameter to the customer class
# called "name" and then add "self.name" below.
Joe = customer("Joe", 200, True)
Frank = customer("Frank", 500, True)
Tina = customer("Tina", 1000, True)