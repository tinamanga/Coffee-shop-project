from customer import Customer
from coffee import Coffee

# Making some customers
c1 = Customer("Alex")
c2 = Customer("Sara")

# Making some coffees
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

# Customers creating orders
c1.create_order(latte, 4.5)
c1.create_order(cappuccino, 3.0)
c2.create_order(latte, 5.0)
c2.create_order(latte, 5.5)

# Showing what each customer ordered
print("Alex ordered:")
for coffee in c1.coffees():
    print(coffee.name)

print("Sara ordered:")
for coffee in c2.coffees():
    print(coffee.name)

# Showing average price of latte
print("Average price of Latte:", latte.get_average_price())

# Finding who spent the most on Latte
top = Customer.most_aficionado(latte)
if top:
    print("Top Latte spender:", top.name)
else:
    print("No orders for Latte.")
