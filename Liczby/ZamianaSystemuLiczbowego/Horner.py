def horner(n,A,x):
  w=A[0]
  i=1
  while i<=n:
    i=i+1
    w=w*x+A[i]
  return w

A=[0]*100
n=int(input("Podaj ilość liczb: "))
x=2
print("Podaj elementy: ")
for i in range (0, (n+1)):
  A[i]=float(input())

print(horner(n,A,x))