import sys

c = int(sys.stdin.readline())
for i in range(c):
    n1, n2 = map(int, sys.stdin.readline().split())
    print("Case #", i+1, ": ", n1+n2, sep='')