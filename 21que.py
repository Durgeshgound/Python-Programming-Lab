#Write a program to connect to a database and create a table.

import sqlite3

# Step 1: Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("student.db")

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

print("Table created successfully!")

# Step 4: Commit changes
conn.commit()

# Step 5: Close connection
conn.close()