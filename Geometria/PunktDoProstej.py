import math

print("Czy punkt należy do prostej?????")


l=str(input("Podaj wartość A B C odzielone spacjami: "))
p=str(input("Podaj współrzędne punktu: (x,y) "))

prosta= [int(x) for x in l.split(" ")]
punkt = [int(x) for x in p.split(",")]


if abs(prosta[0]*punkt[0]+prosta[1]*punkt[1]+prosta[2])/math.sqrt(pow(prosta[0],2)*pow(prosta[1],2)) >0 :
    print(True)
else:
    print(False)