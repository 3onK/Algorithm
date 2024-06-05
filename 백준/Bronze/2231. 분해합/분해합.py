n = int(input())
for i in range(1, n+1):
    arr = list(map(int,str(i)))
    total = i + sum(arr)
    if total == n:
        print(i)
        break
    if i == n:
        print(0)