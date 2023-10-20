def pierwiastek(p):
    a=1
    b=p
    delta =0.001
    while abs(b-a) > delta:
        a=(a+b)/2
        b=p/a
    s=(a+b)/2
    return round(s,3)

p=int(input("Podaj liczbę: "))

print(f"pierwiastek({p}) ~= {pierwiastek(p)}")