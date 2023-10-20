def rozszerzony_euklides(a, b):
    if b == 0:
        return a, 1, 0  # NWD(a, 0) = a, x = 1, y = 0
    else:
        nwd, x1, y1 = rozszerzony_euklides(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return nwd, x, y

# Przykład użycia:
a = 48
b = 18
nwd, x, y = rozszerzony_euklides(a, b)
print("Największy wspólny dzielnik ({}, {}) = {}".format(a, b, nwd))
print("Rozwiązanie równania {}x + {}y = {} to x = {}, y = {}".format(a, b, nwd, x, y))
