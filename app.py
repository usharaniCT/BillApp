from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join('db', 'bills.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-bill', methods=['POST'])
def generate_bill():
    name = request.form['customer_name']
    product = request.form['product']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    total = quantity * price

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bills (customer_name, product, quantity, price, total)
        VALUES (?, ?, ?, ?, ?)''',
        (name, product, quantity, price, total)
    )
    conn.commit()
    conn.close()

    return render_template('bill_preview.html', name=name, product=product, quantity=quantity, price=price, total=total)

@app.route('/view-bills')
def view_bills():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bills")
    bills = cursor.fetchall()
    conn.close()
    return render_template('view_bills.html', bills=bills)

if __name__ == '__main__':
    if not os.path.exists(DB_PATH):
        print("Database not found. Run: python db/create_db.py")
    else:
        app.run(port=5001)
