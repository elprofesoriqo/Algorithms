n=int(input("Podaj liczbe: "))
d=2
while d*d<=n:
  if n%d==0:
    print(d)
    n=n//d
  else:
    d=d+1
print(n)