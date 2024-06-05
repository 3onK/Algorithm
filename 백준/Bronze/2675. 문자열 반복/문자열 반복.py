import sys

inp = int(sys.stdin.readline())

for count in range(inp):
    inp1, inp2 = sys.stdin.readline().split()
    for i in list(str(inp2)):
        for j in range(int(inp1)):
            print(i, end="")
    print()
