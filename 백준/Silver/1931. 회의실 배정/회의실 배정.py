import sys

n = int(sys.stdin.readline())
i_list = [[0]*2 for _ in range(n)]
for i in range(n):
    s, f = map(int, sys.stdin.readline().split())
    i_list[i][0] = s
    i_list[i][1] = f
i_list.sort(key = lambda x: (x[1], x[0]))

count = 1
f_time = i_list[0][1]
for i in range(1, n):
    if i_list[i][0] >= f_time:
        count += 1
        f_time = i_list[i][1]
print(count)