import random

n=int(input("Podaj liczbe elmentów tablicy: "))
T=[]
x=1
while x<=n:
    T.append(random.randint(-4,28))
    x+=1

def szukaj(T):
    i=0
    a=len(T)
    while i<a:
        i+=1
        if T[i]<9:
            return True
        else:
            i+=1
            return False


print(f"Elementy tablicy: {T}")
print(szukaj(T))