class zadanieX:
    def __init__(self,prosta_p1,prosta_p2,punkt1):
        self.prosta_p1 = prosta_p1
        self.prosta_p2 = prosta_p2
        self.punkt1 = punkt1


    def wyzn(self):
        return (self.punkt1[1]-self.prosta_p1[1])*(self.prosta_p2[0]-self.prosta_p1[0])-(self.prosta_p2[1]-self.prosta_p1[1])*(self.punkt1[0]-self.prosta_p1[0])


def wOdc(punkt_1, punkt_2, punkt_3):
    odl=zadanieX(punkt_1, punkt_2, punkt_3)
    if abs(odl.wyzn())>0:
        return False
    else:
        return True
        if punkt_3[0]>=min(punkt_1[0],punkt_2[0]) and punkt_3[0]<=max(punkt_1[0],punkt_2[0]) and punkt_3[1]>=min(punkt_1[1],punkt_2[1]) and punkt_3[1]<=max(punkt_1[1],punkt_2[1]):
            return True
        

def strona(punkt_1, punkt_2, punkt_3, punkt_4):
    odl_1=zadanieX(punkt_1, punkt_2, punkt_3)
    odl_2=zadanieX(punkt_1, punkt_2, punkt_4)
    if odl_1.wyzn()*odl_2.wyzn()>0:
        print("Leżą po tej samej stronie")
    else:
        return False
    
def przezodc(punkt_1, punkt_2, punkt_3, punkt_4):
    odl_1=zadanieX(punkt_1, punkt_2, punkt_3)
    odl_2=zadanieX(punkt_1, punkt_2, punkt_4)
    odl_3=zadanieX(punkt_3, punkt_4, punkt_1)
    odl_4=zadanieX(punkt_3, punkt_4, punkt_2)
    return True if odl_1.wyzn()*odl_2.wyzn()<0 and odl_3.wyzn()*odl_4.wyzn()<0 or wOdc(punkt_1, punkt_2, punkt_3) or wOdc(punkt_1, punkt_2, punkt_4) or wOdc(punkt_3, punkt_4, punkt_1) or wOdc(punkt_3, punkt_4, punkt_2)  else False


print("Współrzędne punktu odddziel przecinkiem x,y")
punkt_1 = str(input("Podaj współrzędne punktu: "))
punkt_2 = str(input("Podaj współrzędne punktu: "))
punkt_3 = str(input("Podaj współrzędne punktu: "))
punkt_4 = str(input("Podaj współrzędne punktu: "))

punkt_1 = [int(x) for x in punkt_1.split(',')]
punkt_2 = [int(x) for x in punkt_2.split(',')]
punkt_3 = [int(x) for x in punkt_3.split(',')]
punkt_4 = [int(x) for x in punkt_4.split(',')]

print(f"Czy punkt 3 zawiera się w prostej? {wOdc(punkt_1, punkt_2, punkt_3)}")
print(f"Czy punkty 3 i 4 są po tej samej stronie prostej? {strona(punkt_1, punkt_2, punkt_3, punkt_4)}")
print(f"Czy odcinki od punktów 1,2 i 3,4 się przecinają? {przezodc(punkt_1, punkt_2, punkt_3, punkt_4)}")