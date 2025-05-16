
class Coffee:
    def __init__(self, name):
        # Set the name when creating a coffee
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name must be a string with at least 3 characters
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters")

    def orders(self):
        # Return all orders for this coffee
        from order import Order  # Local import to avoid circular import
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        # Return unique customers who ordered this coffee
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        # Total number of orders for this coffee
        return len(self.orders())

    def get_average_price(self):
        # Return average price of this coffee
        orders = self.orders()
        if not orders:
            return 0  # No orders yet
        total = sum(order.price for order in orders)
        return total / len(orders)
