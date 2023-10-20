import random
def carlo(n):
    z=0
    for i in range(n):
        x= random.uniform(-1,1)
        y=random.uniform(-1,1)
        if x*x+y*y<=1:
            z+=1
    return 4*(z/n)


n=int(input("Podaj ilość punktów: "))

print(f"Przybliżona wartość liczby PI wynosi: {carlo(n)}")