import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
result = a*b*c

for i in range(10):
    print(list(str(result)).count(str(i)))