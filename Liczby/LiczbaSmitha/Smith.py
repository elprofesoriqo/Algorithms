def czy_pierwsza(liczba):
    if liczba == 2:
        return True
    if liczba % 2 == 0 or liczba <= 1:
        return False

    pierw = int(liczba**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if liczba % dzielnik == 0:
            return False
    return True


liczba=int(input("Podaj liczbe: "))


def suma_cyfr(liczba):
    s=0
    while liczba>0:
        s+=liczba%10
        liczba/=10
    return s

def suma_rozklad(liczba):
    d=2
    suma=0
    while liczba!=1:
        while liczba%d==0:
            liczba//=d
            suma+=d
        d+=1
    return suma


while liczba>1:
    while czy_pierwsza(liczba)==False:
        while suma_cyfr(liczba)==suma_rozklad(liczba):
            print(f"Liczba {liczba} jest liczbą Smitha")
print(f"Liczba {liczba} nie jest liczbą Smitha")