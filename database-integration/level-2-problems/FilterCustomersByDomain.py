import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT name, email FROM customers WHERE email LIKE ?",
    ("%mail.com",)
)

records = cursor.fetchall()

for name, email in records:
    print(f"{name} - {email}")

conn.close()