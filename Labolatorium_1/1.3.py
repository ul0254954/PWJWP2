class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def __str__(self):
        return f"Student: {self.name}, Wynik: {self.score}"
    
    def __eq__(self, other):
        return self.score == other.score 
    def __ne__(self, other):
        return self.score != other.score
    def __lt__(self, other):
        return self.score < other.score
    def __gt__(self, other):
        return self.score > other.score


s1 = Student("Ola", 85)
s2 = Student("Marek", 90)

print(s1 < s2)    # True
print(s1 > s2)    # False
print(s1 == s2)   # False
print(s1 != s2)   # True