class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        
        # Local imports to avoid circular import issues
        from customer import Customer
        from coffee import Coffee

        # Validating that the customer is a Customer instance
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        
        # Validate that the coffee is a Coffee instance
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        
        # Validating price range
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")

        # Assigning to instance variables
        self._customer = customer
        self._coffee = coffee
        self._price = price

        # Keeping track of all orders
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
