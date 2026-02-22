#!/usr/bin/env python3

def min_coins(n, coins):
    # dp[x] = minimum number of coins needed to form sum x
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # base case

    for x in range(1, n + 1):
        for c in coins:
            if x - c >= 0:
                dp[x] = min(dp[x], dp[x - c] + 1)

    return dp[n]


# Coin denominations
coins = [1, 3, 4]

# Target sums
targets = [17, 33, 64, 71, 99]

for t in targets:
    print(f"{t} =", min_coins(t, coins))
