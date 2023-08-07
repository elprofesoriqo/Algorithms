import random

def podciag(n: int, tab: list) -> int:
    pod_ciag=[]
    poczatek=0
    max = 1
    length = 1
    p=0
    s=0
    for i in range(1, n):
        if tab[i]>tab[i-1]:
            length+=1
            if length>max:
                max=length
                poczatek=p
        else:
            p=i
            length=1

    for i in range(poczatek, poczatek+max):
        pod_ciag.append(tab[i])
        s=s+tab[i]

    return s

n = 10
tab = []

for i in range (n):
    tab.append(random.randint(-5,8))



print(f"Ciąg {tab}")
print(f"Suma elementów podciągu wynosi: {podciag(n,tab)}")