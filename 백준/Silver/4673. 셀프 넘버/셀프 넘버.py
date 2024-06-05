def d(n):
    num = int(n)
    for i in list(str(n)):
        num += int(i)
    return num

default_set = set(range(1,10001))
remove_set = set() 

for i in range(1, 10001):
    remove_set.add(d(i))

result = default_set - remove_set

for i in sorted(result):
    print(i)