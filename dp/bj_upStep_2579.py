import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 301
data = [0] * 301
for i in range(n):
    data[i] = int(input())


dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(data[0], data[1]) + data[2]

for i in range(3, n):
    dp[i] = max(dp[i-2], dp[i-3] + data[i-1]) + data[i]

print(dp[n-1])
