def nwd(a: int, b: int) -> int:
    if b == 0:
        return a
        
    return nwd(b, a % b)


a = 32
b = 12

result = nwd(a, b)

print(f"nwd({a},{b}) = {result}")