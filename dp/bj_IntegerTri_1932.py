import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(data[i])):
        if j == 0:
            data[i][j] = data[i-1][j] + data[i][j]
        elif j == (len(data[i]) - 1):
            data[i][j] = data[i-1][j-1] + data[i][j]
        else:
            data[i][j] = max(data[i-1][j], data[i-1][j-1]) + data[i][j]
print(max(data[n-1]))