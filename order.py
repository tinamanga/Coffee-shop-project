class order:
      all_orders = []  # list of all orders

def __init__(self, customer, coffee, price):
        self.set_customer(customer)
        self.set_coffee(coffee)
        self.set_price(price)
        Order.all_orders.append(self)