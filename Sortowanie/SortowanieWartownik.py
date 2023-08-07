def Sortowanie(A,szk):
    n=len(A)
    A.insert(n,szk)
    i=0
    while A[i]!=szk:
        i+=1
    if i<n:
        print('Tak')
    else:
        print('Nie')

A=[3,5,2,3,4,5]
szk=int(input('Podaj element szukany'))

Sortowanie(A, szk)

