from typing import Dict, Optional

class Library:
    def __init__(self):
        self.books: Dict[str, int] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)


lib = Library()
lib.add_book("978-83-832-2774-0","Python dla każdego")
print(lib.find_book("978-83-832-2774-0"))
print(lib.find_book("123"))