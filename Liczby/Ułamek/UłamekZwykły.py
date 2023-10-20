def NWD(x, y):
    if y!=0:
        return NWD(y, x%y)
    else:
        return a
def NWW(x, y):
    return x * y // NWD(x, y)
#def dodawanie_ulamkow(x, y, z ,v, e, f):
#    e = x*(NWW(x, z))//y+ z*(NWW(y, v))//v
#    f = NWW(y, v)
#    print(e)
#    print("-")
#    print(f)#

a = int(input("Podaj licznik pierwszego ulamka "))
print("-")
b = int(input("Podaj mianownik pierwszego ulamka "))
c = int(input("Podaj licznik drugiego ulamka "))
print("-")
d = int(input("Podaj mianownik drugiego ulamka "))
e = a * (NWW(b, d)) // b + c * (NWW(b, d)) // d
f = NWW(b, d)
print(e)
print("-")
print(f)

calosci=0
while e >= f:
    calosci=calosci +1
    e=e-f
reszta=0
reszta=(e-f)*calosci
print(calosci)
print(reszta)
