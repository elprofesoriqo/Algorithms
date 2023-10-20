def konwersja_systemu_liczbowego(liczba, baza_wejsciowa, baza_wyjsciowa):
    if baza_wejsciowa < 2 or baza_wejsciowa > 16 or baza_wyjsciowa < 2 or baza_wyjsciowa > 16:
        return "Błędna baza. Obsługiwane bazy to 2-16."

    cyfry = "0123456789ABCDEF"
    wynik = ""

    if liczba == 0:
        return "0"  # Obsługuje przypadek, gdy liczba wejściowa wynosi 0.

    # Konwersja z bazy wejściowej na dziesiętną
    liczba_dziesietna = 0
    potega = 0
    while liczba > 0:
        reszta = liczba % 10
        liczba_dziesietna += reszta * (baza_wejsciowa ** potega)
        potega += 1
        liczba //= 10

    # Konwersja z dziesiętnej na bazę wyjściową
    while liczba_dziesietna > 0:
        reszta = liczba_dziesietna % baza_wyjsciowa
        wynik = cyfry[reszta] + wynik
        liczba_dziesietna //= baza_wyjsciowa

    return wynik

# Przykład użycia:
liczba = input("Podaj liczbę w systemie liczbowym: ")
baza_wejsciowa = int(input("Podaj bazę systemu wejściowego (2-16): "))
baza_wyjsciowa = int(input("Podaj bazę systemu wyjściowego (2-16): "))

wynik = konwersja_systemu_liczbowego(liczba, baza_wejsciowa, baza_wyjsciowa)
print("Wynik konwersji:", wynik)
