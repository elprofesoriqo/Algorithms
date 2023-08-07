n=200000

T=[False]*n

i=2
def sito(T,n):
    for i in range (2, n):
        while i<n:
            k=2*i
            while k<=n:
                T[k]=True
                k+=i
            i+=i
(sito(T, n))


i=2
def czworacze (T,n):
    for i in range (2,n-8):
        if T[i] == 1 and T[i+2] == 1 and T[i+6] == 1 and T[i+8] == 1:
                print(i,i+2,i+6,i+8)
(czworacze(T,n))