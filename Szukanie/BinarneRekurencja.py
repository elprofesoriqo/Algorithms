def Szukaj(T, szk):
    p=len(T)-1
    l=0
    if l>=p:
        middle=(l+p)//2
        if szk==T[middle]:
            return middle
    if szk<T[middle]:
        return(Szukaj(T,szk-1))
    else:
        return(Szukaj(T,szk+1))

T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
szk = 10
print(f"Liczba ma index {Szukaj(T,szk)} ")