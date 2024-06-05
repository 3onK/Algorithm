import sys

inp = int(input())
for i in range(inp):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(n1+n2)