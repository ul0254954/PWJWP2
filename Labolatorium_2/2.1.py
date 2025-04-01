class Ksiazka: 
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
    def opis(self):
        return f"Tytuł: {self.tytul}, Autor: {self.autor}, Rok wydania: {self.rok_wydania}"
    
class Ebook(Ksiazka): #Ebook dziedziczy atrybuty i metody klasy Ksiazka
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania) #super() oznacza: „weź metody z klasy nadrzędnej (czyli Ksiazka)” .__init__ to konkretne wywołanie konstruktora tej klasy
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        # użyj opis() z klasy Ksiazka + dodaj info o rozmiarze
        return super().opis() + f", Rozmiar pliku: {self.rozmiar_pliku} MB"

class Audiobook(Ksiazka):
    def __init__(self,tytul,autor,rok_wydania,czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania
    def opis(self):
        return super().opis() + f", Czas trwania: {self.czas_trwania} min."
    

k1 = Ksiazka("Wiedźmin", "Andrzej Sapkowski", 1994)
e1 = Ebook("Python Basics", "Jan Kowalski", 2020, 5.8)
a1 = Audiobook("Zaginiony Symbol", "Dan Brown", 2009, 1030)
print(k1.opis())
print(e1.opis())
print(a1.opis())