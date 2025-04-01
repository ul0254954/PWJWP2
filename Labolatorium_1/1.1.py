import json
 
class AplikacjaMobilna:
    liczba_pobran = 0
 
    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja
   
    def nowe_pobranie(self):
        AplikacjaMobilna.liczba_pobran += 1
   
    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran
 
    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)
        return cls(dane["nazwa"], dane["wersja"])
 
 
 
 
if __name__ == "__main__":
    try:
        aplikacja = AplikacjaMobilna.z_json("app.json")
        print(f"Nazwa:{aplikacja.nazwa}, Wersja:{aplikacja.wersja}")
 
        aplikacja.nowe_pobranie()
        print(f"Liczba pobrań: {AplikacjaMobilna.ile_pobran()}")
                   
    except FileNotFoundError:
        print("Błąd: Plik 'app.json' nie istnieje!")
 
    except json.JSONDecodeError:
        print("Błąd: Plik 'app.json' zawiera niepoprawne dane JSON!")