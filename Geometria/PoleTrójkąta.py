import math
def pole(boki,c):
    p=(boki[0]+boki[1]+c)/2
    pole=math.sqrt(p*(p-boki[0])*(p-boki[1])*(p-c))
    return round(pole,2)

b=str(input("Podaj wartość A B C odzielone spacjami: "))

boki= [int(x) for x in b.split()]
c=max(boki)
boki.remove(c)



if  boki[0]+boki[1]>c :
    print(True)
    print(f"Pole wynosi: {pole(boki,c)}")
else:
    print(False)

