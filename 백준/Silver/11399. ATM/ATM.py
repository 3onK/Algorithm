n = int(input())
p = list(map(int, input().split()))
p.sort()
tmp = p[0]
for i in range(1, n):
    p[i] += tmp
    tmp = p[i]
print(sum(p))