def palindrom(word):
    najdluzszy = ""
    for i in range(len(word)):
        for j in range(i, len(word)):
            fragment = word[i:j+1]
            if fragment == fragment[::-1] and len(fragment) > len(najdluzszy):
                najdluzszy = fragment
    return najdluzszy

input_filename = "WUZ3_zad1_3_trening.txt"
output_filename = "WUZ3_zad1_3_trening_wynik.txt"

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    for line in input_file:
        words = line.strip().split()
        new_line = []

        for word in words:
            prefix = palindrom(word)
            odwrocenie = word[::-1]
            suffix = palindrom(odwrocenie)
            najdluzszy = max(prefix, suffix, key=len)
            new_line.append(najdluzszy) 
            new_line = " ".join(new_line)


        output_file.write(new_line + "\n")

