n=int(input("Podaj liczbe calkowita "))
d=2
def czy_pierwsza(n):
    pierwsza = bool
    if n>1:
        pierwsza=True
    else:
        pierwsza=False
    while pierwsza and d**2<=n:
        if n%d==0:
            pierwsza=False
        else:
            d=d+1
    if pierwsza==True:
        print("Liczba jest pierwsza")
    elif pierwsza==False:
        print("Liczba nie jest pierwsza")

