def czy_pierwsza(s):
    for i in range (2, s):
        if (s%i==0):
            return 0
        return 1

x=int(input("Podaj liczbe: "))

n=2
s=0
while x>2:
    while x%n==0:
        x=x/n
    print(n)
s=s+n
n=n+1

print("Suma wynosi: ")
print(s)

if czy_pierwsza(s)==1:
    print("Jest to liczba pierwsza")
else:
    print("Jest to liczba zlozona")