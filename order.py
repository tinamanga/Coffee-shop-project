class order:
      all_orders = []  # list of all orders

def __init__(self, customer, coffee, price):
        self.set_customer(customer)
        self.set_coffee(coffee)
        self.set_price(price)
        Order.all_orders.append(self)

        def set_customer(self, customer):
         from customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("customer must be a Customer")

        def get_customer(self):
         return self._customer

        customer = property(get_customer, set_customer)

        def set_coffee(self, coffee):
         from coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("coffee must be a Coffee")

        def get_coffee(self):
         return self._coffee

        coffee = property(get_coffee, set_coffee)

        def set_price(self, price):
        # check price is between 1.0 and 10.0
         if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
         else:
            raise Exception("Price must be float between 1.0 and 10.0")

        def get_price(self):
          return self._price

        price = property(get_price, set_price)