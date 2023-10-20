def euklides_odejmowanie_rekurencyjne(a, b):
    # Jeśli b jest równe 0, to NWD to a.
    if b == 0:
        return a
    # W przeciwnym razie oblicz różnicę między a i b, a następnie
    # wywołaj funkcję rekurencyjnie dla nowej pary liczb (b i różnica).
    else:
        difference = abs(a - b)  # Odejmujemy wartość bezwzględną, aby uniknąć błędów w przypadku ujemnych liczb.
        return euklides_odejmowanie_rekurencyjne(b, difference)

# Przykład użycia:
a = 48
b = 18
nwd = euklides_odejmowanie_rekurencyjne(a, b)
print("Największy wspólny dzielnik ({}, {}) = {}".format(a, b, nwd))
