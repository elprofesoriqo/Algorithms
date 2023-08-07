from cmath import sin

def f(x):
    wynik = x * sin(x)
    return float(wynik.real) #convertowanie z coplex do float, bo sin daje notacje j
   

def zerowe(a,b):
    delta=0.001
    srodek=0

    if f(a)==0.0:
        return a
    if f(b)==0.0:
        return b
    
    
    while abs(b-a) > delta:
        srodek=(a+b)/2
        if f(srodek)==0:
            return srodek
        if f(a) * f(srodek)<0:
            b= srodek
        else:
            a= srodek
        return (a+b)/2

a=1
b=4
delta=0.001

print(f"Miejsce zerowe wynosi: {zerowe(a,b)}")
