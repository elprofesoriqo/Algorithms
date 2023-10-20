from cmath import sqrt
def f(x: float) -> float:
    return sqrt(1-x*x)


def metoda(a: int, b: int, n: int) -> float:
    wysokość = (b - a) / n
    area = 0
    punkt = a

    for i in range(n):
        bok_1 = f(punkt) #boki numerujemy od lewej do prawej
        punkt += wysokość
        bok_2 = f(punkt)
        area += ((bok_1 + bok_2) * wysokość) / 2

    return area


a = -1 #początek
b = 1 #koniec
n = 100 #ilość trapezów

print(f"Przybliżenie liczby PI wynosi: {metoda(a,b,n)}")