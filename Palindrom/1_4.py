def slowa(slowa):
    najkrotsze = []
    for para_slow in slowa:
        word1, word2 = para_slow.split()
        if len(word1) <= len(word2):
            najkrotsze.append(word1)
        else:
            najkrotsze.append(word2)
    return najkrotsze

with open('plik_z_danymi.txt', 'r') as input_file:
    input_words = input_file.read().splitlines()

najkrotsze = slowa(input_words)

with open('WUZ3_zad1_4_trening_wynik.txt', 'w') as output_file:
    for word in najkrotsze:
        output_file.write(word + '\n')
