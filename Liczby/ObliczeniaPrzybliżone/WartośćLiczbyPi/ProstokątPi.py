from cmath import sqrt

def f(x: float) -> float:
    wynik = 1-x*x
    return sqrt(wynik.real)


def metoda(a: int, b: int, n: int) -> float:
    szerokość = (b - a) / n
    area = 0
    punkt = a

    for i in range(n):
        punkt += szerokość
        wysokość = f(punkt)
        area += wysokość * szerokość

    return area


a = -1 #początek
b = 1 #koniec
n = 50 #ilość prostokątów

print(f"Przybliona wartość liczby PI wynosi: {metoda(a,b,n)}")