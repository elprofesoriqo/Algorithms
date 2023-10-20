import random

def brown(x,y):
    x=0
    y=0
    n=50
    for i in range(n):
        dx=random.uniform(-1,1)
        dy=random.uniform(-1,1)
        x+=dx
        y+=dy