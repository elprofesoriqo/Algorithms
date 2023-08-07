import random
import math
def f(x):
    return -4*x*x+4*x

def sprawdzenie_wartości_punktu(x,y):
    if y>0 and y<=f(x):
        return 1
    elif y>0 and y<=f(x):
        return -1
    return 0

def losowanie_punktu(a,b):
    return random.uniform(a,b)

xp = int(input("Podaj początek całkowania: "))
xk = int(input("Podaj koniec przedziału: "))
n= int(input("Podaj dokładność całkowania w setkach punktów: "))
n=100
yp=0
yk=math.ceil(max(f(xp), f(xk)))


punktWy =0

for i in range(n):
    punktWy += sprawdzenie_wartości_punktu(losowanie_punktu(xp, yk), losowanie_punktu(yp, yk))

calka = punktWy/n * ((xk-xp)*(yk-yp))

print(f"Wartość całki wynosi: {calka}")