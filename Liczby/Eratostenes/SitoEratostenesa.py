n=int(input("Podaj N: "))
t=[0]*(n+1)
def sito (t, n ):
    for i in range (2,n,1):
        t[i]=1
        i=2
        while i<=n:
            m=2*i
            while m<=n:
                t[m]=0
                m+=i
            while t[i]==0 & i<n:
                i=i+1
        for i in range (2,n,1):
            if t[i] == 1:
                print(i," ")
print( sito(t, n))