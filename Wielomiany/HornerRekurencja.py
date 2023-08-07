n=int(input("Podaj stopien"))
A=[0]*(n+1)
print("Podaj elementy wielomianu")
for i in range(0,(n+1)):
    A[i]=float(input())
x=float(input("Podaj wartosc argumentu"))

def Horner(n, A, x):
    if n==0:
        return A[0]
    return Horner(n-1, A, x)*x+A[n]
print(Horner(n,A,x))