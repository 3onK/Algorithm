inp = list(str(input()))
result = 0

for i in inp:
    ch = ord(i)
    if 65 <= ch <= 67:
        result += 3
    elif 68 <= ch <= 70:
        result += 4
    elif 71 <= ch <= 73:
        result += 5
    elif 74 <= ch <= 76:
        result += 6
    elif 77 <= ch <= 79:
        result += 7
    elif 80 <= ch <= 83:
        result += 8
    elif 84 <= ch <= 86:
        result += 9
    elif 87 <= ch <= 90:
        result += 10
print(result)