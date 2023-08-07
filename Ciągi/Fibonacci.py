def fibrek(x): 
    if x<3: return 1 
    return fibrek(x-1) + fibrek(x-2) 
def fibit(x): 
    f1=1 
    f2=1 
    tmp=0 
    for i in range (2,x,1): 
        tmp=f2 
        f2=f1+f2 
        f1=tmp 
    return f2 
x=int(input("Podaj numer wyrazu w ciągu: ")) 
print("Rekurencyjnie: ",fibrek(x)) 
print("Iteracyjnie: ",fibit(x))