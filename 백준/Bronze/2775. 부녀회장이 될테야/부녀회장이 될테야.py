inp = int(input())
 
for i in range(inp):
    k = int(input())
    n = int(input())
    arr = [a for a in range(1, n+1)]
    for floor in range(k):
        for room in range(1, n):
            arr[room] += arr[room-1]
    print(arr[-1])