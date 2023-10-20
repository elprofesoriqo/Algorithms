import math


def change_dynamic(amount: int, coins: list):
    partial_results = [math.inf] * (amount + 1)
    used_coins = [math.inf] * (amount + 1)

    partial_results[0] = 0

    for coin_value in coins:
        for i in range(0, amount - coin_value + 1):
            if partial_results[i] + 1 < partial_results[i + coin_value]:
                partial_results[i + coin_value] = partial_results[i] + 1
                used_coins[i + coin_value] = coin_value

    if partial_results[amount] == math.inf:
        print("Cannot give out specified value using given coins")
        return

    print(f"Amount {amount} can be given out using {partial_results[amount]} coins")
    print("Used coins:")
    
    i = amount
    while i > 0:
        print(used_coins[i])
        i -= used_coins[i]


coins = [1, 2, 7, 10]
amount = 14

print("Dynamic algorithm")
change_dynamic(amount, coins)