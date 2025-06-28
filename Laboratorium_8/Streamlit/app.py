import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Aplikacja sprzedażowa - Streamlit")
st.write("Witaj w aplikacji sprzedażowej!")
st.header("Dodaj nowy rekord sprzedaży")

conn = sqlite3.connect('sales.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    date TEXT NOT NULL,
    latitude REAL,
    longitude REAL
)
''')
conn.commit()

product = st.text_input("Produkt")
quantity = st.number_input("Ilość", min_value=1, step=1)
price = st.number_input("Cena jednostkowa (zł)", min_value=0.0, step=0.1)
date = st.date_input("Data sprzedaży")

latitude = st.number_input("Szerokość geograficzna (latitude)", format="%.6f")
longitude = st.number_input("Długość geograficzna (longitude)", format="%.6f")

if st.button("Dodaj rekord"):
    c.execute('INSERT INTO sales (product, quantity, price, date, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)',
              (product, quantity, price, date.strftime('%Y-%m-%d'), latitude, longitude))
    conn.commit()
    st.success("Rekord został dodany!")
    st.balloons()

st.header("Tabela sprzedaży")
df = pd.read_sql_query("SELECT * FROM sales", conn)

products = df['product'].unique().tolist()
products.insert(0, 'Wszystkie')

selected_product = st.selectbox("Filtruj po produkcie", products)

if selected_product != 'Wszystkie':
    df = df[df['product'] == selected_product]

st.dataframe(df)
st.header("Wykresy sprzedaży")

if not df.empty:
    df['date'] = pd.to_datetime(df['date'])
    df['total'] = df['quantity'] * df['price']

    # Wykres sprzedaży dziennej
    daily_sales = df.groupby('date')['total'].sum().reset_index()
    fig1 = px.line(daily_sales, x='date', y='total', title='Sprzedaż dzienna (wartość)')
    st.plotly_chart(fig1)

    # Wykres suma produktów wg typu
    product_sales = df.groupby('product')['quantity'].sum().reset_index()
    fig2 = px.bar(product_sales, x='product', y='quantity', title='Suma sprzedanych produktów wg typu')
    st.plotly_chart(fig2)
else:
    st.info("Brak danych do wyświetlenia wykresów.")

# Mapa sprzedaży (ta część musi być osobno)
st.header("Mapa lokalizacji sprzedaży")

if not df.empty and df['latitude'].notnull().all() and df['longitude'].notnull().all():
    st.map(df[['latitude', 'longitude']])
else:
    st.info("Brak danych do wyświetlenia na mapie.")
