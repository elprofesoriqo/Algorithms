def nwd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


a = 32
b = 12

result = nwd(a, b)

print(f"nwd({a}, {b}) = {result}")