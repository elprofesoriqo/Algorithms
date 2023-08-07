
def czy_pierwsza (a):
    for i  in range(1, a//2, 1):
        if a % i == 1:
            return 1
a = int(input("Podaj liczbe "))
if czy_pierwsza(a) == 1:
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")
