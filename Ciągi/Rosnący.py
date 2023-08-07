n=int(input("Podaj ilość liczb w ciągu: "))
T=[0]*n
print("Proszę wprowadź liczby należące do ciągu: ")

for i in range(0,n):
    T[i]=int(input())

def grow(T):
    n=len(T)
    for i in range(n-1):
        if T[i]>= T[i+1]:
            return False
        return True


if grow(T)==True:
    print(f"Ciąg {T} jest rosnący.")
else:
    print(f"Ciąg {T} nie jest rosnący.")