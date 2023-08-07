from tkinter import *
import math


window = Tk()
window.minsize(height= 500, width=500)
window.title('Zadanie z geometrii analitycznej')



def kolko():
    p=int(promien.get())
    sr= [int(x) for x in srodek.get().split(",")]
    punkt= [int(x) for x in pu.get().split(",")]
    if math.sqrt(pow(punkt[0]-sr[0],2)+pow(punkt[1]-sr[1],2)) <= p:
        wynik=Label(text='Czy punkt należy do kolka? tak', font=('Arial', 13)).grid(column=0,row=11)
    else:
        wynik=Label(text='Czy punkt należy do kolka? nie', font=('Arial', 13)).grid(column=0,row=11)

pr=int
srodek_l=Label(text='Podaj wartość srodka: (x,y) ').grid(column=0, row=4)
srodek=Entry(width=30)
srodek.grid(column=0,row=5)
punkt_l=Label(text='Podaj współrzędne punktu: (x,y) ').grid(column=0, row=6)
pu=Entry(width=30)
pu.grid(column=0,row=7)
promien_l=Label(text='Podaj wartość promienia: ').grid(column=0, row=8)
promien=Entry(width=30)
promien.grid(column=0,row=9)
button = Button(text='dawaj',command=kolko)
button.grid(column=0, row=10)



window.mainloop()
