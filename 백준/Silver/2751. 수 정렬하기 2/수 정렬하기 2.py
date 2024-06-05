import sys
n = int(sys.stdin.readline())
arr = [0] * 2000001
for _ in range(n):
    inp = int(sys.stdin.readline())
    arr[inp+1000000] += 1
for i in range(0, 2000001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i-1000000)