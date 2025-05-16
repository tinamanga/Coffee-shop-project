# Coffee-shop-project

## Description
This is a simple object-oriented Python application that models a coffee shop system. It includes three main classes: Customer, Coffee, and Order. The program allows customers to place coffee orders and tracks those orders. It also includes features like:

Listing customer orders

Listing unique coffees ordered

Calculating average coffee prices

Identifying the top-spending customer for a specific coffee

🧠 Domain Model
Classes and Relationships:
Customer

Has many Orders

Has many Coffees (through Orders)

Coffee

Has many Orders

Has many Customers (through Orders)

Order

Belongs to one Customer

Belongs to one Coffee

This creates a many-to-many relationship between Customers and Coffees through Orders.

🛠️ Technologies Used
Python 3

pipenv (for virtual environment)

Optional: pytest (for unit testing)

📁 Project Structure
bash
Copy
Edit
coffee_shop_project/
│
├── customer.py        # Defines the Customer class
├── coffee.py          # Defines the Coffee class
├── order.py           # Defines the Order class
├── debug.py           # Test script to manually check functionality
├── Pipfile            # pipenv environment file
├── Pipfile.lock       # pipenv lock file
└── README.md          # Project documentation (this file)
✅ Features Implemented
✔️ Customer Class
Validates name (1–15 characters)

.orders() → All orders by the customer

.coffees() → Unique list of coffees the customer ordered

.create_order(coffee, price) → Places an order

@classmethod most_aficionado(coffee) → Returns the customer who spent the most on a coffee

✔️ Coffee Class
Validates name (at least 3 characters)

.orders() → All orders for this coffee

.customers() → Unique list of customers who ordered it

.num_orders() → Number of times coffee was ordered

.get_average_price() → Average price for this coffee

✔️ Order Class
Validates:

customer is a Customer instance

coffee is a Coffee instance

price is a float between 1.0 and 10.0

▶️ How to Run the Project
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/coffee_shop_project.git
cd coffee_shop_project
Set up your environment:

bash
Copy
Edit
pipenv install
pipenv shell
Run the debug script:

bash
Copy
Edit
python3 debug.py
You should see output showing customer orders, average coffee prices, and the top coffee spender.

🧪 Optional: Run Tests (Bonus)
If you have a tests/ folder with pytest tests:

bash
Copy
Edit
pipenv install pytest
pytest
🚫 Input Validation & Errors
The app includes basic validation:

Customer names must be 1–15 characters long.

Coffee names must be at least 3 characters.

Prices must be float values between 1.0 and 10.0.

Appropriate ValueError is raised on invalid inputs.

🙋‍♀️ Author
Tina Manga
GitHub Profile

