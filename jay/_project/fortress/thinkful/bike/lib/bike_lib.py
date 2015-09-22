import csv

# -------------- data structures ------------- #

class BikeShop(object):
    def __init__(self):
        self.inventory = {}

    def display_inventory(self):
        print self

    def __repr__(self):
        return str(self.inventory)


class Customer(object):
    __slots__ = ['own', 'money', 'name']

    def __init__(self, name, money, own):
        self.own = own
        self.money = money
        self.name = name

    def __repr__(self):
        return 'Customer({})'.format(self.name)

    def __str__(self):
        return self.__repr__()


class Bicycle(object):
    __slots__ = ['model', 'weight', 'cost']

    def __init__(self, model, weight, cost):
        self.cost = cost
        self.weight = weight
        self.model = model

    def __repr__(self):
        return 'Bicycle({})'.format(self.model)

    def __str__(self):
        return self.__repr__()


# -------------- helper functions ---------------#

def csv_to_dict(csv_path, d=None):
    if d is None:
        d = {}
    with open(csv_path) as f:
        reader = csv.reader(f)
        header = reader.next()
        for line in reader:
            d[line[0].strip()] = {header[i].strip(): line[i].strip() for i in range(len(line))}
    return d
