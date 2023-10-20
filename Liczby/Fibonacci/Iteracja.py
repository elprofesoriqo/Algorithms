def fib(n: int) -> int:
    f1 = 1
    f2 = 1
    
    for i in range(3, n + 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    return f2


n = 10

result = fib(n)

print(f"fib({n}) = {result}")