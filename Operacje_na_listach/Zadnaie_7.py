import random
tab=[]

n=int(input("Podaj ilość liczb: "))

for i in range(n):
    tab.append(random.randint(-2,119))

def maks(tab):
    m=tab[0]
    for i in tab:
        if i>m:
            m=i
    return m

k=0
for i in tab:
    if maks(tab)==i:
        k+=1

print(f"Największa liczba z przedziału {tab} to liczba: {maks(tab)}, wystąpła ona {k} razy")