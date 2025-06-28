from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Test – wyświetlenie pierwszych 10 liczb Fibonacciego
gen = fibonacci()
for _ in range(10):
    print(next(gen))