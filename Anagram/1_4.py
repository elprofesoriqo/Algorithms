def anagram(slowo_1, slowo_2):
    return sorted(slowo_1) == sorted(slowo_2)

def slowa_wspolne(slowo_1, slowo_2):
    wspolne = 0
    rozne = 0
    min_len = min(len(slowo_1), len(slowo_2))

    for i in range(min_len):
        if slowo_1[i] == slowo_2[i]:
            wspolne += 1
        else:
            rozne += 1

    rozne += abs(len(slowo_1) - len(slowo_2))
    return rozne

with open('Anagram/dane.txt', 'r') as file:
    liczba_zmian = 0
    brak_zmian = 0
    for line in file:
        line = line.strip()
        words = line.split()

        if len(words) > 1:
            if anagram(words[0], words[1]):
                brak_zmian += 1
            else:
                liczba_zmian += slowa_wspolne(words[0], words[1])

print(f"Liczba wierszy z anagramami: {brak_zmian}")
print(f"Liczba wierszy bez anagramów: {liczba_zmian}")
