inp = int(input())
x = 0
row = 1

while x < inp:
    x += row
    row += 1
if row % 2 != 0:
    print((row-1)-(x-inp), "/", 1+(x-inp), sep="")
else:
    print(1+(x-inp), "/", (row-1)-(x-inp), sep="")