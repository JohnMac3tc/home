import os

from thinkful.bike.lib.bike_lib import csv_to_dict
from thinkful.bike.lib.bike_lib import Bicycle
from thinkful.bike.lib.bike_lib import Customer
from thinkful.bike.lib.bike_lib import BikeShop

def main():
    path = 'data'

    # TODO: this should be moved to a config.ini
    bike_csv = 'bicycles/bicycles.csv'
    customer_csv = 'customers/customers.csv'
    inv_csv = 'inventory/inventory.csv'

    # TODO: move to utils
    csv_data = lambda csv_name: csv_to_dict(csv_path=os.path.join(path, *csv_name.split('/')))

    bikes = [Bicycle(**v) for k, v in csv_data(bike_csv).iteritems()]
    customers = [Customer(**v) for k, v in csv_data(customer_csv).iteritems()]

    mikes_shop = BikeShop()
    mikes_shop.inventory = csv_data(inv_csv)

    # TODO: move to function "display_state"
    data = dict(customers=customers,
                bikes=bikes,
                inventory=mikes_shop.inventory
                )

    p_format = lambda s: '{:#<30}{}{:#>30}'.format('', s, '')

    for category, items in data.iteritems():
        print p_format(category) + '\n'
        for item in items:
            print item


if __name__ == '__main__':
    main()
