import random
tablica=[]

print("Podaj elementy tablicy: ")
for i in range (0, 14):
  tablica.append(float(input()))

def szukaj(tablica):
    i=0
    a=len(tablica)
    while i<a:
        i+=1
        if tablica[i]>=6:
            return True
        else: 
            i+=1
            return False
print(tablica)
print(szukaj(tablica))
    