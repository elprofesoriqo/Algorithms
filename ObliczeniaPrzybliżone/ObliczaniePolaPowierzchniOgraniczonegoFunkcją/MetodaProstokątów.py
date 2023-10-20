def f(x: float) -> float:
    return x * x + 2 * x


def metoda(a: int, b: int, n: int) -> float:
    szerokość = (b - a) / n
    area = 0
    punkt = a

    for i in range(n):
        punkt += szerokość
        wysokość = f(punkt)
        area += wysokość * szerokość

    return round(area,2)


a = 0 #początek
b = 10 #koniec
n = 100 #ilość prostokątów
j=str(input("Podaj jednostkę: ")).lower()

print(f"Powierzchnia wynosi: {metoda(a,b,n)}{j}2")