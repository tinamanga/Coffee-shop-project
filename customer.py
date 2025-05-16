
from order import Order
class Customer:
     all_customers = [] 
     def __init__(self, name):

        # setting the name when a customer is created
        self.set_name(name)
        Customer.all_customers.append(self)

     def set_name(self, name):

        # check name is a short string between 1 and 15 characters
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be 1-15 characters.")

     def get_name(self):
        return self._name

     name = property(get_name, set_name)

     def orders(self):

        # returning orders that belong to the customer
        return [order for order in Order.all_orders if order.customer == self]

     def coffees(self):
        # returning all coffees this customer ordered (no repeats)
        return list(set([order.coffee for order in self.orders()]))

     def create_order(self, coffee, price):
        # creating a new order for a coffee
        return Order(self, coffee, price)

     @classmethod
     def most_aficionado(cls, coffee):
        # Returning the customer who spent the most on the given coffee
        spending = {}

        for order in Order.all_orders:
            if order.coffee == coffee:
                if order.customer not in spending:
                    spending[order.customer] = 0
                spending[order.customer] += order.price

        if not spending:
            return None
        
        return max(spending, key=spending.get)