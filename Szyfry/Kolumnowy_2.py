try:
    tekst = input("Podaj tekst: ").strip().lower()
    klucz = input("Podaj klucz: ")
except KeyboardInterrupt:
    print("\nPrzerwano przez użytkownika")
    exit()


def szyfr(tekst,klucz):
    szyfr= ""
    while len(tekst)%len(klucz) != 0:
        tekst= tekst+"X" 

    for j in range(len(klucz)):
        for i in range(len(tekst) // len(klucz)):
            szyfr = szyfr+ tekst[i*len(klucz)+int(klucz[j])-1]
    return szyfr

try:
    print(f"Zakodowany tekst:\n{szyfr(tekst, klucz)}")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
