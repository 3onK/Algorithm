import sys

n = int(sys.stdin.readline())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    count = 0
    total = sum(arr[1:])
    avg = total/arr[0]
    for point in arr[1:]:
        if point > avg:
            count += 1
    result = count/arr[0]*100
    print("%0.3f" %round((result), 3)+"%")