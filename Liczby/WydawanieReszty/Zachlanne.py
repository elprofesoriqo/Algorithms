def change_greedy(amount: int, coins: []) -> int:
    result = 0
    i = 0
    
    while amount > 0:
        result += int(amount / coins[i])
        amount %= coins[i]
        i += 1

    return result


coins = [200, 100, 50, 20, 10, 5, 2, 1]
amount = 589

result = change_greedy(amount, coins)

print("Greedy algorithm")
print(f"Amount {amount} can be given out using {result} coins")