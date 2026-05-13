import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE customers SET email = ? WHERE id = ?",
    ("john_new@mail.com", 2)
)

print("Email updated successfully.")

conn.commit()
conn.close()