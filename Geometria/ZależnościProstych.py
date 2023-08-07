def row(prostal, prostak):
    if prostal[0]*prostak[1] - prostak[0]*prostal[1]==0:
        return True
    else: 
        return False

def pro(prostal, prostak):
    if prostak[0]*prostal[0]+prostal[1]*prostak[1]:
        return True
    else:
        return False


print("Jakie są proste")

l=str(input("Podaj wartość m, n odzielone spacjami: "))
k=str(input("Podaj wartość a, b odzielone spacjami: "))



prostal= [int(x) for x in l.split()]
prostak = [int(x) for x in k.split()]



if row(prostal, prostak) or pro(prostal,prostak) == True:
    print(f"Czy są równoległe: {row(prostal, prostak)}")
    print(f"Czy są prostodpadłe: {pro(prostal,prostak)}")
else:
    print("Proste są nijakie")
