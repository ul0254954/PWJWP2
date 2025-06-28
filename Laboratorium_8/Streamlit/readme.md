# Aplikacja sprzedażowa - Streamlit

## Opis
Prosta aplikacja webowa stworzona w Pythonie przy użyciu Streamlit oraz SQLite.  
Umożliwia dodawanie rekordów sprzedaży, przeglądanie danych, filtrowanie po produkcie, wyświetlanie wykresów oraz prezentację lokalizacji sprzedaży na mapie.

## Funkcjonalności
- ✅ Dodawanie nowych rekordów sprzedaży (produkt, ilość, cena, data, lokalizacja)
- ✅ Filtrowanie danych po produkcie
- ✅ Wyświetlanie tabeli sprzedaży
- ✅ Wizualizacja sprzedaży dziennej na wykresie liniowym
- ✅ Wizualizacja sumy sprzedanych produktów na wykresie kolumnowym
- ✅ Wyświetlanie mapy lokalizacji sprzedaży
- ✅ Elementy interaktywne: formularze, selectbox, przyciski, animacja `st.balloons()`

## Technologie
- Python
- Streamlit
- SQLite
- Pandas
- Plotly

## Uruchomienie projektu

### 1. Przejdź do katalogu projektu w terminalu.
```bash
python -m venv venv
```
### 2. Uruchom środowisko
```bash
venv\Scripts\activate
```
### 3. Zainstaluj wymagane biblioteki
```bash
pip install -r requirements.txt
```
### 4. Uruchom komendą
```bash
streamlit run app.py