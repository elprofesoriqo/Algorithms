n=int(input("Podaj ilość liczb w ciągu: "))
T=[0]*n
print("Proszę wprowadź liczby należące do ciągu: ")
for i in range(0,n):
    T[i]=int(input())

def szukaj_lidera(T):
    a=len(T)
    sorted(T)
    ile=0
    k=n//2
    kandydat=T[k]
    for i in range(a):
        if T[i]==kandydat:
            ile+=ile
    if ile>n/2:
        return kandydat
    return -1



print(szukaj_lidera(T))