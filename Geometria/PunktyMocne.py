import math

a=str(input("Podaj współrzędne punktu: (x,y) "))
b=str(input("Podaj współrzędne punktu: (x,y) "))
c=str(input("Podaj współrzędne punktu: (x,y) "))


punkta = [int(x) for x in a.split(",")]
punktb = [int(x) for x in b.split(",")]
punktc = [int(x) for x in c.split(",")]

l=math.sqrt(pow(punktb[0]-punkta[0],2)+pow(punktb[1]-punkta[1],2))

if math.sqrt(pow(punktc[0]-punkta[0],2)+pow(punktc[1]-punkta[1],2)) + math.sqrt(pow(punktc[0]-punktb[0],2)+pow(punktc[1]-punktb[1],2))==l:
    print("Super punkty")
else:
    print("Lipka uuu słaby punkt")