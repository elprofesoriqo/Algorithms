import math


def sqrt(n: int, p: float) -> float:
    x1 = n / 2
    x2 = (x1 + (n / x1)) / 2
    while math.fabs(x2 - x1) > p:
        x1 = (x2 + n / x2) / 2
        x1, x2 = x2, x1

    return x2


n = 9
p = 0.00000001

result = sqrt(n, p)

print(f"sqrt({n}) ~= {result}")