from tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np


class Zadanie1:
    d=int
    def __init__(self, prosta, punkt):
        self.prosta = prosta
        self.punkt = punkt

    def odleglosc(self):
        Zadanie1.d= abs(self.prosta[0]*self.punkt[0]+self.prosta[1]*self.punkt[1]+self.prosta[2])/math.sqrt(pow(self.prosta[0],2)*pow(self.prosta[1],2))
        if Zadanie1.d==0:
            return True
        else:
            return False


window = Tk()
window.minsize(height= 500, width=1000)
window.title('Zadanie z geometrii analitycznej')


def f(x,pros):
    return (pros[0]*x+pros[2])/pros[1]

def rys():
    pros= [int(x) for x in p.get().split(' ')]
    punk= [int(x) for x in pu.get().split(",")]
    xlist=np.linspace(-10,10)
    ylist=f(xlist,pros)
    plt.plot(xlist,ylist)
    plt.title("Rysunek funkcji")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.scatter([punk[0]], [punk[1]], color="red")
    plt.show()



def dane():
    prosta= [int(x) for x in p.get().split(' ')]
    punkt= [int(x) for x in pu.get().split(",")]
    dane=Zadanie1(prosta,punkt)
    wynik=Label(text=f'Czy punkt należy do prostej? {dane.odleglosc()}', font=('Arial', 16)).grid(column=0,row=8)




prosta_wyg=Label(text='Prostą reprezentujemy w ten sposób: Ax + By + C = 0', font=('Arial', 24)).grid(column=0, row=0)
prosta_l=Label(text='Podaj wartość A B C odzielone spacjami: ').grid(column=0, row=3)
p=Entry(width=30)
p.grid(column=0,row=4)
punkt_l=Label(text='Podaj współrzędne punktu: (x,y) ').grid(column=0, row=5)
pu=Entry(width=30)
pu.grid(column=0,row=6)
button = Button(text='dawaj',command=dane)
button.grid(column=0, row=7)
button_graph= Button(text='rysuj', command=rys)
button_graph.grid(column=2, row=7)





window.mainloop()
