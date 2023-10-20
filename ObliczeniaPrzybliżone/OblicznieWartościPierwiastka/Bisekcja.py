def pierwiastek(p):
    a=1
    delta = 0.01
    b=p
    while abs(b-a)>delta:
        s=(a+b)/2
        if s*s<p:
            a=s
        else:
            b=s
    s=(a+b)/2
    return s

p=int(input("Podaj liczbę: "))

print(f"pierwiastek({p}) ~= {pierwiastek(p)}")