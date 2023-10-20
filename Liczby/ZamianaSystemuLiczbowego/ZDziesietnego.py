def konwersja_systemu_liczbowego(liczba, baza):
    if baza < 2 or baza > 16:
        return "Błędna baza. Obsługiwane bazy to 2-16."

    cyfry = "0123456789ABCDEF"
    wynik = ""

    if liczba == 0:
        return "0"  # Obsługuje przypadek, gdy liczba wejściowa wynosi 0.

    while liczba > 0:
        reszta = liczba % baza
        wynik = cyfry[reszta] + wynik
        liczba //= baza

    return wynik

# Przykład użycia:
liczba = int(input("Podaj liczbę dziesiętną: "))
baza = int(input("Podaj bazę systemu liczbowego (2-16): "))

wynik = konwersja_systemu_liczbowego(liczba, baza)
print("Wynik konwersji:", wynik)
