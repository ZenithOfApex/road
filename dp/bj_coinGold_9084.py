# 123 더하기 변형? 버전
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, money+1):
            dp[i] += dp[i-coin]

    print(dp[money])
