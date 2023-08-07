x=int(input("Podaj element, ktory chcesz znalezc"))
T=[2,3,54,6,7,34,234,2346,7834]
def Szukaj(T,x):
    i=0
    n=len(T)
    while i<n and T[i]!=x:
        i+=1
        if i==n:
            return False
    return True

if Szukaj(T,x) is True:
    print("Dany element znajduje sie w tablicy")
else:
    print("Danego elementu nie ma w tablicy")

