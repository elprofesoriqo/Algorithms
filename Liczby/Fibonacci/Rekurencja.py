def fib(n: int) -> int:
    if n <= 2:
        return 1
        
    return fib(n - 1) + fib(n - 2)


n = 10

result = fib(n)

print(f"fib({n}) = {result}")