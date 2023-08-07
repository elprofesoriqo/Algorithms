import math
def Szukaj(lista, szk):
    p=len(lista)-1
    l=0
    if l<p:
        sr=(l+p)//2
        if szk==lista[sr]:
            return sr
        if lista[sr]<szk:
            l=sr+1
        else:
            p=szk-1

lista=[]
n=int(input("Podaj ilość wyrazów w ciągu: "))
for i in range(n):
    lista.append(int(input("Podaj wartość: ")))
szk=int(input("Podaj liczbę której szukasz: "))

print(f"Liczba posiada index {Szukaj(lista,szk)} w liście {lista} ")