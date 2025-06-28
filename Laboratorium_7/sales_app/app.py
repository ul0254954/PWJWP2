from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def query_db(query, args=()):
    conn = sqlite3.connect('sales.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    results = cur.fetchall()
    conn.close()
    return results

@app.route('/')
def index():
    return '''
    <h2>Filtry sprzedaży:</h2>
    <ul>
        <li><a href="/a">Sprzedaż Laptopów</a></li>
        <li><a href="/b">Dane z 2025-05-07 i 2025-05-08</a></li>
        <li><a href="/c">Transakcje powyżej 200 zł</a></li>
        <li><a href="/d">Łączna sprzedaż wg produktu</a></li>
        <li><a href="/e">Dzień z największą sprzedażą (ilość)</a></li>
    </ul>
    '''

@app.route('/a')
def laptop_sales():
    data = query_db("SELECT * FROM sales WHERE product = 'Laptop'")
    return render_template('result.html', title='Sprzedaż Laptopów', rows=data)

@app.route('/b')
def specific_dates():
    data = query_db("SELECT * FROM sales WHERE date IN ('2025-05-07', '2025-05-08')")
    return render_template('result.html', title='Dane z wybranych dni', rows=data)

@app.route('/c')
def expensive_sales():
    data = query_db("SELECT * FROM sales WHERE price > 200")
    return render_template('result.html', title='Sprzedaż > 200 zł', rows=data)

@app.route('/d')
def total_by_product():
    data = query_db("""
        SELECT product, SUM(quantity * price) AS total_sales
        FROM sales
        GROUP BY product
    """)
    return render_template('result.html', title='Łączna sprzedaż wg produktu', rows=data)

@app.route('/e')
def top_day():
    data = query_db("""
        SELECT date, SUM(quantity) AS total_quantity
        FROM sales
        GROUP BY date
        ORDER BY total_quantity DESC
        LIMIT 1
    """)
    return render_template('result.html', title='Najlepszy dzień sprzedaży (ilość)', rows=data)

if __name__ == '__main__':
    app.run(debug=True)
