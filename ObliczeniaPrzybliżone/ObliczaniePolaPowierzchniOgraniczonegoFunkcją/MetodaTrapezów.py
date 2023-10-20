def f(x: float) -> float:
    return x * x + 2 * x


def metoda(a: int, b: int, n: int) -> float:
    wysokość = (b - a) / n
    area = 0
    punkt = a

    for i in range(n):
        bok_1 = f(punkt) #boki numerujemy od lewej do prawej
        punkt += wysokość
        bok_2 = f(punkt)
        area += ((bok_1 + bok_2) * wysokość) / 2

    return round(area,2)


a = 0 #początek
b = 10 #koniec
n = 100 #ilość trapezów
j=str(input("Podaj jednostkę: ")).lower()

print(f"Powierzchnia wynosi: {metoda(a,b,n)}{j}2")