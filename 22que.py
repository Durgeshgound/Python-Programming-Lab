#Write a program to perform INSERT, UPDATE, DELETE, and SELECT operations on a database.

import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)""")
conn.commit()

# 🔹 INSERT Operation
def insert_data():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   (name, age, course))
    conn.commit()
    print("Record inserted successfully!")

# 🔹 SELECT Operation
def select_data():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    print("\nStudent Records:")
    for row in rows:
        print(row)

# 🔹 UPDATE Operation
def update_data():
    id = int(input("Enter ID to update: "))
    name = input("Enter new name: ")
    
    cursor.execute("UPDATE students SET name = ? WHERE id = ?", (name, id))
    conn.commit()
    print("Record updated successfully!")

# 🔹 DELETE Operation
def delete_data():
    id = int(input("Enter ID to delete: "))
    
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    print("Record deleted successfully!")

# 🔹 Menu-driven program
while True:
    print("\n1. Insert")
    print("2. Display (Select)")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        insert_data()
    elif choice == 2:
        select_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")

# Close connection
conn.close()