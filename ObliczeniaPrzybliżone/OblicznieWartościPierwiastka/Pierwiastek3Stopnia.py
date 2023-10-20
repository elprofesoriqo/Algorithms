
def pierwiastek(p,delta):
    a=1
    b=p
    s=(a+b)/2
    while p-(s*s*s)>delta:
        if s*s*s>=p:
            b=s
        else:
            a=s
    return s

delta = float(input("Podaj wartość przybliżenia: "))
p=int(input("Podaj wartość pierwiastka: "))

print(f"Pierwiastek 3ciego stopnia z {p} wynosi: {pierwiastek(p,delta)}")