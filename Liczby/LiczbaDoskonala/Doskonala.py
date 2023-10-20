#n - liczba
from math import ceil, sqrt

def is_perfect(n: int) -> bool:
    suma_cyfr = 1
    
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            suma_cyfr += i
            
            if n // i != i:
                suma_cyfr += n // i

    return suma_cyfr == n


n = int(input("Podaj liczbę: "))

if is_perfect(n):
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')