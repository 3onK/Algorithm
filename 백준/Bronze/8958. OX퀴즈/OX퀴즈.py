import sys

n = int(sys.stdin.readline())

for i in range(n):
    answer = list(sys.stdin.readline())
    point = 0
    count = 1
    for j in answer:
        if j =='O':
            point += count
            count += 1
        else:
            count = 1
    print(point)