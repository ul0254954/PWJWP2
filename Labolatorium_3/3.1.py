class Asystent:
    def __init__(self, nazwa: str, wersja: str):
        self.nazwa = nazwa
        self.wersja = wersja

class AnalizaJezykowa:
    def analizuj_zapytanie(self, zapytanie: str) -> str:
        if "pogoda" in zapytanie.lower():
            return "intencja: prognoza pogody"
        return "intencja: nieznana"

class GeneratorOdpowiedzi:
    def generuj_odpowiedz(self, analiza: str) -> str:
        if "prognoza pogody" in analiza:
            return "Jutro będzie słonecznie z temperaturą 25°C."
        return "Przepraszam, nie rozumiem pytania."

class InteligentnyAsystent:
    def __init__(self, nazwa: str, wersja: str):
        self.asystent = Asystent(nazwa, wersja)
        self.analizator = AnalizaJezykowa()
        self.generator = GeneratorOdpowiedzi()

    def odpowiedz_na(self, zapytanie: str) -> str:
        analiza = self.analizator.analizuj_zapytanie(zapytanie)
        odpowiedz = self.generator.generuj_odpowiedz(analiza)
        return odpowiedz

asystent = InteligentnyAsystent("Linguo", "1.0")
print(asystent.odpowiedz_na("Jaka będzie jutro pogoda?"))

asystent = InteligentnyAsystent("Linguo", "1.0")
print(asystent.odpowiedz_na("Czy dzisiaj jest poniedziałek?"))