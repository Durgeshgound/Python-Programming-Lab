#Demonstrate transaction control (commit and rollback) in database operations.

import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

# Create table
cur.execute("CREATE TABLE IF NOT EXISTS accounts(id INTEGER, balance INTEGER)")

cur.execute("DELETE FROM accounts")  
cur.execute("INSERT INTO accounts VALUES(1, 1000)")
cur.execute("INSERT INTO accounts VALUES(2, 1000)")
conn.commit()

try:
    # Transaction start
    print("Before Transaction:")
    cur.execute("SELECT * FROM accounts")
    print(cur.fetchall())

    cur.execute("UPDATE accounts SET balance = balance - 500 WHERE id = 1")
    cur.execute("UPDATE accounts SET balance = balance + 500 WHERE id = 2")
    # Force error (for rollback demo)
    x = 10 / 0  
    # Commit (won’t run due to error)
    conn.commit()

except:
    print("Error occurred! Rolling back...")
    conn.rollback()

# Final data
print("\nAfter Transaction:")
cur.execute("SELECT * FROM accounts")
print(cur.fetchall())

conn.close()
