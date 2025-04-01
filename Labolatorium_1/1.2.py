class Matrix:
    def __init__(self, a, b, c, d,): #inicjowanie
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__(self): #wyświetlanie
        return f"[{self.a}, {self.b}]\n[{self.c}, {self.d}]"  #f"[{self.a}, {self.b}] - pierwszy wiersz, \n - nowa linia, [{self.c}, {self.d}]" - drugi wiersz
    def __add__(self, other): #self -> m1, other -> m2 dodawanie
        return Matrix(
            self.a + other.a,
            self.b + other.b,
            self.c + other.c,
            self.d + other.d
        )
    def __mul__(self,other): #mnożenie 
        a = self.a * other.a + self.b * other.c
        b = self.a * other.b + self.b * other.d
        c = self.c * other.a + self.d * other.c
        d = self.c * other.b + self.d * other.d
        return Matrix(a,b,c,d)
        

m1 = Matrix(1, 2, 3, 4)
m2 = Matrix(5, 4, 3, 2)
m3 = m1 + m2
m4 = m1 * m2
print(m1)
print()
print(m2)
print()
print(m3)
print()
print(m4)