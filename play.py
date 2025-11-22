from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()

    # Ensure at least 10 products
    while len(products) < 10:
        products.append((0, f"Product {len(products)+1}", 99.99, "Amazing product"))

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
 