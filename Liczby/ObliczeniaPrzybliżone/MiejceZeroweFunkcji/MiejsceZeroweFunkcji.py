from cmath import sin


def funkcja(x):
    return x * sin(x)

def bisekcja(a,b,delta):
    if funkcja(a)==0.0:
        return a
    if funkcja(b)==0.0:
        return b
    
    srodek=0
    while b-a > delta:
        srodek==(a+b)/2
        if funkcja(srodek)==0.0:
            return srodek
        if funkcja(a) * funkcja(srodek)<0.0:
            b= srodek
        else:
            a= srodek
        return (a+b)/2

a=-7
b=7
delta=0.001

print(f"Miejsce zerowe wynosi: {bisekcja(a,b,delta)}")