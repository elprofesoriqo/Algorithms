def nwd(a: int, b: int) -> int:
    while b != 0:
        b2 = b
        b = a % b
        a = b2

    return a


a = 32
b = 12

result = nwd(a, b)

print(f"nwd({a},{b}) = {result}")