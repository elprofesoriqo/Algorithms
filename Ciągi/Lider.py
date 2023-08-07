n=int(input("Podaj ilość liczb w ciągu: "))
T=[0]*n
print("Proszę wprowadź liczby należące do ciągu: ")
for i in range(0,n):
    T[i]=int(input())


def szukaj_lidera(T):
    a=len(T)
    for i in range(a):
        ile=0
        for j in range(a):
            if T[j]==T[i]:
                ile+=ile
        if ile> a/2:
            return T[i]
        return -1

print(szukaj_lidera(T))