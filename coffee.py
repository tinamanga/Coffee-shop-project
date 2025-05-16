
from order import Order
class cofee:
    all_coffees = []  # list of all coffees

    def __init__(self, name):
        self.set_name(name)
        Coffee.all_coffees.append(self)

    def set_name(self, name):

        # name must be at least 3 characters
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Name must be at least 3 characters.")

    def get_name(self):
        return self._name

    name = property(get_name, set_name)

    def orders(self):
        # return orders for this coffee
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        # return all customers who ordered this coffee
        return list(set([order.customer for order in self.orders()]))

    def total_orders(self):
        # count how many orders for this coffee
        return len(self.orders())

    def get_average_price(self):
        prices = [order.price for order in self.orders()]
        if prices:
            return sum(prices) / len(prices)
        else:
            return 0