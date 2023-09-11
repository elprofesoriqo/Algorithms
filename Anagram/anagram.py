
def hasz(slowo):
    hasz_value=0
    for znak in slowo:
        hasz_value += ord(znak)
        hasz_value %= 256
    return hasz_value


def anagram(slowo_1, slowo_2):
    if sorted(slowo_1) == sorted(slowo_2):
        return True
    else:
        return False


with open('Anagram/dane.txt', 'r') as file:
    liczba_anagramow = 0
    liczba_kolizji = 0
    processed_lines = 0
    liczba_roznych_haszy = 0
    for line in file:
        line = line.strip()  
        processed_lines += 1

        words = line.split()

        if len(words) > 1:
            if hasz(words[0]) == hasz(words[1]):
                if anagram(words[0], words[1]):
                    liczba_anagramow +=1
                else:
                    liczba_kolizji +=1
            else:
                liczba_roznych_haszy +=1

        words.clear()
        if processed_lines >= 50:
            break

print(f"Liczba wierszy z anagramami: {liczba_anagramow}")
print(f"Liczba wierszy z kolizjami: {liczba_kolizji}")
print(f"Liczba wierszy z różnymi haszami: {liczba_roznych_haszy}")
