import sqlite3
import os

# Path where the database will be created
db_path = r"C:\Users\saksh\OneDrive\Desktop\app creation\mydatabase.db"

# Create a connection (this will create the file)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT
)
""")

# Insert sample products
products = [
    ("Laptop", 1200.50, "High-end gaming laptop"),
    ("Phone", 650.00, "Smartphone with high-resolution camera"),
    ("Headphones", 150.00, "Noise-cancelling headphones"),
    ("Smartwatch", 200.00, "Fitness smartwatch with GPS"),
    ("Tablet", 400.00, "10-inch tablet with stylus support")
]

cursor.executemany("INSERT INTO products (name, price, description) VALUES (?, ?, ?)", products)

# Commit and close
conn.commit()
conn.close()

# Confirm
if os.path.exists(db_path):
    print(f"Database successfully created at: {db_path}")
else:
    print("Database creation failed!")
