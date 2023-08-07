import random

tablica=[]

for i in range(10):
    tablica.append(random.randint(5,41))


def szukaj(tablica):
    i=0
    a=len(tablica)
    while i<a:
        i=i+1
        if tablica[i]%2==0:
            return True
        else:
            i+=1
            return False
    
print(tablica)
print(szukaj(tablica))