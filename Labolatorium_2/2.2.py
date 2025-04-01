class UserNotFoundError(Exception): #klasa błędu "nie znaleziono użytkownika"
    pass
class WrongPasswordError(Exception): #klassa błędu złe hasło
    pass

class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self,username, password):
        if username not in self.users:
            raise UserNotFoundError("Użytkownik nie istnieje") 
        if self.users[username] != password:
            raise WrongPasswordError("Nieprawidłowe hasło")
        print("Zalogowano pomyślnie!") 

auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
    auth.login("admin", "1234")        #  Poprawne logowanie
    auth.login("unknown", "pass")      #  UserNotFoundError
    auth.login("user", "wrongpass")    #  WrongPasswordError
except Exception as e:
    print(f"Błąd: {e}")