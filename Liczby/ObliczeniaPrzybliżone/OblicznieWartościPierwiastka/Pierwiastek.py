def pierwiastek(pocz,kon,p,delta):
    pocz=(pocz+kon)/2
    kon=p/pocz
    s=(pocz+kon)/2
    if abs(pocz-kon)>delta:
        return pierwiastek(pocz,kon,p,delta)
    else:
        return s 
        pierwiastek(pocz,kon,p,delta)


p=int(input("Podaj pierwiastek: "))
delta=float(input("Podaj wartość delty: "))
pocz=1
kon=p
print(f"Wartość pierwiasta wynosi: {pierwiastek(pocz,kon,p,delta)}")