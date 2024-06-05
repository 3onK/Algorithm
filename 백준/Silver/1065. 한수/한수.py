import sys

def d(n):
    result = 99
    
    if int(n)<100:
        return n
    else:
        for i in range(100, int(n)+1):
            count = 1
            num = list(str(i))
            a = int(num[1]) - int(num[0])
            pre = num[1]
            for i in num[2:]:
                if int(i) - int(pre) != a:
                    count = 0
                    break
                pre = i
            result += count
        return result

inp = sys.stdin.readline()
result = d(inp)
print(result)