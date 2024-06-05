import sys

n, k = map(int, sys.stdin.readline().split())
coin = [0] * n
count = 0
for i in range(n):
    coin[i] = int(sys.stdin.readline())
coin.reverse()
while k>0:
    for j in coin:
        if k//j != 0:
            count += k//j
            k -= j * (k//j)
print(count)