import random
tab=[]


for i in range(20):
    tab.append(random.randint(1,50))

def maks(tab):
    m=tab[0]
    for i in tab:
        if i>m:
            m=i
    return m

def min(tab):
    m=tab[0]
    for i in tab:
        if i<m:
            m=i
    return m

print(f"W tablicy {tab} najmniejszym elementem jest liczba: {min(tab)}, a największym jest {maks(tab)}")