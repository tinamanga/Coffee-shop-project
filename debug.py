
from customer import Customer
from coffee import Coffee

# Make some customers
c1 = Customer("Alex")
c2 = Customer("Sara")

# Make some coffees
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

# Customers create orders
o1 = c1.create_order(latte, 4.5)
o2 = c1.create_order(cappuccino, 3.0)
o3 = c2.create_order(latte, 5.0)
o4 = c2.create_order(latte, 5.5)

# Show what each customer ordered
print("Alex ordered:")
for coffee in c1.coffees():
    print(coffee.name)

print("Sara ordered:")
for coffee in c2.coffees():
    print(coffee.name)

# Show average price of latte
print("Average price of Latte:", latte.get_average_price())

# Find who spent the most on Latte
top = Customer.biggest_spender(latte)
print("Top Latte spender:", top.name)