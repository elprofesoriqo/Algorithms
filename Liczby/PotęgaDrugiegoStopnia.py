def licz(bin, k):
    p=k
    for i in range(1, len(bin)):
        if bin[i] == 1:
            p=p*p*k
        else:
            p=p*p
    return p

def binarnie(x):
    if x == 0:
        return "0"
    b = []
    while x != 0:
        b.append(x%2)
        x = int(x/2)
    b.reverse() 
    return b


k=int(input("Podaj podstawę potęgi: "))
i=int(input("Podaj w jaki sposób podajesz potęgę: (0-binarka, 1-liczba) "))
if i ==0:
    liczby=input("Podaj reprezentacje binarną odzieloną spacjami: ")
    bin =[int(x) for x in liczby.split(" ")]
    print(f"Potęga o postaci {liczby} z liczby {k} wynosi: {licz(bin,k)}")
    print(bin)
if i==1:
    x=int(input("Podaj liczbę: "))
    bin=binarnie(x)
    print(f"Potęga o postaci {x} z liczby {k} wynosi: {licz(bin,k)}")
    print(bin)

