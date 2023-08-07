
try:
    tekst = input("Podaj tekst: ").strip().lower()
    klucz = int(input("Podaj klucz: "))
except KeyboardInterrupt:
    print("\nPrzerwano przez użytkownika")
    exit()


def szyfr(message: str, key: int) -> str:
    encrypted = ""

    for letter in message:
        encrypted_letter = ord(letter) + key
        if encrypted_letter > ord("z"):
            encrypted_letter = ord("a") + encrypted_letter - ord("z")

        encrypted += chr(encrypted_letter)

    return encrypted




try:
    print(f"Zakodowany tekst:\n{szyfr(tekst, klucz)}")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
