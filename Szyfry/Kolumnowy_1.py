try:
    tekst = input("Podaj tekst: ").strip().lower()
    klucz = input("Podaj klucz: ")
except KeyboardInterrupt:
    print("\nPrzerwano przez użytkownika")
    exit()

def szyfr(tekst, klucz):
    indeksy = sorted(range(len(klucz)), key=lambda k: klucz[k])
    
    naglowki = "\t".join([klucz[i] for i in indeksy])
    
    wiersze = []
    for i in range(0, len(tekst), len(klucz)):
        wiersz = tekst[i:i+len(klucz)]
        if len(wiersz) < len(klucz):
            wiersz += "X" * (len(klucz) - len(wiersz))
        wiersze.append(wiersz)
    
    tabela = ""
    for i in range(len(wiersze)):
        wiersz = [wiersze[i][indeksy[j]] for j in range(len(klucz))]
        tabela += "\t".join(wiersz) + "\n"
    
        return f"{naglowki}\n{tabela}"

try:
    print(f"Zakodowany tekst:\n{szyfr(tekst, klucz)}")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
