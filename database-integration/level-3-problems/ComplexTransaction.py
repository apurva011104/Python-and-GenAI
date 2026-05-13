import sqlite3

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

try:
    cursor.execute(
        "INSERT INTO customers (name, email) VALUES (?, ?)",
        ("Sam", "sam@mail.com")
    )

    cursor.execute(
        "DELETE FROM customers WHERE name = ?",
        ("Alex",)
    )

    cursor.execute("INSERT INTO unknown_table VALUES (1)")

    conn.commit()
    print("Transaction completed successfully.")

except Exception as e:
    conn.rollback()
    print("Transaction rolled back due to error.")
    print("Error:", e)

finally:
    conn.close()