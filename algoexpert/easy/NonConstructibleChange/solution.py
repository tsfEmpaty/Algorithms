# O(nlogn) time | O(1) space - where n is the number of coins


def nonConstructibleChange(coins: list) -> int:
    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            break

        currentChangeCreated += coin
    return currentChangeCreated + 1


print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))  # 20
