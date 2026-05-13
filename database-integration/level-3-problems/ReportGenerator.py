import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

orders = [
    (2001, 1),
    (2002, 1),
    (2003, 1),
    (2004, 2),
    (2005, 2)
]

cursor.executemany(
    "INSERT INTO orders (order_id, customer_id) VALUES (?, ?)",
    orders
)

cursor.execute("""
SELECT customers.name, COUNT(orders.order_id) AS total_orders
FROM customers
JOIN orders
ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY total_orders DESC
LIMIT 3
""")

records = cursor.fetchall()

print("Top 3 Customers:")

for i, (name, total) in enumerate(records, start=1):
    print(f"{i}. {name} - {total} Orders")

conn.commit()
conn.close()