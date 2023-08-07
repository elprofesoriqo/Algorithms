n=int(input("Podaj ilość liczb w zbiorze: "))
t=[0]*n

for i in range(n):
    t[i]=input("Podaj liczbę: ")

rosnący=True
malejący=True
nierosnący=True
niemalejący=True

def monotoniczosc(t,rosnący, malejący, nierosnący, niemalejący):
    a=len(t)
    for i in range(a-1):
        if t[i]==t[i+1]:
            rosnący=False
            malejący=False
        if t[i]<t[i+1]:
            malejący=False
            nierosnący=False
        if t[i]>t[i+1]:
            rosnący=False
            niemalejący=False
        
    if rosnący==True:
        print(f"Ciąg {t} jest rosnący")
    if malejący==True:
        print(f"Ciąg {t} jest malejący")
    if nierosnący==True:
        print(f"Ciąg {t} jest nierosnący")
    if niemalejący==True:
        print(f"Ciąg {t} jest niemalejący")
    if rosnący==False and malejący==False and nierosnący==False and niemalejący==False:
        print(f"Ciąg jest niemonotoniczny")

print(monotoniczosc(t,rosnący, malejący, nierosnący, niemalejący))