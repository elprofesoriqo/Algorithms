import random

tab=[]
n=int(input("Ilość elementów: "))

for i in range(n):
    tab.append(random.randint(0, 33))

def szukaj(tab):
    i=0
    a=len(tab)
    while i<a:
        i+=1
        if tab[i]%3==1:
            return True
        else:
            return False

print(tab)

print(szukaj(tab))