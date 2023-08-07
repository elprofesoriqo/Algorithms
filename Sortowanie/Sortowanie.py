import math
import random

def wybieranie(lista):
    for krok in range(len(lista)):
        min = krok # wyznaczenie minimum
        for i in range(krok +1, len(lista)): 
            if lista[i] < lista[min]: # szukamy najmniejszego elementu bez pierwszego, potem bez 2 itp.
                min=i
        lista[krok], lista[min] = lista[min], lista[krok] # zamiana miejscami
    return lista

def wstawianie(lista):
    for krok in range(1, len(lista)):
        pom = lista[krok] # przypisanie zmiennej pomocniczej wartość pierwszego elementu 
        j=krok-1 # przesuwamy pierwszy element 
        while j>=0 and pom < lista[j]:
            lista[j+1] = lista[j] # zamieniamy miejscami
            j=j-1 # ustawiamy pozycje elementu
        lista[j+1] = pom # wstawienie elementu mmniejszego
    return lista

def bombelek(lista):
    for element in range(len(lista)): # przeszukiwanie każdego elementu
        for j in range(0, len(lista)-element-1): # porównywanie elementów
            if lista[j]>lista[j+1]: 
                pom, lista[j], lista[j+1] = lista[j], lista[j+1], pom # zamiana wartości indeksu, pom- pomocnicza
    return lista

def szybszy_bombelek(lista): # w tym sortowaniu dokładamy sprawdzenie czy tablica była już posortowana aby nie sprawdzać ponownie
    for element in range(len(lista)): # przeszukiwanie każdego elementu
        zamiana = False
        for j in range(0, len(lista)-element-1): # porównywanie elementów
            if lista[j]>lista[j+1]: 
                pom, lista[j], lista[j+1] = lista[j], lista[j+1], pom # zamiana wartości indeksu, pom- pomocnicza
                zamiana = True
        if not zamiana:
            break
    return lista


def zliczanie(lista):
    size = len(lista) +1
    output = [0] * size
    count = [0] * size 

    for i in range(0, size):
        count[lista[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[lista[i]] - 1] = lista[i]
        count[lista[i]] -= 1
        i -= 1

    for i in range(0, size):
        lista[i] = output[i]

    return lista


def szybki(lista, poczatek, koniec):
    sr = lista[math.floor((poczatek + koniec)/2)]
    while poczatek < koniec:
        while lista[poczatek]< sr:
            poczatek+=1
        while lista[koniec]>sr:
            koniec-=1
        if poczatek <= koniec:
            lista[poczatek], lista[koniec] = lista[koniec], lista[poczatek]
            poczatek+=1
            koniec-=1
        if poczatek <koniec:
            szybki(lista, poczatek, koniec)
        if poczatek<koniec:
            szybki(lista, poczatek, koniec)
    return lista















lista = []
for i in range(10):
    lista.append(random.randint(-100, 100))
    random.shuffle(lista)
print(f"Lista początkowa: {lista}")
poczatek=0
koniec=9



print(f"Sortowanie poprzez wybieranie: {wybieranie(lista)}")
print(f"Sortowanie poprzez wstawianie: {wstawianie(lista)}")
print(f"Sortowanie poprzez bąbelkowanie: {bombelek(lista)}")
print(f"Sortowanie poprzez bąbelkowanie: {szybszy_bombelek(lista)}")
#print(f"Sortowanie poprzez zliczanie: {zliczanie(lista)}")
print(f"Sortowanie szybkie: {szybki(lista, poczatek, koniec)}")


