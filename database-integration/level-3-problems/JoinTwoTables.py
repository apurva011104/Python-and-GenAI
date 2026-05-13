import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER
)
""")

orders = [
    (1001, 1),
    (1002, 2)
]

cursor.executemany(
    "INSERT OR IGNORE INTO orders (order_id, customer_id) VALUES (?, ?)",
    orders
)

cursor.execute("""
SELECT customers.name, orders.order_id
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id
""")

records = cursor.fetchall()

for name, order_id in records:
    print(f"{name} - OrderID: {order_id}")

conn.commit()
conn.close()